from utils import day
from utils import days
from utils import week
from utils import weekday
from utils import findsunday
from utils import easter
from utils import find_extra_epiphany
from utils import ROMANS
from utils import FERIA


EMBER_DAYS = []

### REFACTORED from temporal_cycle.py

class Temporal:
    def __init__(self, year):
        self.year = year

    global EASTER
    EASTER = easter(self.year)

    def start_year(self):
        """ Circumcision up to Septuagesima, excluding Epiphany """
        cir = day(self.year, 1, 1)
        y = {
                str(cir): "circumci",
                str(cir+days(1)): "8stephen",
                str(cir+days(2)): "8joannis",
                str(cir+days(3)): "8innocen",
                }
        if (
                weekday(cir) == "Sun" 
                or weekday(cir) == "Mon" 
                or weekday(cir) == "Tue"
                ):
            y.update({str(day(self.year, 1, 2)): "snomjesu"})
        else:
            y.update({str(cir-findsunday(cir)+week(1)): "snomjesu"})

        return y

    def gesimas(self):
        """ Septuagesima to Quinquagesima """
        for i, x in enumerate(("septuage", "sexagesi", "quinquag")):
            if x == "septuage":
                global SEPTUAGESIMA
                SEPTUAGESIMA = EASTER - week(9-i)
            y = {
                    str(EASTER - week(9-i)): x,
                    }

            return y

    def epiphany(self, year):
        """ Epiphany and its Sundays """
        epiph = day(year, 1, 6)
        y = {
            str(epiph-days(1)): "vigepiph",
            str(epiph): "epiphani",
            str(epiph+days(7)): "8epiphan",
                }
        if weekday(epiph) == "Sun":
            epiph_1 = epiph+week(1)
        else:
            epiph_1 = epiph-findsunday(epiphany)+week(1)
        # ec = 1
        # TODO: use range and get rid of the roman numerals
        for i, x in enumerate(ROMANS[0:6]):
            if weekday(epiph+days(i+1)) != "Sun":
                if weekday(epiph+days(i+1)) == "Sat":
                    y.update({str(epiph+days(i+1)): "sabin8ep"})
                else:
                    y.update({str(epiph+days(i+1)): "in8epi_"+ROMANS[i+1]})
            else:
                pass

        return y

    def post_epiphany(self):
        """  """
        c,o,y = day(self.year, 1, 6),0,{}
        while c.strftime('%m%d') != SEPTUAGESIMA.strftime('%m%d') and o+1 > 6:
            if ROMANS[o] == 'I':
                if c == day(year, 1, 13):
                    # TODO: add ferias
                    y.update({
                        str(c): "in8epiph",
                        str(c-days(1)): "sfamijmj",
                        })
                else:
                    y.update({
                        str(c): "sfamdomi", # HACK: always first?
                        })
            else:
                y.update({str(c): "dp.epi_"+ROMANS[o]})
                for t in range(6):
                    y.update({str(c+days(t+1)): "de.epi_"+ROMANS[o]})
        o+=1
        c+=week(1)

        return y

    def lent(self):
        y, ashweek = [], ("dcinerum", "f5poscin","f6poscin", "sabbpcin")
        for c, x in enumerate([
            "quadra01", "quadra02", "quadra03",
            "quadra04", "passione", "inpalmis",
            ]):
            if x == "quadra01":
                for day, count in enumerate(ashweek):
                    y.update({str(EASTER-week(6-c)-days(4-0)): day})
            y.update({str(EASTER-week(6-c)): x})
            for j, f in enumerate(FERIA):
                y.update({str(EASTER-week(6-c)+days(j+1)): x+f})
                pass

        return y

    def post_easter(self):
        y, d = [], ("domresur", "in8re", "sabalbis")
        for j, x in enumerate(d):
            if d[x] == 1:
                for i in FERIA[1,-1]:
                    y.update({str(EASTER+days(j)): x+i})
            else:
                y.update({str(EASTER+days(j)): x})

        return y

    def paschaltime(self):
        y = []
        pasch = ("domalbis", "dp.pas_", "dom8asce")
        for i, the_day in enumerate(pasch, start=1):
            if the_day == "dp.pas_":
                for f in ROMANS[1,5]:
                    if f == "II":
                        y.update({
                            str(EASTER+week(i)+days(3)): "solstjos",
                            # TODO: add all the days within the octave
                            str(EASTER+week(i+1)+days(3)): "8solsjos",
                            })
                    elif f == "V":
                        # just for now to avoid the error:
                        # TODO: ROGATION_MONDAY = EASTER+week(i)+days(1)
                        pre_ascen = ("rogati_", "ascensio", "8ascensi")
                        for c, x in enumerate(pre_ascen):
                            if c == 0:
                                for r in range(0,4):
                                    y.update({str(EASTER+week(i)+days(c)): x+str(c)})
                            else:
                                y.update({
                                    str(
                                        EASTER+week(i)+days(4 if x=="ascensio" else 11)
                                        ): x
                                    })
                    else:
                         pass

        return y

