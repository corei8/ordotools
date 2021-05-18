import roman_general_en as generalEn
from datetime import datetime
from datetime import timedelta


def easter(year):
    firstDigit = year // 100
    Remain19 = year % 19
    temp = (firstDigit - 15) // 2 + 202 - 11 * Remain19
    if firstDigit > 26:
        temp = temp - 1
    if firstDigit > 38:
        temp = temp - 1
    if (
        firstDigit == 21
        or firstDigit == 24
        or firstDigit == 25
        or firstDigit == 33
        or firstDigit == 36
        or firstDigit == 37
    ):
        temp = temp - 1
    temp = temp % 30
    tA = temp + 21
    if temp == 29:
        tA = tA - 1
    if temp == 28 and Remain19 > 10:
        tA = tA - 1
    # find the next Sunday
    tB = (tA - 19) % 7
    tC = (40 - firstDigit) % 4
    if tC == 3:
        tC = tC + 1
    if tC > 1:
        tC = tC + 1
    temp = year % 100
    tD = (temp + (temp // 4)) % 7
    tE = ((20 - tB - tC - tD) % 7) + 1
    d = tA + tE
    # return the date
    if d > 31:
        d = d - 31
        m = 4
    else:
        m = 3
    return datetime(year=year, month=m, day=d)


def monthParse(calendar, month):
    #! Needs work
    print('Month: ' + getattr(calendar, month)[0])
    for x in range(1, len(getattr(calendar, month))):
        print(month, x, '\t', getattr(calendar, month)[x][1])
        x += 1


def day(year, month, day):
    x = datetime(year=year, month=month, day=day)
    return x


def week(i):
    x = timedelta(weeks=i)
    return x


def indays(numdays):
    x = timedelta(days=numdays)
    return x


def weekday(date):
    return date.strftime('%a')


def findsunday(date):
    if date.strftime('%a') == 'Mon':
        x = 0
    if date.strftime('%a') == 'Tue':
        x = 1
    if date.strftime('%a') == 'Wed':
        x = 2
    if date.strftime('%a') == 'Thu':
        x = 3
    if date.strftime('%a') == 'Fri':
        x = 4
    if date.strftime('%a') == 'Sat':
        x = 5
    if date.strftime('%a') == 'Sun':
        pass
    return timedelta(days=x)


def temporal(year):
    year_prev, year = int(year) - 1, int(year)
    cycle = []
    # Christmas
    xmas = day(year_prev, 12, 25)
    # cycle.insert(0, ["In Nativitate Domini", "d1", weekday(day(year_prev, 12, 25)), day(year_prev, 12, 25)])
    # cycle.insert(0, ["In Vigilia Nativitatis Domini", "d1", weekday(day(year_prev, 12, 24)), day(year_prev, 12, 24)])
    # Sundays of Advent
    #! Adjust this for the real year_prev.
    advents = [["Dominica IV Adventus", "sd2"],
               ["Dominica III Adventus", "sd2"],
               ["Dominica II Adventus", "sd2"],
               ["Dominica I Adventus", "sd2"]
               ]
    xmas_diff = findsunday(xmas)
    # i = 0
    # for sunday in advents:
    #    event = [
    #        weekday(day(year_prev, 12, 24) - xmas_diff - week(i)),
    #        day(year_prev, 12, 24) - xmas_diff - week(i)
    #    ]
    #    sunday.extend(event)
    #    i += 1
    #    cycle.insert(0, sunday)
    # Dominica Infra Octavam Nativitatis
    # Remember that this is replaced if it falls on the octave.
    # cycle.append([
    #    "Dominica Infra Octavam Nativitatis",
    #    "sd",
    #    weekday(day(year_prev, 12, 24) + (week(1)-xmas_diff)),
    #    day(year_prev, 12, 24) + (week(1)-xmas_diff)
    # ])
    dinfraxmas = weekday(day(year_prev, 12, 24) + (week(1)-xmas_diff))
    # find Septuagesima
    gesimas = [
        "Spetuagesima",
        "Sexagesima",
        "Quinquagesima"
    ]
    quads = [
        "I in Quadragesima",
        "II in Quadragesima",
        "III in Quadragesima",
        "IV in Quadragesima",
        "de Passione",
        "in Palmis"
    ]
    i = 1
    for x in gesimas:
        cycle.append([
            "Dominica in " + x,
            "sd2",
            weekday(easter(year) - week(9*i)),
            easter(year) - week(9*i)
        ])
        i += 1
    for x in quads:
        cycle.append([
            "Dominica " + x,
            "sd1",
            weekday(easter(year) - week(9*i)),
            easter(year) - week(9*i)
        ])
        i += 1
    cycle.append([
        "Dominica Dominica Resurrectionis",
        "d1",
        weekday(easter(year)),
        easter(year)
    ])
    ########################
    ### DISPLAY THE LIST ###
    ########################
    print("\n")
    # print(cycle)
    col_width = max(len(str(word))
                    for row in cycle for word in row) + 2  # padding
    for row in cycle:
        print("".join(str(word).ljust(col_width) for word in row))


def app():
    user = ''
    while user != 'exit':
        user = input('\nEnter "exit" to quit\nEnter 4-digit year: ')
        if user == "exit":
            break
        else:
            try:
                temporal(user)
            except ValueError:
                pass


app()
