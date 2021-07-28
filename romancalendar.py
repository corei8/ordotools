import sys
from datetime import datetime
from datetime import timedelta
import stitch

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


romans = [
    "I",
    "II",
    "III",
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
        x = 0
    return timedelta(days=x)


def temporal(year):
    year_prev, year = int(year) - 1, int(year)
    this_year = year
    cycle = []
    feria = [
        "Feria II",
        "Feria III",
        "Feria IV",
        "Feria V",
        "Feria VI",
        "Sabbato",
    ]
    circumcision = day(this_year, 1, 1)
    cycle.extend(
        [
            [
                "Circumcisio Domini et Oct Nativitatis",
                "d2",
                circumcision,
            ],
            [
                "Octava S Stephani Protomartyris",
                "sp",
                circumcision + indays(1),
            ],
            [
                "Octava S Joannis Ap & Ev",
                "sp",
                circumcision + indays(2),
            ],
            [
                "Octava Ss Innocentium Mm",
                "sp",
                circumcision + indays(3),
            ],
        ]
    )
    if (
        weekday(circumcision) == "Sun"
        or weekday(circumcision) == "Mon"
        or weekday(circumcision) == "Tue"
    ):
        cycle.append(
            [
                "SS Nominis Jesu",
                "d2",
                day(this_year, 1, 2),
            ]
        )
    else:
        sunday_post_cir_pre_ep = circumcision - findsunday(circumcision) + week(1)
        cycle.append(
            [
                "SS Nominis Jesu",
                "d2",
                sunday_post_cir_pre_ep,
            ]
        )
    # 'GESIMAS'
    gesimas = ["Septuagesima", "Sexagesima", "Quinquagesima"]
    i = 1
    for x in gesimas:
        if x == "Septuagesima":
            septuadate = easter(year) - week(10 - i)
        cycle.append(
            [
                "Dominica in " + x,
                "sd2",
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
                epiphany,
            ],
        )
        first_epiph = epiphany + week(1)
    else:
        first_epiph = epiphany - findsunday(epiphany) + week(1)
    epiph_oct_days = ["II", "III", "IV", "V", "VI", "VII"]
    ep_oct_days_counter = 1
    for x in epiph_oct_days:
        if weekday(epiphany + indays(ep_oct_days_counter)) != "Sun":
            cycle.append(
                [
                    "De die "
                    + epiph_oct_days[ep_oct_days_counter - 1]
                    + " infra Oct Epiphaniæ",
                    "sd",
                    epiphany + indays(ep_oct_days_counter),
                ],
            )
        else:
            pass
        ep_oct_days_counter += 1
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
                        epiph_counter,
                    ]
                )
                cycle.append(
                    [
                        "S Familiæ Jesu Mariæ et Joseph",
                        "dm",
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
                        epiph_counter,
                    ]
                )
        else:
            cycle.append(
                [
                    "Dominica " + epiph_sundays[o] + " post Epiphaniam",
                    "sp",
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
    for x in quads:
        if x == "I in Quadragesima":
            cycle.append(
                [
                    "Dies Cinerum",
                    "sp",
                    easter(year) - week(10 - i) - indays(4),
                ]
            )
            cycle.append(
                [
                    "Feria V post Diem Cinerum",
                    "sp",
                    easter(year) - week(10 - i) - indays(4),
                ]
            )
            cycle.append(
                [
                    "Feria VI post Diem Cinerum",
                    "sp",
                    easter(year) - week(10 - i) - indays(4),
                ]
            )
            cycle.append(
                [
                    "Sabbato post Diem Cinerum",
                    "sp",
                    easter(year) - week(10 - i) - indays(4),
                ]
            )
        cycle.append(
            [
                "Dominica " + x,
                "sd1",
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
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Feria IV":
                cycle.append(
                    [
                        "Feria IV Quattuor Temporum Quadragesimæ",
                        "sp",
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Feria VI":
                cycle.append(
                    [
                        "Feria VI Quattuor Temporum Quadragesimæ",
                        "sp",
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Sabbato":
                cycle.append(
                    [
                        "Sabbato Quattuor Temporum Quadragesimæ",
                        "sp",
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "in Palmis" and y == "Feria V":
                cycle.append(
                    [
                        y + " in Cœna Domini",
                        "d1",
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "in Palmis" and y == "Feria VI":
                cycle.append(
                    [
                        y + " in Parasceve",
                        "d1",
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "in Palmis" and y == "Sabbato":
                cycle.append(
                    [
                        "Sabbatum Sanctum",
                        "d1",
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "in Palmis":
                cycle.append(
                    [
                        y + " Majoris Hebd; Feria Priv",
                        "sp",
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            else:
                cycle.append(
                    [
                        y + " infra Hebd " + x,
                        "sp",
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            j += 1
        i += 1
    cycle.append(["Dominica Resurrectionis", "d1", easter(year)])
    cycle.extend(
        [
            [
                "Feria II Paschatis",
                "d1",
                easter(year) + indays(1),
            ],
            [
                "Feria III Paschatis",
                "d1",
                easter(year) + indays(2),
            ],
            [
                "De die IV infra Oct Paschæ",
                "sd",
                easter(year) + indays(3),
            ],
            [
                "De die V infra Oct Paschæ",
                "sd",
                easter(year) + indays(4),
            ],
            [
                "De die VI infra Oct Paschæ",
                "sd",
                easter(year) + indays(5),
            ],
            [
                "Sabbatum in Albis",
                "sd",
                easter(year) + indays(6),
            ],
        ]
    )
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
        if x == "Dominica II post Pascha":
            cycle.extend(
                [
                    [
                        "Solemnitas S Joseph, Sponsi BMV C et Ecclesiæ Universalis Patroni",
                        "d1",
                        easter(year) + week(i) + indays(3),
                    ],
                    [
                        "Octava Solemnitas S Joseph",
                        "dm",
                        easter(year) + week(i + 1) + indays(3),
                    ],
                ]
            )
        if x == "Dominica V post Pascha":
            cycle.extend(
                [
                    [
                        "Litaniæ Minores",
                        "sp",
                        easter(year) + week(i) + indays(1),
                    ],
                    [
                        "Litaniæ Minores",
                        "sp",
                        easter(year) + week(i) + indays(2),
                    ],
                    [
                        "Litaniæ Minores",
                        "sp",
                        easter(year) + week(i) + indays(3),
                    ],
                    [
                        "Vigilæ Ascensionis",
                        "sp",
                        easter(year) + week(i) + indays(3),
                    ],
                    [
                        "Ascensio DNJC",
                        "d1",
                        easter(year) + week(i) + indays(4),
                    ],
                ]
            )
            ascension_day = easter(year) + week(i) + indays(5)
        if x == "Dominica infra Octavam Ascensionis":
            j = 0
            for y in romans[1:6]:
                if (ascension_day + indays(j + 1)) == (easter(year) + week(i)):
                    pass
                else:
                    cycle.append(
                        [
                            "De " + y + " die infra Oct Ascensionis",
                            "sd",
                            ascension_day + indays(j + 1),
                        ]
                    )
                j += 1
        cycle.append([x, "sd", easter(year) + week(i)])
        i += 1
    cycle.extend(
        [
            [
                "Vigilia Pentecostes",
                "sd",
                easter(year) + week(i) - indays(1),
            ],
            [
                "Dominica Pentecostes",
                "d1",
                easter(year) + week(i),
            ],
        ]
    )
    # add the octave of Pentecost
    j = 0
    for y in romans[1:6]:
        if y == "II" or y == "III":
            cycle.append(
                [
                    "De " + y + " die infra Oct Pentecostes",
                    "d1",
                    ascension_day + indays(j + 1),
                ]
            )
        else:
            cycle.append(
                [
                    "De " + y + " die infra Oct Pentecostes",
                    "d1",
                    ascension_day + indays(j + 1),
                ]
            )
        j += 1
    cycle.append(
        [
            "Sabbato die infra Oct Pentecostes",
            "d1",
            ascension_day + indays(j + 1),
        ]
    )
    cycle.append(
        [
            "Feria IV Quattuor infra Temporum Pentecostes",
            "d1",
            easter(year) + week(i) + indays(3),
        ]
    )
    cycle.append(
        [
            "Feria VI Quattuor infra Temporum Pentecostes",
            "d1",
            easter(year) + week(i) + indays(5),
        ]
    )
    cycle.append(
        [
            "Sabbato Quattuor infra Temporum Pentecostes",
            "d1",
            easter(year) + week(i) + indays(6),
        ]
    )
    i += 1
    # SUNDAYS AFTER PENTECOST
    prelim_pents = [
        ["Dominica Sanctissimæ Trinitatis", "d1"],
        ["Dominica II post Pentecosten infra Octavam Corporis Christi", "sd"],
        ["Dominica III post Pentecosten infra Octavam SSmi Cordis DNJC", "sd"],
    ]
    for x in prelim_pents:
        if x[0] == "Dominica II post Pentecosten infra Octavam Corporis Christi":
            corpus_christi = easter(year) + week(i) - indays(3)
            j = 0
            for y in romans[1:7]:
                if (corpus_christi + indays(j + 1)) == (easter(year) + week(i)):
                    pass
                else:
                    cycle.append(
                        [
                            "De " + y + " die infra Oct Corporis Christi",
                            "sd",
                            corpus_christi + indays(j + 1),
                        ]
                    )
                j += 1
            cycle.append(
                [
                    "Sanctissimi Corporis Christi",
                    "d1",
                    corpus_christi,
                ]
            )
            cycle.append(
                [
                    "Octava SSmi Corporis Christi",
                    "dm",
                    corpus_christi + week(1),
                ]
            )
        if x[0] == "Dominica III post Pentecosten infra Octavam SSmi Cordis DNJC":
            ssmi_cordis = easter(year) + week(i) - indays(2)
            j = 0
            for y in romans[1:7]:
                if (ssmi_cordis + indays(j + 1)) == (easter(year) + week(i)):
                    pass
                else:
                    cycle.append(
                        [
                            "De " + y + " die infra Oct Ss Cordis Jesu",
                            "sd",
                            ssmi_cordis + indays(j + 1),
                        ]
                    )
                j += 1
            cycle.append(
                [
                    "Sacratissimi Cordis Jesu",
                    "d1",
                    ssmi_cordis,
                ]
            )
            cycle.append(
                [
                    "Sacratissimi Cordis Jesu",
                    "dm",
                    ssmi_cordis + week(1),
                ]
            )
        cycle.append([x[0], x[1], easter(year) + week(i)])
        i += 1
    sept_counter = 0
    for x in romans[4:-1]:
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
                    easter(year) + week(i),
                ]
            )
            if (easter(year) + week(i)).strftime("%B") == "September":
                if int((easter(year) + week(i)).strftime("%d")) <= 3:
                    sept_counter += 0
                else:
                    sept_counter += 1
            if sept_counter == 2:
                cycle.append(
                    [
                        "Feria IV Quattuor Temporum Septembris",
                        "sd",
                        easter(year) + week(i) + indays(3),
                    ]
                )
                cycle.append(
                    [
                        "Feria VI Quattuor Temporum Septembris",
                        "sd",
                        easter(year) + week(i) + indays(5),
                    ]
                )
                cycle.append(
                    [
                        "Sabbato Quattuor Temporum Septembris",
                        "sd",
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
            cycle.append([x, "sd2", lastadvent - week(i)])
            cycle.append(
                [
                    "Feria IV Quattuor Temporum in Adventu",
                    "sp",
                    lastadvent - week(i) + indays(3),
                ]
            )
            cycle.append(
                [
                    "Feria VI Quattuor Temporum in Adventu",
                    "sp",
                    lastadvent - week(i) + indays(5),
                ]
            )
            cycle.append(
                [
                    "Sabbato Quattuor Temporum in Adventu",
                    "sp",
                    lastadvent - week(i) + indays(6),
                ]
            )
        else:
            cycle.append([x, "sd2", lastadvent - week(i)])
        i += 1
    # CHRISTMAS
    cycle.append(["Nativitas DNJC", "d1", christmas])
    if 5 <= int(christmas.strftime("%u")) <= 7 or christmas.strftime("%u") == 1:
        cycle.append(
            [
                "Dominica Infra Octavam Nativitatis reposit",
                "sd",
                christmas + indays(5),
            ]
        )
    else:
        cycle.append(
            [
                "Dominica Infra Octavam Nativitatis",
                "sd",
                christmas + indays(7) - findsunday(christmas),
            ]
        )
    if (
        int(day(this_year, 12, 30).strftime("%u")) == 1
        or int(day(this_year, 12, 30).strftime("%u")) == 7
    ):
        cycle.append(
            [
                "De VI Die infra Octavam Nativitatis",
                "sd",
                christmas + indays(5),
            ]
        )
    cycle.extend(
        [
            [
                "S Stephani Protomartyris",
                "d2",
                christmas + indays(1),
            ],
            [
                "S Joannis Ap & Ev",
                "d2",
                christmas + indays(2),
            ],
            [
                "Ss Innocentium Mm",
                "d2",
                christmas + indays(3),
            ],
            [
                "S Thomas EM",
                "d",
                christmas + indays(4),
            ],
            [
                "S Sylvestri I PC",
                "d",
                christmas + indays(6),
            ],
        ]
    )
    ########################################################################
    # SEND LIST TO CSV, HTML AND TERMINAL
    # this is to be turned into a seperate function eventually
    print("\n")
    gen_file = "temporal/temporal_" + str(this_year)
    # print to terminal
    for row in cycle:
        try:
            if len(row[0]) >= 19:
                feast_formatted = row[0][0:18] + "…"
            else:
                feast_formatted = row[0] + "." * (19 - len(row[0]))
            print(
                feast_formatted
                + "\t"
                + row[1]
                + "\t"
                + str(row[2].strftime("%a"))
                + "\t"
                + str(row[2].strftime("%x"))
            )
        except TypeError:
            pass
    # print to dictionary file
    original_stdout = sys.stdout
    with open(gen_file + ".py", "w") as f:
        sys.stdout = f
        print("temporal = {")
        keylist = ["feast", "rank"]
        memory = []
        for row in cycle:
            temporal_event = row[2].strftime("%m/%d")
            if temporal_event in memory:
                temporal_event += "."
            memory.append(temporal_event)
            mini_dict = str(dict(zip(keylist, [row[0], row[1]])))
            print(str(" '" + temporal_event + "'" + ": " + mini_dict + ","))
        print("}")
        sys.stdout = original_stdout


def app():
    user1 = ""
    user2 = ""
    while user1 != "exit":
        user1 = input('\nEnter "exit" to quit\nEnter 4-digit year: ')
        if user1 == "exit":
            break
        user2 = input(
            '\nYou can request a range. Press "ENTER" to skip.\nEnter 4-digit year for the end of the range: '
        )
        if user2 == "":
            try:
                temporal(user1)
                stitch.stitch(user1)
            except ValueError:
                pass
        else:
            try:
                for x in range(int(user1), int(user2) + 1):
                    temporal(x)
                    stitch.stitch(x)
            except ValueError:
                pass


app()
