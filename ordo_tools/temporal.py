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
    This class will enable us to explore parts of the liturgical year, rather
    than having to calulate the entire year. The exact implementation process
    is still being worked out, but this Class will be much easier to debug and
    develop rather than the previous idea, which is in temporal_cycle.py.
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
        if weekday(epiph) == "Sun": # BUG: never implemented?
            epiph_1 = epiph+week(1)
        else:
            epiph_1 = epiph-findsunday(epiph)+week(1)
        # TODO: use range and get rid of the roman numerals
        #       use the standard format for better debugging
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
                # 'vig_chris',
                'christmas',
                'ststephan',
                'stjoannis',
                'stsinnoce',
                'stthomaem',
                'stsilvest',
                ]
        # BUG: this is not working for 2023
        if findsunday(christmas) == 0 or 1 or 2 or 3:
            # Sunday w/in the octave occurs on 30 if the Sunday is on 25-28
            y.update({christmas + days(5) - findsunday(christmas): 'rdom8chr'}) # reposita
        else:
            # Sunday falls on the 29-31
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
            # TODO: Sunday within the Octave of the Nativity
            #       this is going to be a bit complicated...
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



def build_test_website(year):
    y = Temporal(year).build_entire_year()
    cal = []
    # TODO: make the calendar custom
    # TODO: make the month and weekday headers sticky
    for x in range(53):
        cal.append([])
        for d in range(7):
            cal[x].append([])
    theday = day(year=year, month=1, day=1)
    while theday.strftime("%Y") != str(year+1):
        cal[int(theday.strftime('%U'))-1][int(theday.strftime('%w'))].extend([
            # '',
            theday.strftime('%B'),
            theday.strftime('%d'),
            ])
        theday += days(1)
    for date in y.keys():
        place = int(date.strftime('%U'))-1
        cal[place][int(date.strftime('%w'))].insert(0, y[date])
    with open("../output/html/index.html", 'w') as f:
        f.truncate(0)
        f.write("""
                <!doctype html>
                <html lang="en">
                <head>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
                integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
                <style>
                </style>
                </head>
                <body>
                <header class="text-bg-secondary pt-2 pb-2 p-3">
                A simple demonstration of an ordo-generating program 
                for the traditional calendar.
                </header>
                <div class="container">
                <h1 class="display-1 text-center">
                The Ordo
                </h1>
                <div class="alert alert-warning" role="alert">
                This website and the algorithms that generate the calendars 
                are very much <em>works in progress.</em> Do not use this website as you
                would an official ordo.
                </div>
                </div>
                <div class="container center">
                """)
        month_memory = ''
        weekdays = """
        <div class="row w-100 rounded">
        <div class="col bg-body-secondary p-1 text-center rounded-start"> Sunday </div>
        <div class="col bg-body-secondary p-1 text-center"> Monday </div>
        <div class="col bg-body-secondary p-1 text-center"> Tuesday </div>
        <div class="col bg-body-secondary p-1 text-center"> Wednesday </div>
        <div class="col bg-body-secondary p-1 text-center"> Thursday </div>
        <div class="col bg-body-secondary p-1 text-center"> Friday </div>
        <div class="col bg-body-secondary p-1 text-center rounded-end"> Saturday </div>
        </div>
        """
        # TODO: use modals to display more information:
        # https://getbootstrap.com/docs/4.0/components/modal/

        def start_row(classes=''):
            return '<div class="row w-100 '+classes+'">'

        def start_col(classes=''):
            return '<div class="col p-1 '+classes+'" style="min-height: 10em;">'

        def empty_col(classes=''):
            return start_col(classes)+'</div>'

        for j, aweek in enumerate(cal):
            f.write(start_row())
            for i, aday in enumerate(aweek):
                if i%2 == j%2:
                    shading = 'bg-white'
                else:
                    shading = 'bg-light-subtle'
                if len(aday) == 2:
                    if aday[0] != month_memory:
                        if aday[0] == 'January':
                            pass
                        elif i == 0:
                            pass
                        else:
                            f.write(empty_col()*int(7-i))
                        f.write('</div>'+start_row())
                        f.write('<div class="col p1 text-center">'\
                                +'<h1 class="display-4 pt-3">'\
                                +aday[0]+" "+str(year)+'</h1></div></div>'+weekdays)
                        f.write(start_row())
                        f.write(empty_col()*i)
                    month_memory = aday[0]
                    f.write(start_col('fw-light '+shading))
                    f.write(str(aday[1]).lstrip('0'))
                    f.write('</br></br><div class="text-small">¯\_(ツ)_/¯</div></div>')
                elif len(aday) == 0:
                    f.write(empty_col())
                else:
                    if aday[1] != month_memory:
                        if aday[1] == 'January':
                            pass
                        elif i == 0:
                            pass
                        else:
                            f.write(empty_col()*int(7-i))
                        f.write('</div>'+start_row())
                        f.write('<div class="col p1 text-center">'\
                                +'<h1 class="display-4 pt-3">'\
                                +aday[1]+" "+str(year)+'</h1></div></div>'+weekdays)
                        f.write(start_row())
                        f.write(empty_col()*i)
                    month_memory = aday[1]
                    f.write(start_col('fw-light '+shading))
                    f.write(str(aday[-1]).lstrip('0'))
                    f.write('</br></br>')
                    f.write('<div class="fs-6">'+str(aday[0])+'</div>')
                    f.write('</div>')
            f.write('</div>')
        f.write("""
                </div>
                <footer class="mt-5 text-light bg-dark pt-2 pb-2 p-3">
                Contact the developer at corei8.github@gmail.com for any questions,
                or if you wish to contribute.
                </footer>
                </body>
                </html>
                """)

build_test_website(2023)
