from ordo_tools.helpers import day
from ordo_tools.helpers import days

def build_test_website(year: int, y: dict) -> None:

    # build the calendar with blank days
    cal = []
    for x in range(53):
        cal.append([])
        for d in range(7):
            cal[x].append([])

    # add dates to our year data
    theday = day(year=year, month=1, day=1)
    while theday.strftime("%Y") != str(year+1):
        cal[int(theday.strftime('%U'))-1][int(theday.strftime('%w'))].extend([
            theday.strftime('%B'),
            theday.strftime('%d'),
            ])
        theday += days(1)

    # place the year date into its weekday
    for date in y.keys():
        placement = int(date.strftime('%U'))-1
        cal[placement][int(date.strftime('%w'))].insert(0, y[date])

    # determine the file output and starter text depending on the calendar
    build_dirs = ["./output/ordosite/_includes/calendar.html","./output/html/index.html"]
    for out, path in enumerate(build_dirs):
        with open(path, 'w') as f:
            f.truncate(0)
            if out == 1:
                f.write(""" <!DOCTYPE html> <html lang=""en-us"> <head> <meta name="viewport" content="width=device-width, initial-scale=1"> <meta charset="utf-8"> <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous"> <style>body {background: aliceblue;}</style> <title>test site</title> </head> <body> """)
            f.write(""" <div class="container center p-0"> """)

    # useful variables
            month_memory = ''
            weekdays = """
    <div class="row w-100 m-0 rounded">
    <div class="col bg-primary text-white p-1 text-center rounded-start"> Sunday </div>
    <div class="col bg-primary text-white p-1 text-center"> Monday </div>
    <div class="col bg-primary text-white p-1 text-center"> Tuesday </div>
    <div class="col bg-primary text-white p-1 text-center"> Wednesday </div>
    <div class="col bg-primary text-white p-1 text-center"> Thursday </div>
    <div class="col bg-primary text-white p-1 text-center"> Friday </div>
    <div class="col bg-primary text-white p-1 text-center rounded-end"> Saturday </div>
    </div>
            """
            # TODO: use modals to display more information:
            # https://getbootstrap.com/docs/4.0/components/modal/

            def start_row(classes=''):
                return '<div class="row w-100 m-0 '+classes+'">'

            def start_col(classes=''):
                return '<div class="col p-1 text-break '+classes+'" style="min-height: 10em;">'

            def empty_col(classes=''):
                return start_col(classes)+'</div>'

            for j, aweek in enumerate(cal):
                f.write(start_row())
                for i, aday in enumerate(aweek):

                    # alternate the cell shading
                    if i%2 == j%2:
                        shading = 'bg-body'
                    else:
                        shading = 'bg-light'

                    # see if the day is a calendar day
                    if len(aday) == 2:
                        index = 0
                    elif len(aday) == 0:
                        f.write(empty_col())
                        continue
                    else:
                        index = 1

                    # test to see if we are starting a new month
                    if aday[index] != month_memory:
                        if aday[index] == 'January':
                            pass
                        elif i == 0:
                            pass
                        else:
                            f.write(empty_col()*int(7-i))
                        f.write('</div>'+start_row())
                        f.write(f'<div class="col mt-5 text-center"><h1 class="display-4 pt-3">{aday[index]} {year}</h1></div></div>{weekdays}')
                        f.write(start_row())
                        f.write(empty_col()*i)
                    month_memory = aday[index]
                    f.write(start_col('fw-light d-flex flex-column justify-content-between '+shading))

                    # date-bar
                    f.write(f'<div class="w-100 p-1">{str(aday[-1]).lstrip("0")}</div>')

                    # main content
                    f.write(f'''<div class="text-center w-100">{'<h1>🧐</h1>' if index != 1 else aday[0]['feast']}</div>''')

                    # statusbar helpers
                    if out == 1:
                        fish_path = "assets/images/full_fish.svg"
                    else:
                        fish_path = "/assets/images/full_fish.jpeg"
                    color = aday[0]["color"]
                    blank_image = "data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="
                    fish_placeholder = f'<img src="{blank_image}" height="16em" width="16em">'

                    # build the "statusbar"
                    f.write(f'''
                    <div class="text-end w-100 p-1 d-flex flex-row justify-content-between" height="16em">
                    { f'<img src="{blank_image}" height="16em" width="16em" style="border: solid 1px black; border-radius: 50%; background: {color}">'}
                    { f'<img src="{fish_path}" height="16em">' if aday[0]["fasting"] == True or i == 5 else fish_placeholder }
                    </div>
                    ''')

                    f.write("</div>") # close the column
                f.write("</div>") # close the row
            if out == 1:
                f.write("</div></div></body></html>")
            f.write("</div>")
            f.close()
    return None

