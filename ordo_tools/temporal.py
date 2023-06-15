from datetime import datetime
from ordo_tools.utils import FERIA
from ordo_tools.utils import ROMANS
from ordo_tools.utils import day
from ordo_tools.utils import days
from ordo_tools.utils import easter
from ordo_tools.utils import find_extra_epiphany
from ordo_tools.utils import findsunday
from ordo_tools.utils import week
from ordo_tools.utils import weekday


EMBER_DAYS = []

class Temporal:
    """
    This class will enable us to explore parts of the liturgical year, rather
    than having to calulate the entire year. The exact implementation process
    is still being worked out, but this Class will be much easier to debug and
    develop rather than the previous idea, which is in OLD_temporal.py.
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
        for i, x in enumerate([ "septuage", "sexagesi", "quinquag" ]):
            y = {
                    self.easter - week(9-i): x,
                    }

            return y

    def epiphany(self):
        """ Epiphany and its Sundays """
        epiph = day(self.year, 1, 6)
        # NOTE: it is better to refactor this
        #       to use a list of events
        y = {
                epiph-days(1): "vigepiph",
                epiph: "epiphani",
                epiph+days(7): "8epiphan",
                }
        for x in range(8):
            # TODO: see if these are days within or special per day
            i = x+1 # from when we used enumerate...
            # TODO: skip the sunday after epiphany
            if weekday(epiph+days(i+1)) != "Sun":
                if weekday(epiph+days(i+1)) == "Sat":
                    y.update({epiph+days(i+1): "sabin8ep"})
                else:
                    y.update({epiph+days(i+1): "in8epi_"+str(i)})
            else:
                pass

        return y

    def post_epiphany(self):
        """ All of the Sundays and ferias after Epiphany """
        # NOTE: refactored & working
        epiphany = day(self.year, 1, 6)
        if weekday(epiphany) == "Sun":
            sun_after_epiphany = epiphany+week(1)
        else:
            sun_after_epiphany = epiphany-findsunday(epiphany)+week(1)
        date,i,y = sun_after_epiphany,0,{}
        while date != self.septuagesima and i+1 < 6:
            if i == 1:
                if date == day(self.year, 1, 13):
                    y.update({
                        date: "in8epiph",
                        date-days(1): "sfamijmj",
                        })
                else:
                    y.update({
                        date: "sfamdomi",
                        })
            else:
                y.update({date: "dom.epi_"+str(i+1)})
            for j in range(6):
                if j == 5:
                    d = "s"
                else:
                    d = j+2
                y.update({date+days(j+1): "de.epi_"+str(i+1)+"_"+str(d)})
            i+=1
            date+=week(1)

        return y

    def lent(self):
        y, ashweek = {}, ("dcinerum", "f5poscin","f6poscin", "sabbpcin")
        for c, x in enumerate([
            "quadra01", "quadra02", "quadra03",
            "quadra04", "passione", "inpalmis",
            ]):
            if x == "quadra01":
                for count, theday in enumerate(ashweek):
                    y.update({self.easter-week(6-c)-days(4-count): theday})
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
                # TODO: use the standard numbering format for the ferias
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

    # TODO: Advent, Pentecost, and Christmas have to be co-dependant, because
    #       they have overlapping dates. The same goes for Epiphany and Lent.

    def pentecost(self):
        y = {}
        pent_date = self.easter + week(7)
        y.update({
            pent_date: 'pentecost',
            })
        for fer in range(2,8):
            if fer != 7:
                y.update({
                    pent_date+days(fer-1): 'inpent_f'+str(fer)
                    })
            else:
                y.update({
                    pent_date+days(fer-1): 'inpent_fs'
                    })
        sundays_after_pentecost = self.key_points()[0]
        # NOTE: just a placeholder for now... lots more to do
        for x in range(1, sundays_after_pentecost+1):
            if x > 23: # HACK: just to prevent craziness
                break
            elif x == 1:
                y.update({
                    pent_date+week(x): 'trinity',
                    pent_date+week(x)+days(4): 'corpchris'
                    })
                # TODO: add octave within Corpus Christi
            else:
                y.update({
                    pent_date+week(x): 'dp.pe_'+str(x)
                    })
        return y

    def advent(self):
        y = {}
        advents = ["domadv_"]
        for x in range(4):
            if x == 0 and self.key_points()[-1]-week(x):
                y.update({
                    self.key_points()[-1]-week(x): 'dvig_chri'
                    })
            else:
                y.update({
                    self.key_points()[-1]-week(x): advents[0]+str(4-x)
                    })
        return y

    def christmas(self):
        y = {}
        christmas = day(year=self.year, month=12, day=25)
        christmas_days = [
                'christmas',
                'ststephan',
                'stjoannis',
                'stsinnoce',
                'stthomaem',
                'stsilvest',
                ]
        # BUG: this is not working for 2023
        if findsunday(christmas) == 0 or 1 or 2 or 3: # Sunday w/in octave occurs on 30 if the Sunday is on 25-28
            y.update({christmas + days(5) - findsunday(christmas): 'rdom8chr'}) # reposita
        else: # Sunday falls on the 29-31
            y.update({christmas + days(7) - findsunday(christmas): 'dom8chri'})
            print(christmas+days(7)-findsunday(christmas))
        if (
                int(day(self.year, month=12, day=30).strftime('%u')) == 1
                or int(day(self.year, month=12, day=30).strftime('%u')) == 7
                ):
            y.update({christmas+days(5): 'in8chr_5'})
        for i, feast in enumerate(christmas_days):
            if i == 0:
                if christmas-days(-1) == self.key_points()[-1]:
                    pass # prevents duplicate keys
                else:
                    y.update({christmas-days(1): 'vig_chri'})
                y.update({christmas: feast})
            else: # TODO: if one of these days coincide with the sunday...
                y.update({
                    christmas+days(i): feast
                    })
        return y

    def build_entire_year(self) -> dict:
        """
        Returns a dictionary of the entire temporal cycle, but only the 
        dates with keys. This is for testing only.
        """
        y = {}
        y.update(self.christmas())
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

