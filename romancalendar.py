import importlib
import re
import sys
from datetime import datetime
from datetime import timedelta
from stitch import occur

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
    #! Needs work, maybe not necessary?
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


def build_temporal(year):
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
                [1, 5],
                circumcision,
            ],
            [
                "Octava S Stephani Protomartyris",
                [9, 7],
                circumcision + indays(1),
            ],
            [
                "Octava S Joannis Ap & Ev",
                [9, 7],
                circumcision + indays(2),
            ],
            [
                "Octava Ss Innocentium Mm",
                [9, 7],
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
                [1, 5],
                day(this_year, 1, 2),
            ]
        )
    else:
        sunday_post_cir_pre_ep = circumcision - findsunday(circumcision) + week(1)
        cycle.append(
            [
                "SS Nominis Jesu",
                [1, 5],
                sunday_post_cir_pre_ep,
            ]
        )
    # '*GESIMAS'
    gesimas = ["Septuagesima", "Sexagesima", "Quinquagesima"]
    i = 1
    for x in gesimas:
        if x == "Septuagesima":
            septuadate = easter(year) - week(10 - i)
        cycle.append(
            [
                "Dominica in " + x,
                [False, 1],
                easter(year) - week(10 - i),
            ]
        )
        i += 1
    # EPIPHANY
    epiphany = day(this_year, 1, 6)
    epiph_sundays = ["I", "II", "III", "IV", "V", "VI"]
    cycle.append(
            [
                "Vigilia Epiphaniæ",
                [7, 2, False, False, 'sd Vig Privil II cl', 0],
                epiphany - indays(1),
            ],
        )
    cycle.append(
            [
                "Epiphania Domini",
                [False, 0, False, False, 'd I cl cum Oct Privil 2 ord', 100],
                epiphany,
            ],
        )
    if weekday(epiphany) == "Sun":
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
                    [False, 11],
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
                        [False, 6],
                        epiph_counter,
                    ]
                )
                cycle.append(
                    [
                        "S Familiæ Jesu Mariæ et Joseph",
                        [False, 8],
                        epiph_counter - indays(1),
                    ]
                )
            else:
                cycle.append(
                    [
                        "S Familiæ Jesu Mariæ et Joseph; Dominica "
                        + epiph_sundays[o]
                        + " post Epiphaniam",
                        [False, 8],
                        epiph_counter,
                    ]
                )
        else:
            cycle.append(
                [
                    "Dominica " + epiph_sundays[o] + " post Epiphaniam",
                    [False, 2],
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
                    [False, 3],
                    easter(year) - week(10 - i) - indays(4),
                ]
            )
            cycle.append(
                [
                    "Feria V post Diem Cinerum",
                    [False, 3],
                    easter(year) - week(10 - i) - indays(3),
                ]
            )
            cycle.append(
                [
                    "Feria VI post Diem Cinerum",
                    [False, 14],
                    easter(year) - week(10 - i) - indays(2),
                ]
            )
            cycle.append(
                [
                    "Sabbato post Diem Cinerum",
                    [False, 14],
                    easter(year) - week(10 - i) - indays(1),
                ]
            )
        cycle.append(
            [
                "Dominica " + x,
                [False, 0],
                easter(year) - week(10 - i),
            ]
        )
        j = 1
        for y in feria:
            if x == "de Passione" and y == "Feria VI":
                cycle.append(
                    [
                        "Septem Dolorum BMV",
                        [False, 8],
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Feria IV":
                cycle.append(
                    [
                        "Feria IV Quattuor Temporum Quadragesimæ",
                        [False, 14],
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Feria VI":
                cycle.append(
                    [
                        "Feria VI Quattuor Temporum Quadragesimæ",
                        [False, 14],
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Sabbato":
                cycle.append(
                    [
                        "Sabbato Quattuor Temporum Quadragesimæ",
                        [False, 14],
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "in Palmis" and y == "Feria V":
                cycle.append(
                    [
                        y + " in Cœna Domini",
                        [False, 3],
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "in Palmis" and y == "Feria VI":
                cycle.append(
                    [
                        y + " in Parasceve",
                        [False, 4],
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "in Palmis" and y == "Sabbato":
                cycle.append(
                    [
                        "Sabbatum Sanctum",
                        [False, 4],
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "in Palmis":
                cycle.append(
                    [
                        y + " Majoris Hebd; Feria Priv",
                        [False, 4],
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            else:
                cycle.append(
                    [
                        y + " infra Hebd " + x,
                        [False, 3],
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            j += 1
        i += 1
    cycle.append(["Dominica Resurrectionis", [False, 0], easter(year)])
    cycle.extend(
        [
            [
                "Feria II Paschatis",
                [False, 3],
                easter(year) + indays(1),
            ],
            [
                "Feria III Paschatis",
                [False, 3],
                easter(year) + indays(2),
            ],
            [
                "De die IV infra Oct Paschæ",
                [False, 3],
                easter(year) + indays(3),
            ],
            [
                "De die V infra Oct Paschæ",
                [False, 3],
                easter(year) + indays(4),
            ],
            [
                "De die VI infra Oct Paschæ",
                [False, 3],
                easter(year) + indays(5),
            ],
            [
                "Sabbatum in Albis",
                [False, 3],
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
                        [False, 4],
                        easter(year) + week(i) + indays(3),
                    ],
                    #TODO: We need all the days within the octave
                    [
                        "Octava Solemnitas S Joseph",
                        [False, 7],
                        easter(year) + week(i + 1) + indays(3),
                    ],
                ]
            )
        if x == "Dominica V post Pascha":
            cycle.extend(
                [
                    [
                        "Litaniæ Minores",
                        [9, 14],
                        easter(year) + week(i) + indays(1),
                    ],
                    [
                        "Litaniæ Minores",
                        [9, 14],
                        easter(year) + week(i) + indays(2),
                    ],
                    [
                        "Litaniæ Minores",
                        [9, 14],
                        easter(year) + week(i) + indays(3),
                    ],
                    [
                        "Vigilæ Ascensionis",
                        [7, 3],
                        easter(year) + week(i) + indays(3),
                    ],
                    [
                        "Ascensio DNJC",
                        [False, 4],
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
                            [5, 7],
                            ascension_day + indays(j + 1),
                        ]
                    )
                j += 1
        if x == "Dominica in Albis": cycle.append([x, [False, 0], easter(year) + week(i)])
        else: cycle.append([x, [False, 2], easter(year) + week(i)])
        i += 1
    cycle.extend(
        [
            [
                "Vigilia Pentecostes",
                [7, 3],
                easter(year) + week(i) - indays(1),
            ],
            [
                "Dominica Pentecostes",
                [0, 4],
                easter(year) + week(i),
            ],
        ]
    )
    j = 0
    for y in romans[1:6]:
        if y == "II" or y == "III":
            cycle.append(
                [
                    "De " + y + " die infra Oct Pentecostes",
                    [0, 4],
                    ascension_day + indays(j + 1),
                ]
            )
        else:
            cycle.append(
                [
                    "De " + y + " die infra Oct Pentecostes",
                    [5, 4],
                    ascension_day + indays(j + 1),
                ]
            )
        j += 1
    cycle.append(
        [
            "Sabbato die infra Oct Pentecostes",
            [5, 4],
            ascension_day + indays(j + 1),
        ]
    )
    cycle.append(
        [
            "Feria IV Quattuor infra Temporum Pentecostes",
            [False, 10],
            easter(year) + week(i) + indays(3),
        ]
    )
    cycle.append(
        [
            "Feria VI Quattuor infra Temporum Pentecostes",
            [False, 10],
            easter(year) + week(i) + indays(5),
        ]
    )
    cycle.append(
        [
            "Sabbato Quattuor infra Temporum Pentecostes",
            [False, 10],
            easter(year) + week(i) + indays(6),
        ]
    )
    i += 1
    # SUNDAYS AFTER PENTECOST
    prelim_pents = [
        ["Dominica Sanctissimæ Trinitatis", [False, 4]],
        ["Dominica II post Pentecosten infra Octavam Corporis Christi", [False, 2]],
        ["Dominica III post Pentecosten infra Octavam SSmi Cordis DNJC", [False, 2]],
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
                            [False, 6],
                            corpus_christi + indays(j + 1),
                        ]
                    )
                j += 1
            cycle.append(
                [
                    "Sanctissimi Corporis Christi",
                    [False, 4],
                    corpus_christi,
                ]
            )
            cycle.append(
                [
                    "Octava SSmi Corporis Christi",
                    [False, 8],
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
                            [False, 7],
                            ssmi_cordis + indays(j + 1),
                        ]
                    )
                j += 1
            cycle.append(
                [
                    "Sacratissimi Cordis Jesu",
                    [False, 4],
                    ssmi_cordis,
                ]
            )
            cycle.append(
                [
                    "Octava Sacratissimi Cordis Jesu",
                    [False, 8],
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
                    [False, 2],
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
                        [False, 14],
                        easter(year) + week(i) + indays(3),
                    ]
                )
                cycle.append(
                    [
                        "Feria VI Quattuor Temporum Septembris",
                        [False, 14],
                        easter(year) + week(i) + indays(5),
                    ]
                )
                cycle.append(
                    [
                        "Sabbato Quattuor Temporum Septembris",
                        [False, 14],
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
                    [False, 14],
                    lastadvent - week(i) + indays(3),
                ]
            )
            cycle.append(
                [
                    "Feria VI Quattuor Temporum in Adventu",
                    [False, 14],
                    lastadvent - week(i) + indays(5),
                ]
            )
            cycle.append(
                [
                    "Sabbato Quattuor Temporum in Adventu",
                    [False, 14],
                    lastadvent - week(i) + indays(6),
                ]
            )
        elif x == "Dominica I Adventus":
            cycle.append([x, [False, 0], lastadvent - week(i)])
        else:
            cycle.append([x, [False, 1], lastadvent - week(i)])
        i += 1
    # CHRISTMAS
    cycle.append(["Nativitas DNJC", [False, 4], christmas])
    if 5 <= int(christmas.strftime("%u")) <= 7 or christmas.strftime("%u") == 1:
        cycle.append(
            [
                "Dominica Infra Octavam Nativitatis reposit",
                [False, 7],
                christmas + indays(5),
            ]
        )
    else:
        cycle.append(
            [
                "Dominica Infra Octavam Nativitatis",
                [False, 7],
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
                [False, 7],
                christmas + indays(5),
            ]
        )
    cycle.extend(
        [
            [
                "S Stephani Protomartyris",
                [False, 5],
                christmas + indays(1),
            ],
            [
                "S Joannis Ap & Ev",
                [False, 5],
                christmas + indays(2),
            ],
            [
                "Ss Innocentium Mm",
                [False, 5],
                christmas + indays(3),
            ],
            [
                "S Thomas EM",
            [False, 5],
                christmas + indays(4),
            ],
            [
                "S Sylvestri I PC",
            [False, 5],
                christmas + indays(6),
            ],
        ]
    )
    
    def dict_clean(dict):
        mdl = importlib.import_module('temporal.temporal_' + str(dict))
        i = 0
        dic = mdl.temporal
        x = sorted(dic)
        for second in x:
            try: 
                first = x[i+1]
                if first[0:5] == second and len(first) == 6:
                    #todo add a "nobility meter" to the feasts
                    ranker = occur(dic[first]['rank'][0], dic[second]['rank'][1])
                    if ranker == 1:
                        # office of the first
                        dic.update({first.strip('.'): dic[first]})
                        del dic[second], dic[first]
                    elif ranker == 2:
                        # office of the second
                        dic.update({first.strip('.'): dic[second]})
                        del dic[second], dic[first]
                    elif ranker == 3:
                        # commemoration of the second
                        dic[second].update({'feast': dic[first]['feast'], 'rank': dic[first]['rank'], 'target': dic[first]['target'], 'com1': dic[second]['feast']})
                        del dic[first]
                    elif ranker == 4:
                        # commemoration of the first
                        dic.update({first.strip('.'): {'feast': dic[second]['feast'], 'rank': dic[second]['rank'], 'target': dic[second]['target'], 'com1': dic[second]['feast']}})
                        del dic[first]
                    elif ranker == 5:
                        # translation of the second
                        dic.update({'trans' + second.strip('.'): dic[second]})
                        del dic[second]
                    elif ranker == 6:
                        # translation of the first
                        dic.update({'trans_' + first.strip('.'): dic[first]})
                        del dic[first]
                    elif ranker == 7:
                        # office of more noble, commemoration of the less noble
                        continue
                    elif ranker == 8:
                        # office of the more noble, translation of the less noble
                        continue                        
                    else: pass
                else: pass
                i += 1
            except IndexError:
                break
        gen_file = "temporal/temporal_" + str(dict)
        with open(gen_file + ".py", "a") as f:
            f.truncate(0)
            i = 0
            for line in sorted(dic):
                if i == 0: f.write('temporal = {\n\'' + line + '\' : ' + str(dic[line]) + ',\n')
                else: f.write('\'' + line + '\' : ' + str(dic[line]) + ',\n')
                i += 1
            f.write('}')
            f.close()

    def make_dict(year):
        gen_file = "temporal/temporal_" + str(year)
        with open(gen_file + ".py", "w") as f:
            f.write("temporal = {")
            keylist = ["feast", "rank", "target"]
            memory = []
            for row in cycle:
                temporal_event = row[-1].strftime("%m/%d")
                if temporal_event in memory:
                    temporal_event += "."
                memory.append(temporal_event)
                mini_dict = str(dict(zip(keylist, [row[0], row[1], re.sub("datetime.", r"", str(row[2]))])))
                f.write(str("\n'" + temporal_event + "'" + ": " + mini_dict + ","))
            f.write("}")
        f.close()
        dict_clean(year)

    make_dict(2021)

def app():
    build_temporal(2021)

app()
