import roman_general_en as generalEn
import sys
from datetime import datetime
from datetime import timedelta

# TODO: find the letter of the Martyrology


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
    print("Month: " + getattr(calendar, month)[0])
    for x in range(1, len(getattr(calendar, month))):
        print(month, x, "\t", getattr(calendar, month)[x][1])
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
    return date.strftime("%a")


def findsunday(date):
    if date.strftime("%a") == "Mon":
        x = 1
    if date.strftime("%a") == "Tue":
        x = 2
    if date.strftime("%a") == "Wed":
        x = 3
    if date.strftime("%a") == "Thu":
        x = 4
    if date.strftime("%a") == "Fri":
        x = 5
    if date.strftime("%a") == "Sat":
        x = 6
    if date.strftime("%a") == "Sun":
        pass
    return timedelta(days=x)


# TODO: schedule all the octaves


# TODO: add the ember days


def temporal(year):
    year_prev, year = int(year) - 1, int(year)
    this_year = year
    cycle = []
    # HOLY NAME - sunday between 01-01 and 01-06 else 01-02
    circumcision = day(this_year, 1, 1)
    if (
        weekday(circumcision) == "Sun"
        or weekday(circumcision) == "Mon"
        or weekday(circumcision) == "Tue"
    ):
        cycle.append(
            [
                "SS Nominis Jesu",
                "d2",
                weekday(day(this_year, 1, 2)),
                day(this_year, 1, 2),
            ]
        )
    else:
        sunday_post_cir_pre_ep = circumcision - findsunday(circumcision) + week(1)
        cycle.append(
            [
                "SS Nominis Jesu",
                "d2",
                weekday(sunday_post_cir_pre_ep),
                sunday_post_cir_pre_ep,
            ]
        )
    # GESIMAS
    gesimas = ["Septuagesima", "Sexagesima", "Quinquagesima"]
    i = 1
    for x in gesimas:
        if x == "Septuagesima":
            septuadate = easter(year) - week(10 - i)
        cycle.append(
            [
                "Dominica in " + x,
                "sd2",
                weekday(easter(year) - week(10 - i)),
                easter(year) - week(10 - i),
            ]
        )
        i += 1
    # EPIPHANY
    epiphany = day(this_year, 1, 6)
    epiph_sundays = ["I", "II", "III", "IV", "V", "VI"]
    if weekday(epiphany) == "Sun":
        cycle.append(
            [
                "Epiphania Domini",
                "d1",
                weekday(epiphany),
                epiphany,
            ]
        )
        first_epiph = epiphany + week(1)
    else:
        first_epiph = epiphany - findsunday(epiphany) + week(1)

    epiph_counter, o = first_epiph, 0
    while epiph_counter != septuadate:
        if epiph_sundays[o] == "I":
            if epiph_counter == day(this_year, 1, 13):
                cycle.append(
                    [
                        "Octava Epiphaniæ; Dominica "
                        + epiph_sundays[o]
                        + " post Epiphaniam",
                        "dm",
                        weekday(epiph_counter),
                        epiph_counter,
                    ]
                )
                cycle.append(
                    [
                        "S Familiæ Jesu Mariæ et Joseph",
                        "dm",
                        weekday(epiph_counter - indays(1)),
                        epiph_counter - indays(1),
                    ]
                )
            else:
                cycle.append(
                    [
                        "S Familiæ Jesu Mariæ et Joseph; Dominica "
                        + epiph_sundays[o]
                        + " post Epiphaniam",
                        "dm",
                        weekday(epiph_counter),
                        epiph_counter,
                    ]
                )
        else:
            cycle.append(
                [
                    "Dominica " + epiph_sundays[o] + " post Epiphaniam",
                    "sp",
                    weekday(epiph_counter),
                    epiph_counter,
                ]
            )
        o += 1
        epiph_counter += week(1)
    # LENT
    quads = [
        "I in Quadragesima",
        "II in Quadragesima",
        "III in Quadragesima",
        "IV in Quadragesima",
        "de Passione",
        "in Palmis",
    ]
    feria = [
        "Feria II",
        "Feria III",
        "Feria IV",
        "Feria V",
        "Feria VI",
        "Sabbatum",
    ]
    for x in quads:
        if x == "I in Quadragesima":
            cycle.append(
                [
                    "Dies Cinerum",
                    "sp",
                    weekday(easter(year) - week(10 - i) - indays(4)),
                    easter(year) - week(10 - i) - indays(4),
                ]
            )
            cycle.append(
                [
                    "Feria V post Diem Cinerum",
                    "sp",
                    weekday(easter(year) - week(10 - i) - indays(3)),
                    easter(year) - week(10 - i) - indays(4),
                ]
            )
            cycle.append(
                [
                    "Feria VI post Diem Cinerum",
                    "sp",
                    weekday(easter(year) - week(10 - i) - indays(2)),
                    easter(year) - week(10 - i) - indays(4),
                ]
            )
            cycle.append(
                [
                    "Sabbatum post Diem Cinerum",
                    "sp",
                    weekday(easter(year) - week(10 - i) - indays(1)),
                    easter(year) - week(10 - i) - indays(4),
                ]
            )
        cycle.append(
            [
                "Dominica " + x,
                "sd1",
                weekday(easter(year) - week(10 - i)),
                easter(year) - week(10 - i),
            ]
        )
        j = 1
        for y in feria:
            if x == "de Passione" and y == "Feria VI":
                cycle.append(
                    [
                        "Septem Dolorum BMV",
                        "dm",
                        weekday(easter(year) - week(10 - i) + indays(j)),
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Feria IV":
                cycle.append(
                    [
                        "Feria IV Quattuor Temporum Quadragesimæ",
                        "sp",
                        weekday(easter(year) - week(10 - i) + indays(j)),
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Feria VI":
                cycle.append(
                    [
                        "Feria VI Quattuor Temporum Quadragesimæ",
                        "sp",
                        weekday(easter(year) - week(10 - i) + indays(j)),
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Sabbatum":
                cycle.append(
                    [
                        "Sabbato Quattuor Temporum Quadragesimæ",
                        "sp",
                        weekday(easter(year) - week(10 - i) + indays(j)),
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "in Palmis" and y == "Feria V":
                cycle.append(
                    [
                        y + " in Cœna Domini",
                        "d1",
                        weekday(easter(year) - week(10 - i) + indays(j)),
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "in Palmis" and y == "Feria VI":
                cycle.append(
                    [
                        y + " in Parasceve",
                        "d1",
                        weekday(easter(year) - week(10 - i) + indays(j)),
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "in Palmis" and y == "Sabbatum":
                cycle.append(
                    [
                        "Sabbatum Sanctum",
                        "d1",
                        weekday(easter(year) - week(10 - i) + indays(j)),
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "in Palmis":
                cycle.append(
                    [
                        y + " Majoris Hebd; Feria Priv",
                        "sp",
                        weekday(easter(year) - week(10 - i) + indays(j)),
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            else:
                cycle.append(
                    [
                        y + " infra Hebd " + x,
                        "sp",
                        weekday(easter(year) - week(10 - i) + indays(j)),
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            j += 1
        i += 1
    cycle.append(["Dominica Resurrectionis", "d1", weekday(easter(year)), easter(year)])
    # PASCHAL TIME
    post_pent = [
        "Dominica in Albis",
        "Dominica II post Pascha",
        "Dominica III post Pascha",
        "Dominica IV post Pascha",
        "Dominica V post Pascha",
        "Dominica infra Octavam Ascensionis",
    ]
    i = 1
    for x in post_pent:
        cycle.append([x, "sd", weekday(easter(year) + week(i)), easter(year) + week(i)])
        i += 1
    cycle.append(
        [
            "Dominica Pentecostes",
            "d1",
            weekday(easter(year) + week(i)),
            easter(year) + week(i),
        ]
    )
    cycle.append(
        [
            "Feria IV Quattuor infra Temporum Pentecostes",
            "d1",
            weekday(easter(year) + week(i) + indays(3)),
            easter(year) + week(i) + indays(3),
        ]
    )
    cycle.append(
        [
            "Feria VI Quattuor infra Temporum Pentecostes",
            "d1",
            weekday(easter(year) + week(i) + indays(5)),
            easter(year) + week(i) + indays(5),
        ]
    )
    cycle.append(
        [
            "Sabbato Quattuor infra Temporum Pentecostes",
            "d1",
            weekday(easter(year) + week(i) + indays(6)),
            easter(year) + week(i) + indays(6),
        ]
    )
    i += 1  ## is this counter necessary?
    # SUNDAYS AFTER PENTECOST
    prelim_pents = [
        ["Dominica Sanctissimæ Trinitatis", "d1"],
        ["Dominica II post Pentecosten infra Octavam Corporis Christi", "sd"],
        ["Dominica III post Pentecosten infra Octavam SSmi Cordis DNJC", "sd"],
    ]
    for x in prelim_pents:
        if x[0] == "Dominica II post Pentecosten infra Octavam Corporis Christi":
            cycle.append(
                [
                    "Sanctissimi Corporis Christi",
                    "d1",
                    weekday(easter(year) + week(i) - indays(3)),
                    easter(year) + week(i) - indays(3),
                ]
            )
        if x[0] == "Dominica III post Pentecosten infra Octavam SSmi Cordis DNJC":
            cycle.append(
                [
                    "Sacratissimi Cordis Jesu",
                    "d1",
                    weekday(easter(year) + week(i) - indays(2)),
                    easter(year) + week(i) - indays(2),
                ]
            )
        cycle.append(
            [x[0], x[1], weekday(easter(year) + week(i)), easter(year) + week(i)]
        )
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
        "XXVIII",
    ]
    sept_counter = 0
    for x in pent_romans:
        earliest_first_advent = str(year) + "-12-03"
        if easter(year) + week(i) >= datetime.strptime(
            earliest_first_advent, "%Y-%m-%d"
        ):
            break
        else:
            cycle.append(
                [
                    "Dominica " + x + " post Pentecosten",
                    "sd",
                    weekday(easter(year) + week(i)),
                    easter(year) + week(i),
                ]
            )
            if (easter(year) + week(i)).strftime("%B") == "September":
                sept_counter += 1
            #! If the first sunday of september is the first, then sept_counter == 3 is true
            #! the wednesday cannot fall on or before the 14th of september.
            #! this will be correct for many but not all cases!!:
            if sept_counter == 2:
                cycle.append(
                    [
                        "Feria IV Quattuor Temporum Septembris",
                        "sd",
                        weekday(easter(year) + week(i) + indays(3)),
                        easter(year) + week(i) + indays(3),
                    ]
                )
                cycle.append(
                    [
                        "Feria VI Quattuor Temporum Septembris",
                        "sd",
                        weekday(easter(year) + week(i) + indays(5)),
                        easter(year) + week(i) + indays(5),
                    ]
                )
                cycle.append(
                    [
                        "Sabbato Quattuor Temporum Septembris",
                        "sd",
                        weekday(easter(year) + week(i) + indays(6)),
                        easter(year) + week(i) + indays(6),
                    ]
                )
            i += 1
    # ADVENT
    christmas = datetime.strptime(str(year) + "-12-25", "%Y-%m-%d")
    lastadvent = christmas - findsunday(christmas)
    advents = [
        "Dominica IV Adventus",
        "Dominica III Adventus",
        "Dominica II Adventus",
        "Dominica I Adventus",
    ]
    i = 0
    for x in advents:
        if x == "Dominica III Adventus":
            cycle.append(
                [x, "sd2", weekday(lastadvent - week(i)), lastadvent - week(i)]
            )
            cycle.append(
                [
                    "Feria IV Quattuor Temporum in Adventu",
                    "sp",
                    weekday(lastadvent - week(i) + indays(3)),
                    lastadvent - week(i) + indays(3),
                ]
            )
            cycle.append(
                [
                    "Feria VI Quattuor Temporum in Adventu",
                    "sp",
                    weekday(lastadvent - week(i) + indays(5)),
                    lastadvent - week(i) + indays(5),
                ]
            )
            cycle.append(
                [
                    "Sabbato Quattuor Temporum in Adventu",
                    "sp",
                    weekday(lastadvent - week(i) + indays(6)),
                    lastadvent - week(i) + indays(6),
                ]
            )
        else:
            cycle.append(
                [x, "sd2", weekday(lastadvent - week(i)), lastadvent - week(i)]
            )
        i += 1
    # CHRISTMAS
    if weekday(christmas) == "Sun":
        cycle.append(["In Nativitate Domini", "d1", weekday(christmas), christmas])
    else:
        cycle.append(
            [
                "Dominica Infra Octavam Nativitatis",
                "sd",
                weekday(christmas + indays(7) - findsunday(christmas)),
                christmas + indays(7) - findsunday(christmas),
            ]
        )

    ########################
    ### DISPLAY THE LIST ###
    ########################

    print("\n")
    # print to terminal
    for row in cycle:
        print(row[0] + "\t" + row[1] + "\t" + str(row[2]) + "\t" + str(row[3]))
    # print to csv file
    original_stdout = sys.stdout
    with open("romancal.csv", "w") as f:
        sys.stdout = f
        print("Feast" + ", " + "Rank" + ", " + "Weekday" + ", " + "Date")
        for row in cycle:
            print(row[0] + ", " + row[1] + ", " + str(row[2]) + ", " + str(row[3]))
        sys.stdout = original_stdout


def app():
    user = ""
    while user != "exit":
        user = input('\nEnter "exit" to quit\nEnter 4-digit year: ')
        if user == "exit":
            break
        else:
            try:
                temporal(user)
            except ValueError:
                pass


app()
