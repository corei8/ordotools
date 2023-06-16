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
        # NOTE: refactored and working
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
        # NOTE: refactored and working
        y = {}
        for i, x in enumerate([ "septuage", "sexagesi", "quinquag" ]):
            y.update({self.easter - week(9-i): x})
        return y

    def epiphany(self):
        """ Epiphany and its Sundays """
        # NOTE: refactored and working
        epiphany = day(self.year, 1, 6)
        y = {
                epiphany-days(1): "vigepiph",
                epiphany: "epiphani",
                epiphany+days(7): "8epiphan",
                }
        for x in range(1,7):
            if weekday(epiphany+days(x)) != "Sun":
                if weekday(epiphany+days(x)) == "Sat":
                    y.update({epiphany+days(x): "in8ep_fs"})
                else:
                    the_date = epiphany+days(x)
                    y.update({
                        the_date: "in8epi_f"+str(int(the_date.strftime('%w'))+1)
                        })
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
        """ All of the sundays and ferias of Lent, up to Easter """
        # NOTE: not quite refactored, but working
        y, ashweek = {}, ("dcinerum", "f5poscin","f6poscin", "sabbpcin")
        for c, x in enumerate([ # we can shorten this...
            "quadra01", "quadra02", "quadra03",
            "quadra04", "passione", "inpalmis",
            ]):
            if x == "quadra01":
                for count, theday in enumerate(ashweek):
                    y.update({self.easter-week(6-c)-days(4-count): theday})
            y.update({self.easter-week(6-c): x})
            # TODO: we need the feast of the Seven Sorrows
            for j, f in enumerate(FERIA): # this is just dumb, but it is working
                # TODO: introduce holy week; not needed, but nice viusal
                y.update({self.easter-week(6-c)+days(j+1): x+f})
                pass
        return y

    def post_easter(self):
        """ Easter Week """
        # NOTE: refactored and working
        y, d = {}, ("domresur", "in8resur_f", "sabalbis")
        for j, feast in enumerate(d):
            if j == 0:
                y.update({self.easter: feast})
            elif j == 1:
                for i in range(2,7):
                    y.update({self.easter+days(j+i-2): feast+str(i)})
            else:
                y.update({self.easter+days(6): feast})
        return y

    def paschaltime(self):
        """ From Whit Sunday to Pentecost """
        # NOTE: refactored and working
        # TODO: work on the octaves
        y = {}
        for i in range(1,7):
            if i == 1:
                the_day = "domalbis"
            elif i == 6:
                the_day = "dom8asce"
            else:
                the_day = "dom.pasch_"+str(i)
                if i == 3:
                    y.update({
                        self.easter+week(i)+days(3): "solstjos",
                        self.easter+week(i+1)+days(3): "8solstjos"
                    })
                elif i == 5:
                    pre_ascen = ("rogati_", "ascensio", "8ascensi") 
                    for c, x in enumerate(pre_ascen):
                        if c == 0:
                            for r in range(1,4):
                                y.update({self.easter+week(i)+days(r): x+str(r)})
                        else:
                            y.update({
                                      self.easter+week(i)+\
                                      days(4 if x=="ascensio" else 11): x,
                                      })
            y.update({self.easter+week(i): the_day})
        return y

    def key_points(self):
        """
        List of some important numbers for the calendar:
            [
                    0. Date of the last Sunday after Pentecost,
                    1. List of numerals of the displaced Epiphany Sundays,
                    2. Date of the last Sunday of Advent,
                    ]
        """
        christmas = day(year=self.year, month=12, day=25)
        lastadvent = christmas - findsunday(christmas)
        # BUG: this is not working:
        post_pent_sundays = (((lastadvent - week(4))-self.easter+week(7))/7).days
        last_pent = lastadvent - week(4)
        # post_pent_count = self.easter+week(6) + week(4) # from the old method
        epiph_sunday_overflow = ROMANS[ # BUG: this is not working and is kinda dumb
                6-find_extra_epiphany(post_pent_sundays): \
                        find_extra_epiphany(post_pent_sundays)+2
                        ]
        return [last_pent, epiph_sunday_overflow, lastadvent]

    # TODO: Advent, Pentecost, and Christmas have to be co-dependant, because
    #       they have overlapping dates. The same goes for Epiphany and Lent.

    def pentecost(self):
        # NOTE: refactored and working somewhat
        y = {}
        pent_date = self.easter + week(7)
        y.update({pent_date: 'pentecost'})
        for fer in range(2,8):
            if fer != 7:
                y.update({ pent_date+days(fer-1): 'inpent_f'+str(fer) })
            else:
                y.update({ pent_date+days(fer-1): 'inpent_fs' })
        x = 1
        while pent_date+week(x) != self.key_points()[0]:
            if x == 1:
                y.update({
                    pent_date+week(x): 'trinity',
                    pent_date+week(x)+days(4): 'corpchris'
                    })
                # TODO: add octave within Corpus Christi
            else:
                y.update({ pent_date+week(x): 'dp.pe_'+str(x) })
            x+=1
        y.update({ pent_date+week(x): 'dp.pe_'+str(x) })
        # TODO: introduce the sundays after epiphany
        return y

    def advent(self):
        # NOTE: refactored and working
        advents = ["domadv_"]
        y = {}
        for x in range(4):
            if x == 0 and self.key_points()[-1]-week(x):
                y.update({
                    self.key_points()[-1]-week(x): 'dvig_chri'
                    })
            else:
                y.update({
                    self.key_points()[-1]-week(x): advents[0]+str(4-x)
                    })
                for fer in range (2,8):
                    y.update({
                        self.key_points()[-1]-week(x)+days(fer-1):
                        "fer.adv_"+str(4-x)+"_"+(str(fer) if fer != 7 else "s")
                    })
        return y

    def christmas(self):
        y = {}
        # TODO: make christmas a class variable
        christmas = day(year=self.year, month=12, day=25)
        christmas_days = [
                'christmas',
                'ststephan',
                'stjoannis',
                'stsinnoce',
                'stthomaem',
                'stsilvest',
                ]
        # Sunday w/in octave occurs on 30 if the Sunday is on 25-28
        if findsunday(christmas) == 0 or 1 or 2 or 3:
            y.update({christmas + days(5) - findsunday(christmas): 'rdom8chr'})#reposita
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

