from datetime import datetime
from utils import FERIA
from utils import ROMANS
from utils import day
from utils import days
from utils import easter
from utils import find_extra_epiphany
from utils import findsunday
from utils import week
from utils import weekday


EMBER_DAYS = []

### REFACTORED from temporal_cycle.py

class Temporal:
    """
    This class will enable us to explore parts of the liturgical year,
    rather than having to calulate the entire year. The exact implementation
    process is still being worked out, but this Class will be much easier
    to debug and develop rather than the previous idea, which is in 
    temporal_cycle.py.
    """
    def __init__(self, year):
        self.year = year
        self.easter = easter(self.year)
        self.septuagesima = self.easter - week(9)

    def start_year(self):
        """ Circumcision up to Septuagesima, excluding Epiphany """
        cir = day(self.year, 1, 1)
        y = {
                cir: "circumci",
                cir+days(1): "8stephen",
                cir+days(2): "8joannis",
                cir+days(3): "8innocen",
                }
        if (
                weekday(cir) == "Sun" 
                or weekday(cir) == "Mon" 
                or weekday(cir) == "Tue"
                ):
            y.update({day(self.year, 1, 2): "snomjesu"})
        else:
            y.update({cir-findsunday(cir)+week(1): "snomjesu"})

        return y

    def gesimas(self):
        """ Septuagesima to Quinquagesima """
        for i, x in enumerate(("septuage", "sexagesi", "quinquag")):
            # if x == "septuage":
            #     global SEPTUAGESIMA
            #     SEPTUAGESIMA = self.easter - week(9-i)
            y = {
                    self.easter - week(9-i): x,
                    }

            return y

    def epiphany(self):
        """ Epiphany and its Sundays """
        epiph = day(self.year, 1, 6)
        y = {
            epiph-days(1): "vigepiph",
            epiph: "epiphani",
            epiph+days(7): "8epiphan",
                }
        if weekday(epiph) == "Sun":
            epiph_1 = epiph+week(1)
        else:
            epiph_1 = epiph-findsunday(epiph)+week(1)
        # ec = 1
        # TODO: use range and get rid of the roman numerals
        for i, x in enumerate(ROMANS[0:6]):
            if weekday(epiph+days(i+1)) != "Sun":
                if weekday(epiph+days(i+1)) == "Sat":
                    y.update({epiph+days(i+1): "sabin8ep"})
                else:
                    y.update({epiph+days(i+1): "in8epi_"+ROMANS[i+1]})
            else:
                pass

        return y

    def post_epiphany(self):
        """  """
        c,o,y = day(self.year, 1, 6),0,{}
        while c.strftime('%m%d') != self.septuagesima.strftime('%m%d') and o+1 > 6:
            if ROMANS[o] == 'I':
                if c == day(self.year, 1, 13):
                    # TODO: add ferias
                    y.update({
                        c: "in8epiph",
                        c-days(1): "sfamijmj",
                        })
                else:
                    y.update({
                        c: "sfamdomi", # HACK: always first?
                        })
            else:
                y.update({c: "dp.epi_"+ROMANS[o]})
                for t in range(6):
                    y.update({c+days(t+1): "de.epi_"+ROMANS[o]})
        o+=1
        c+=week(1)

        return y

    def lent(self):
        y, ashweek = {}, ("dcinerum", "f5poscin","f6poscin", "sabbpcin")
        for c, x in enumerate([
            "quadra01", "quadra02", "quadra03",
            "quadra04", "passione", "inpalmis",
            ]):
            if x == "quadra01":
                for day, count in enumerate(ashweek):
                    y.update({self.easter-week(6-c)-days(4-0): day})
            y.update({self.easter-week(6-c): x})
            for j, f in enumerate(FERIA):
                y.update({self.easter-week(6-c)+days(j+1): x+f})
                pass

        return y

    def post_easter(self):
        y, d = {}, ("domresur", "in8re", "sabalbis")
        for j, x in enumerate(d):
            if d[j] == 1:
                for i in FERIA[1,-1]:
                    y.update({self.easter+days(j): x+i})
            else:
                y.update({self.easter+days(j): x})

        return y

    def paschaltime(self):
        y = {}
        pasch = ("domalbis", "dp.pas_", "dom8asce")
        for i, the_day in enumerate(pasch, start=1):
            if the_day == "dp.pas_":
                for num in ROMANS[1:5]: # FIXME: better way?
                    if num == "II":
                        y.update({# TODO: all days within the octave
                            self.easter+week(i)+days(3): "solstjos",
                            self.easter+week(i+1)+days(3): "8solsjos",
                            })
                    elif num == "V":
                        y.update({self.easter+week(i): the_day+str(i)})
                        pre_ascen = ("rogati_", "ascensio", "8ascensi")
                        for c, x in enumerate(pre_ascen):
                            if c == 0:
                                for r in range(1,4): # all rogations
                                    y.update({self.easter+week(i)+days(c): x+str(r)})
                            else:
                                y.update({
                                        self.easter+week(i)+\
                                                days(4 if x=="ascensio" else 11): x,
                                    })
                            # TODO: add all the days within the octave of ascension
                    else:
                        y.update({self.easter+week(i): the_day+str(i)})

        return y

    def key_points(self):
        """
        List of some important numbers for the calendar:
            [
                0. Number of Sundays after Pentecost,
                1. List of numerals of the displaced Epiphany Sundays,
                2. Date of the last Sunday of Advent,
            ]
        """
        christmas = datetime.strptime(str(self.year) + "-12-25", "%Y-%m-%d")
        lastadvent = christmas - findsunday(christmas)
        post_pent_sundays = int((((lastadvent - week(4))-self.easter+week(6))/7).days)-1
        # post_pent_count = self.easter+week(6) + week(4) # from the old method
        epiph_sunday_overflow = ROMANS[
                6-find_extra_epiphany(post_pent_sundays): \
                        find_extra_epiphany(post_pent_sundays)+2
                        ]
        return [post_pent_sundays, epiph_sunday_overflow, lastadvent]

    def pentecost(self):
        y = {}
        pent_date = self.easter + week(6)
        sundays_after_pentecost = self.key_points()[0]
        # Pentecost, Trinity Sunday, All the Sundays after
        # Ember Days
        # NOTE: just a placeholder for now... lots more to do
        for x in range(1, sundays_after_pentecost+1):
            y.update({ # NOTE: I think we want the arabic here
                pent_date+week(x): 'dp.pe_'+str(x)
                })
        return y

    def advent(self):
        y = {}
        advents = ["domadv_"]
        for x in range(4):
            y.update({ # NOTE: just propagates the Sundays
                self.key_points()[-1]-week(3+x): advents[0]
                })
        return y

    def build_entire_year(self) -> dict:
        """
        Returns a dictionary of the entire temporal cycle, but only the 
        dates with keys. This is for testing only.
        """
        y = {}
        y.update(self.advent())
        y.update(self.pentecost())
        y.update(self.paschaltime())
        y.update(self.post_easter())
        y.update(self.lent())
        y.update(self.post_epiphany())
        y.update(self.epiphany())
        y.update(self.gesimas())
        y.update(self.start_year())
        return dict(sorted(y.items()))

print(Temporal(2023).build_entire_year())
