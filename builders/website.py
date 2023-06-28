# import isoweek
class WebCal:
    def __init__(self, year: int, data: dict):
        self.year = year
        self.data = data
        self.weekdays = """\
<div class="row w-100 m-0 rounded-top bg-primary">
<div class="col bg-primary text-white p-1 text-center rounded"> Sunday </div>
<div class="col bg-primary text-white p-1 text-center"> Monday </div>
<div class="col bg-primary text-white p-1 text-center"> Tuesday </div>
<div class="col bg-primary text-white p-1 text-center"> Wednesday </div>
<div class="col bg-primary text-white p-1 text-center"> Thursday </div>
<div class="col bg-primary text-white p-1 text-center"> Friday </div>
<div class="col bg-primary text-white p-1 text-center rounded"> Saturday </div>
</div>"""

    def close_div(self):
        return '</div>'

    def start_row(self, classes=''):
        return f'<div class="row w-100 m-0 {classes}">'

    def start_col(self, classes=''):
        return f'<div class="col col-h p-1 text-break {classes}">'

    def empty_col(self, classes=''):
        return self.start_col(classes)+self.close_div()

    def build_month(self, month, cols, file) -> None:
        file.write('<section>')
        file.write(self.start_row())  # starts the month row
        file.write(f'''
        <div class="mt-3 text-start">
            <h3 class="pt-1">
                {month} {self.year}
            </h3>
        </div>
        ''')
        file.write(self.close_div())  # closes the month row
        file.write(f'{self.weekdays}')
        file.write(self.start_row('border empty_dates'))
        file.write(self.empty_col()*cols)
        return None

    def make_calendar(self) -> list:
        """
        Builds the calendar for the current year and adds the
        feast data to that list.
        """
        # last_week = isoweek.Week.last_week_of_year(self.year).week
        last_week = 53  # or 52...
        cal = []
        for x in range(last_week+1):
            cal.append([])
            for d in range(7):
                cal[x].append([])

        # %U' is the week number with Sunday being the first day of the week
        # %w' is the weekday number with Sunday as the first day of the week

        # Add the data for each day at the beginning
        for date in self.data.keys():
            placement = int(date.strftime('%U'))
            cal[placement][int(date.strftime('%w'))] = [
                self.data[date],
                date.strftime("%B"),
                date.strftime("%d")
            ]
        return cal

    def build(self) -> None:
        cal = self.make_calendar()
        last_week = False

        with open("./output/ordosite/_includes/calendar.html", "w") as f:
            f.truncate(0)

            f.write('<div class="container center p-0">')

            # useful variables
            month_memory = ''

            for j, aweek in enumerate(cal):

                # See if it is the last week of the year
                if last_week is True:
                    break
                elif j+1 == len(cal):
                    last_week = True
                else:
                    pass

                for i, aday in enumerate(aweek):

                    # alternate the cell shading
                    if i % 2 == j % 2:
                        shading = 'bg-body'
                    else:
                        shading = 'bg-light'

                    # see if the day is a calendar day
                    if len(aday) == 2:
                        index = 0  # the day is not a calendar day
                    elif len(aday) == 0:
                        continue
                    else:
                        index = 1

                    # How to treat the beginning of a month
                    if aday[index] != month_memory:  # if new month
                        if j == 1 and i != 0:
                            pass
                        elif j == 1 and i == 0:
                            pass
                        else:
                            if j == 0:
                                f.write('<section>')
                            else:
                                f.write(self.empty_col()*int(7-i))
                                f.write(self.close_div())
                                f.write('</section>')
                        self.build_month(month=aday[index], cols=i, file=f)
                    else:
                        if i == 0 and j != 0:
                            f.write(self.start_row('border empty_dates'))

                    month_memory = aday[index]

                    f.write(self.start_col(
                        f'fw-light d-flex flex-column\
                        justify-content-between {shading}'
                    ))

                    # date-bar
                    f.write(f'<div class="w-100 p-1">\
                    {aday[-1].lstrip("0")}</div>')

                    # feast
                    f.write(f'''
                    <div class="text-center w-100 smaller-text">
                    {'<h1>🧐</h1>' if index != 1 else aday[0]['feast']}
                    </div>
                    ''')

                    # statusbar helpers
                    fish_path = "/assets/images/full_fish.png"
                    color = aday[0]["color"]
                    blank_image = "data:image/gif;base64,R0lGODlhAQABAIAAAP///\
                    wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="
                    fish_placeholder = f'<img src="\
                    {blank_image}\
                    " height="16em" width="16em">'

                    # build the "statusbar"
                    f.write(f'''
<div class="w-100 p-0 d-flex flex-column justify-content-between align-items-center">
{f'<div class="smaller-text">{aday[0]["rank"][1]}</div>'}
<div class="text-end w-100 p-1 d-flex flex-row
justify-content-between align-items-end" height="16em">

{ f'<img src="{blank_image}" height="12em" width="12em" style="border: solid 1px black; border-radius: 50%; background: {color}">'}

{f'<img src="{fish_path}" height="12em">' if aday[0]["fasting"] is True or i == 5 else fish_placeholder}

</div></div>
                    ''')

                    f.write("</div>")  # close the column

                    # add blank days if it is the last day
                    if last_week is True and aday[-1] == str(31):
                        f.write(self.empty_col()*int(6-i))
                        break

                f.write("</div>")  # close the row

            with open("./output/ordosite/_includes/calendar.html") as f:
                lines = list(f)
            with open("./output/ordosite/_includes/calendar.html", "w") as out:
                for line in lines:
                    out.write(line.lstrip())
                f.close()

        return None
