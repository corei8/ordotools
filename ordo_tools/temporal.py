from ordo_tools.utils import FERIA
from ordo_tools.utils import ROMANS
from ordo_tools.utils import day
from ordo_tools.utils import days
from ordo_tools.utils import easter
from ordo_tools.utils import find_extra_epiphany
from ordo_tools.utils import findsunday
from ordo_tools.utils import week
from ordo_tools.utils import weekday

# TODO: Add the Ember Days

class Temporal:
    """
    This class will enable us to explore parts of the liturgical year, rather
    than having to calulate the entire year. The exact implementation process
    is still being worked out, but this Class will be much easier to debug and
    develop rather than the previous idea, which is in OLD_temporal.py.

    For the various parts of the year that require more advanced
    configurations, (e.g. the O-antiphons) this modular approach will allow the
    parts of the year to be self-calculated, which will be more efficient in
    the long run, and allow for much easier debugging. Having already trued the
    "figure it out in one go" approach, I can tell you that this is the way to
    go.

    -- Fr. Barnes, June 17, 2023
    """

    def __init__(self, year):
        self.year = year
        self.easter = easter(self.year)
        self.septuagesima = self.easter - week(9)
        self.christmas = day(year=self.year, month=12, day=25)
        self.lastadvent = self.christmas - findsunday(self.christmas)

    def advent(self) -> dict:
        """ Advent Season """
        y = {}
        for x in range(4): # build the advents backwards?
            if x == 0 and self.christmas-days(1) == self.lastadvent:
                y |= { self.lastadvent: "DV_Christmas" }
            else:
                y |= { self.lastadvent-week(x): f"D_Advent_{4-x}" }
                for fer in range (2,8):
                    y |= {
                        self.lastadvent-week(x)+days(fer-1):
                        f"Advent_{4-x}_f{fer if fer != 7 else 's'}"
                    }
        return y

    def christmas_time(self) -> dict:
        """ Christmas and the following days to the end of the year. """
        y = {}
        christmas_weekdays = [
            'Christmas', 'StStephan', 'StJohn', 'StsInnocents', 'StThomas', 'StSylvester',
        ]
        christmas_sundays = [
            'D_StThomas', 'D_StSylvester',
        ]
        dom_in_octave = ''
        if ( # Sunday falls on St. Thomas or St. Sylvester:
            findsunday(self.christmas) == days(2) or
            findsunday(self.christmas) == days(3)
                ):
            dom_in_octave = self.christmas+days(7)-findsunday(self.christmas)
            y |= { # office of the sixth day fall on Dec. 30
                      self.christmas-days(5):
                      "8_Chritmas_f6"
                      }
        elif ( # Sunday falls on the first three days of the octave:
                findsunday(self.christmas) == days(6) or
                findsunday(self.christmas) == days(5) or
                findsunday(self.christmas) == days(4)
            ):
            y |= { self.christmas+(days(5)): "D_Christmas" }
            pass
        else:
            y |= { self.christmas+(days(7)-findsunday(self.christmas)): "D_Christmas" }
        for i, feast in enumerate(christmas_weekdays):
            if i == 0:
                if self.christmas-days(1) == self.lastadvent:
                    pass # prevents duplicate keys
                else:
                    y |= {self.christmas-days(1): 'V_Christmas'}
                y |= {self.christmas: feast}
            elif self.christmas+days(i) == dom_in_octave:
                y |= { dom_in_octave: christmas_sundays[i-4] }
            else:
                y |= { self.christmas+days(i): feast }
        return y

    def start_year(self) -> dict:
        """ Circumcision up to Septuagesima, excluding Epiphany """
        circumcision = day(self.year, 1, 1)
        y = {
            circumcision: "Circumcision",
            circumcision+days(1): "8_Stephen",
            circumcision+days(2): "8_John",
            circumcision+days(3): "8_Innocents",
        }
        if (
                weekday(circumcision) == "Sun" 
                or weekday(circumcision) == "Mon"
                or weekday(circumcision) == "Tue"
                ):
            y |= {day(self.year, 1, 2): "SNameJesu+8_Ste"}
        else:
            y |= {circumcision-findsunday(circumcision)+week(1): "SNameJesus"}
        return y

    def epiphany(self) -> dict:
        """ Epiphany and its Sundays """
        epiphany = day(self.year, 1, 6)
        y = {
            epiphany-days(1): "V_Epiphany",
            epiphany: "Epiphany",
            epiphany+days(7): "8_Epiph",
        }
        for x in range(1,7):
            if weekday(epiphany+days(x)) != "Sun":
                if weekday(epiphany+days(x)) == "Sat":
                    y |= {epiphany+days(x): "8_Epiph_fs"}
                else:
                    the_date = epiphany+days(x)
                    # TODO: see if these are days within or proper per day
                    y |= {
                        the_date: "8_Epiph_f"+str(int(the_date.strftime('%w'))+1)
                    }
            else:
                pass
        return y

    def post_epiphany(self) -> list:
        """ All of the Sundays and ferias after Epiphany """
        epiphany = day(self.year, 1, 6)
        if weekday(epiphany) == "Sun":
            sun_after_epiphany = epiphany+week(1)
        else:
            sun_after_epiphany = epiphany-findsunday(epiphany)+week(1)
        date,i,y = sun_after_epiphany,0,{}
        while date != self.septuagesima and i+1 < 6:
            if i == 1:
                if date == day(self.year, 1, 13):
                    y |= {
                        date: "in8epiph", # FIXME: what does this mean?
                        date-days(1): "HolyFamily",
                    }
                else:
                    y |= { date: "D_HolyFamily" }
            else:
                y |= {date: "D_Epiph_"+str(i+1)}
            for j in range(6):
                if j == 5:
                    d = "s"
                else:
                    d = j+2
                y |= {date+days(j+1): "de_Epiph_"+str(i+1)+"_"+str(d)}
            i+=1
            date+=week(1)
        return [y,i+1] # index 1 is the Epiphany Sunday not used before Septuagesima

    def gesimas(self) -> dict:
        """ Septuagesima to Quinquagesima """
        y = {}
        for i, x in enumerate(["Septuagesima", "Sexagesima", "Quinquagesima"]):
            pre_lent_week = self.easter - week(9-i)
            y |= {pre_lent_week: x}
            for feria in range(6):
                if pre_lent_week+days(feria) == self.easter-week(6)-days(5):
                    break
                else:
                    y |= {pre_lent_week+days(feria+1): f"de_{x[0:4]}_f{feria+2 if feria != 5 else 's'}"}
        return y
            
    def lent(self) -> dict:
        """ All of the Sundays and ferias of Lent, up to Easter """
        for i in range(7):
            if i == 0:
                y = {
                    self.easter-week(7-i)+days(3+c):\
                    f"""{"de_" if c == 0 else ""}AshWed{f"_f{c+4 if c != 3 else 's'}" if c != 0 else ""}"""\
                    for c in range(4)
                }
            else:
                for j in range(7):
                    y |= {
                        self.easter-week(7-i)+days(j):
                        f"""{"D" if j == 0 else "de"}_{"Lent" if i < 5 else "Passion" if i != 6 else "Palm"}{f"_f{j if j != 6 else 's'}" if j != 0 else f"_{i}"}"""
                    }
        return y

    def post_easter(self) -> dict:
        """ Easter Week """
        d = ["Easter", "8Easter_f", "WhitSaturday"]
        for j, feast in enumerate(d):
            if j == 0:
                y = {self.easter: feast}
            elif j == 1:
                for i in range(2,7):
                    y |= {self.easter+days(j+i-2): f"{feast}{i}"}
            else:
                y |= {self.easter+days(6): feast}
        return y

    def paschaltime(self) -> dict:
        """
        From Whit Sunday to Pentecost
        There is probably a better way to implement this,
        but this works for now. Not too easy to debug; 
        that is why there are more comments than ususal.
        """
        y = {}
        for i in range(1,7):
            if i == 1:
                the_sunday = "WhitSunday"
            elif i == 6:
                the_sunday = "D_Ascension"
            else:
                the_sunday = f"D_Easter_{i}"
            d = 1 # easily matches monday with days(1)
            while d != 7:
                if i == 3 and d >= 3:
                    if d == 3:
                        y |= {
                            self.easter+week(i)+days(d): "StJoseph",
                            self.easter+week(i+1)+days(3): "8StJoseph",
                        }
                    else:
                        y |= {self.easter+week(i)+days(d): f"in_8StJoseph"}
                elif i == 4 and d <= 3:
                    if d == 3:
                        pass
                    else:
                        y |= {self.easter+week(i)+days(d): f"in_8StJoseph"}
                elif i == 5: # the whole week is special
                    if d <= 3: # rogations
                        y |= {self.easter+week(i)+days(d): f"Rogation_{d}"}
                    elif d > 3:
                        y |= {self.easter+week(i)+days(d): f"""{"in_8" if d != 4 else ""}Ascension"""}
                elif i == 6 and d < 5:
                    y |= {self.easter+week(i)+days(d): f"""{"in_8" if d != 4 else "8"}Ascension"""}
                else:
                    y |= {self.easter+week(i)+days(d): f"de_Easter_{i}_f{d+1 if d != 6 else 's'}"}
                d += 1
            y |= {self.easter+week(i): the_sunday}
        return y

    def pentecost(self) -> dict:
        """
        All of the days after Pentecost, with Corpus Christi
        """
        # TODO: add the other temporal octaves. Sacred Heart?
        pentecost_date = self.easter + week(7)
        last_pent = self.christmas - findsunday(self.christmas) - week(4)
        # Add Pentecost and its ferias:
        y = {pentecost_date: 'Pentecost'}
        for fer in range(2,8): # Pentecost week ferias
            y |= {pentecost_date+days(fer-1): f"8Pent_f{fer if fer != 7 else 's'}"}
        x,e = 1,0
        while pentecost_date+week(x) != last_pent+week(1): # i.e., Advent 1
            sunday_date, leftovers = pentecost_date+week(x), self.post_epiphany()[1]
            if pentecost_date+week(x) == last_pent-week(6-leftovers)+week(e):
                sunday = f'Epiph_{leftovers+e}_{x}'
                e += 1
            else:
                sunday = f'Pent_{x}'
            d = 0
            while d < 7:
                if x == 1 and d == 0:
                    y |= {sunday_date: "Trinity"}
                elif x == 1 and d >= 4:
                    y |= {sunday_date+days(d): f"{'in_8' if d > 4 else ''}CorpusChristi"}
                elif x == 2 and 0 < d <= 4:
                    y |= {sunday_date+days(d): f"{'in_8' if d < 4 else '8'}CorpusChristi"}
                elif x == 2 and d >= 5:
                    y |= {sunday_date+days(d): f"{'in_8' if d > 5 else ''}SacredHeart"}
                elif x == 3 and 0 < d <= 5:
                    y |= {sunday_date+days(d): f"{'in_8' if d < 5 else '8'}SacredHeart"}
                else:
                    y |= {sunday_date+days(d): f"""{"de" if d != 0 else "D"}_{sunday}{f"_f{d+1 if d != 6 else 's'}" if d != 0 else ""}"""}
                d += 1
            x += 1
        return y

    def build_entire_year(self) -> dict:
        """
        Returns a dictionary of the entire temporal cycle, but only the 
        dates with keys. This is for testing only.
        """
        y = {}
        y |= self.advent()
        y |= self.christmas_time()
        y |= self.start_year()
        y |= self.epiphany()
        y |= self.post_epiphany()[0]
        y |= self.gesimas()
        y |= self.lent()
        y |= self.paschaltime()
        y |= self.post_easter()
        y |= self.pentecost()
        return dict(sorted(y.items()))

