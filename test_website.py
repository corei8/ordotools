from ordo_tools.temporal import Temporal
from ordo_tools.utils import day
from ordo_tools.utils import days

def build_test_website(year):
    y = Temporal(year).build_entire_year()
    cal = []
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
    with open("./output/html/calendar.html", 'w') as f:
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
            return '<div class="col p-1 text-break '+classes+'" style="min-height: 10em;">'

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
