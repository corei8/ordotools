import roman_general_en as generalEn
from datetime import datetime
from datetime import timedelta

# TODO: use datime to diplay Easter in an easier format


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
    print(year, m, d)


def monthParse(calendar, month):
    print('Month: ' + getattr(calendar, month)[0])
    for x in range(1, len(getattr(calendar, month))):
        # display only the feasts for now.
        print(month, x, '\t', getattr(calendar, month)[x][1])
        x += 1


def day(year, month, day):
    x = datetime(year=year, month=month, day=day)
    return x


def indays(numdays):
    x = timedelta(days=numdays)
    return x


def weekday(date):
    return date.strftime('%a')


def findsunday(date):
    if date.strftime('%a') == 'Mon':
        x = 1
    if date.strftime('%a') == 'Tue':
        x = 2
    if date.strftime('%a') == 'Wed':
        x = 3
    if date.strftime('%a') == 'Thu':
        x = 4
    if date.strftime('%a') == 'Fri':
        x = 5
    if date.strftime('%a') == 'Sat':
        x = 6
    if date.strftime('%a') == 'Sun':
        pass
    return timedelta(days=x)


def temporal(year):
    year = int(year)
    cycle = []
    # Christmas
    xmas = day(year, 12, 25)
    cycle.insert(0, ["In Nativitate Domini", "d1", weekday(
        day(year, 12, 25)), day(year, 12, 25)])
    cycle.insert(0, ["In Vigilia Nativitatis Domini", "d1", weekday(
        day(year, 12, 24)), day(year, 12, 24)])
    # Sundays of Advent
    advents = [["Dominica I Adventus", "sd2"],
               ["Dominica II Adventus", "sd2"],
               ["Dominica III Adventus", "sd2"],
               ["Dominica IV Adventus", "sd2"]
               ]
    xmas_diff = findsunday(xmas)
    i = 1
    for sunday in advents:
        event = [
            weekday(day(year, 12, 24) - xmas_diff - timedelta(days=7*i)),
            day(year, 12, 24) - xmas_diff - timedelta(days=7*i)
        ]
        sunday.extend(event)
        i += 1
        cycle.insert(0, sunday)
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
