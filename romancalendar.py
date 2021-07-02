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
    ## ADVENT, CHRISTMAS, EPIPHANY
    dinfraxmas = weekday(day(year_prev, 12, 24) + (week(1)-xmas_diff))
    ## LENT, EASTER
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
            weekday(easter(year) - week(10-i)),
            easter(year) - week(10-i)
        ])
        i += 1
    for x in quads:
        cycle.append([
            "Dominica " + x,
            "sd1",
            weekday(easter(year) - week(10-i)),
            easter(year) - week(10-i)
        ])
        i += 1
    cycle.append([
        "Dominica Dominica Resurrectionis",
        "d1",
        weekday(easter(year)),
        easter(year)
    ])

    # PASCHAL TIME
    post_pent = [
        "Dominica in Albis",
        "Dominica II post Pascha",
        "Dominica III post Pascha",
        "Dominica IV post Pascha",
        "Dominica V post Pascha",
        "Dominica infra Octavam Ascensionis"
    ]
    i = 1
    for x in post_pent:
        cycle.append([
            x,
            "sd",
            weekday(easter(year) + week(i)),
            easter(year) + week(i)
        ])
        i += 1
    cycle.append([
        "Dominica Pentecostes",
        "d1",
        weekday(easter(year) + week(i)),
        easter(year) + week(i)
    ])
    i += 1
    # SUNDAYS AFTER PENTECOST
    prelim_pents = [
        ["Dominica Sanctissimæ Trinitatis", "d1"],
        ["Dominica II post Pentecosten infra Octavam Corporis Christi", "sd"],
        ["Dominica III Post Pentecosten infra Octavam SSmi Cordis DNJC", "sd"]
    ]
    for x in prelim_pents:
        cycle.append([
            x[0],
            x[1],
            weekday(easter(year) + week(i)),
            easter(year) + week(i)
        ])
        i += 1
    pent_romans = [
        "IV",
        "V",
        "VI",
        "VII",
        "VIII",
        "IX",
        "X",
        "XI",
        "XII",
        "XIII",
        "XIV",
        "XV",
        "XVI",
        "XVII",
        "XVIII",
        "XIX",
        "XX",
        "XXI",
        "XXII",
        "XXIII",
        "XXIV",
        "XXV",
        "XXVI",
        "XXVII",
        "XXVIII"
    ]
    for x in pent_romans:
        earliest_first_advent = str(year) + "-12-03"
        if easter(year) + week(i) >= datetime.strptime(earliest_first_advent, "%Y-%m-%d"):
            break
        else:
            cycle.append([
                x,
                "sd",
                weekday(easter(year) + week(i)),
                easter(year) + week(i)
            ])
            i += 1
    # ADVENT
    # christmas
    # last sunday of advent
    # first sunday of advent

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
