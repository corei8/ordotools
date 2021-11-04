import re
from datetime import datetime, timedelta
# from functions import stitch, latex_temporal_test, dict_clean_2
from functions import *

# TODO: find the letter of the Martyrology
# TODO: special antiphons for the all saturdays, maybe integrate them?


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
        "Sabbatum",
    ]
    circumcision = day(this_year, 1, 1)
    cycle.extend(
        [
            [  # ! vespers
                "Circumcisio DNJC et Oct. Nativitatis",
                [3, 'd II cl'],
                # // [1, 5, 2, 2, 80, "d II cl"],
                {'int': 'Dum medium', 'glo': True, 'com1': 'S. Telesphori PM', 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                circumcision,
            ],
            [  # ! vespers
                "Octava S. Stephani Protomartyris",
                [18, 's'],
                # // [9, 7, 4, 10, 10, "s"],
                {'int': 'Sederunt', 'glo': True,
                    'cre': False, 'pre': 'de Nativitate'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                circumcision + indays(1),
            ],
            [  # ! mass, vespers
                "Octava S. Joannis Ap Ev",
                [18, 's'],
                # // [9, 7, 4, 10, 30, "s"],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                circumcision + indays(2),
            ],
            [  # ! mass, vespers
                "Octava Ss Innocentium Mm.",
                [18, 's'],
                # // [9, 7, 4, 10, 10, "s"],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
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
            [  # ! vespers
                "Ssmi Nominis Jesu",
                [10, 'd II cl'],
                # // [1, 5, 2, 2, 80, "d II cl"],
                {'int': 'In nomine Jesu', 'glo': True,
                    'cre': True, 'pre': 'de Nativitate'},
                day(this_year, 1, 2),
            ]
        )
    else:
        sunday_post_cir_pre_ep = circumcision - \
            findsunday(circumcision) + week(1)
        cycle.append(
            [  # ! vespers
                "Ssmi Nominis Jesu",
                [10, 'd II cl'],
                # // [1, 5, 2, 2, 80, "d II cl"],
                {'int': 'In nomine Jesu', 'glo': True,
                    'cre': True, 'pre': 'de Nativitate'},
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
            [  # ! mass, vespers
                "Dominica in " + x,
                [8, 'sd II cl'],
                # // [5, 1, 0, 0, False, "sd II cl"],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                easter(year) - week(10 - i),
            ]
        )
        i += 1
    # EPIPHANY
    epiphany = day(this_year, 1, 6)
    epiph_sundays = ["I", "II", "III", "IV", "V", "VI"]
    cycle.append(
        [  # ! mass, vespers
            "Vigilia Epiphaniæ",
            [12, 'sd Vig privil 2 cl'],
            # // [7, 2, 7, 0, False, "sd Vig privil II cl"],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
            epiphany - indays(1),
        ],
    )
    cycle.append(
        [  # ! mass, vespers
            "Epiphania DNJC",
            [2, 'd I cl cum Oct privil 2 ord'],
            # // [0, 4, 1, 1, 80, "d I cl cum Oct. privil 2 ord"],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
            epiphany,
        ],
    )
    cycle.append(
        [  # ! mass, vespers
            "Octava Epiphaniæ",
            [13, 'dm'],
            # // [0, 4, 1, 1, 80, "d I cl cum Oct. privil 2 ord"],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
            epiphany + indays(7),
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
                [  # ! mass, vespers
                    "Feria "
                    + epiph_oct_days[ep_oct_days_counter - 1]
                    + " infra Oct. Epiphaniæ",
                    [9, 'feria'],
                    # // [False, 11, 8, 7, False, "s"],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
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
                cycle.append(  # ? is this necessary?
                    [  # ! vespers
                        "In Octava Epiphaniæ",
                        [13, 'dm'],
                        # // [3, 6, 3, 0, 80, "dm"],
                        {'int': 'Ecce advenit', 'glo': True,
                            'cre': True, 'pre': 'et Communicantes de Epiphania'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        epiph_counter,
                    ]
                )
                cycle.append(
                    [  # ! mass, vespers
                        "S. Familiæ Jesu, Mariæ, Joseph",
                        [11, 'dm'],
                        # // [3, 8, 5, 4, 80, "dm"],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        epiph_counter - indays(1),
                    ]
                )
            else:
                cycle.append(
                    [  # ! mass, vespers
                        "S. Familiæ Jesu, Mariæ, Joseph; Dominica " +
                        epiph_sundays[o] + " infra Oct. Epiphaniæ",
                        [11, 'dm'],
                        # // [3, 8, 5, 4, 80, "dm"],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        epiph_counter,
                    ]
                )
        else:
            cycle.append(
                [  # ! mass, vespers
                    "Dominica " + epiph_sundays[o] + " post Epiphaniam",
                    [12, 'sd'],
                    # // [5, 2, 0, 0, False, "sd"],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
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
        "IV in Quadragesima (Lætare)",
        "de Passione",
        "in Palmis",
    ]
    for x in quads:
        if x == "I in Quadragesima":
            # ! use extend
            cycle.append(
                [  # ! mass, vespers
                    "Dies Cinerum",
                    [3, 'feria'],
                    # // [9, 3, False, False, False, "feria"],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    easter(year) - week(10 - i) - indays(4),
                ]
            )
            cycle.append(
                [  # ! mass, vespers
                    "Feria V post Diem Cinerum",
                    [18, 'feria'],
                    # // [9, 3, False, False, False, "feria"],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    easter(year) - week(10 - i) - indays(3),
                ]
            )
            cycle.append(
                [  # ! mass, vespers
                    "Feria VI post Diem Cinerum",
                    [18, 'feria'],
                    # // [9, 3, False, False, False, "feria"],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    easter(year) - week(10 - i) - indays(2),
                ]
            )
            cycle.append(
                [  # ! mass, vespers
                    "Sabbatum post Diem Cinerum",
                    [18, 'feria'],
                    # // [9, 3, False, False, False, "feria"],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    easter(year) - week(10 - i) - indays(1),
                ]
            )
        cycle.append(
            [  # ! mass, vespers
                "Dominica " + x,
                [1, 'sd I cl'],
                # // [5, 0, 0, 0, False, 'sd I cl'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                easter(year) - week(10 - i),
            ]
        )
        j = 1
        for y in feria:
            if x == "de Passione" and y == "Feria VI":
                cycle.append(
                    [  # ! mass, vespers
                        "Septem Dolorum BMV",
                        [14, 'dm'],
                        # // [3, 8, 5, 4, 70, 'dm'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Feria IV":
                cycle.append(
                    [  # ! mass, vespers
                        "Feria IV Quatuor Temporum Quadragesimæ",
                        [3, 'feria'],
                        # // [False, 14],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Feria VI":
                cycle.append(
                    [  # ! mass, vespers
                        "Feria VI Quatuor Temporum Quadragesimæ",
                        [3, 'feria'],
                        # // [False, 14],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Sabbatum":
                cycle.append(
                    [  # ! mass, vespers
                        "Sabbatum Quatuor Temporum Quadragesimæ",
                        [3, 'feria'],
                        # // [False, 14],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "in Palmis" and y == "Feria V":
                cycle.append(
                    [  # ! mass, vespers
                        y + " in Cœna Domini",
                        [2, 'd I cl'],
                        # // [False, 3],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "in Palmis" and y == "Feria VI":
                cycle.append(
                    [  # ! mass, vespers
                        y + " in Parasceve",
                        [2, 'd I cl'],
                        # // [False, 4],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "in Palmis" and y == "Sabbatum":
                cycle.append(
                    [  # ! mass, vespers
                        "Sabbatum Sanctum",
                        [2, 'd I cl'],
                        # // [False, 4],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            elif x == "in Palmis":
                cycle.append(
                    [  # ! vespers
                        y + " Majoris Hebd",
                        [3, 'feria'],
                        # // [9, 3, False, 10, "s"],
                        {'int': 'Judica, Domine' if y == 'Feria II' else (
                            'Nos autem' if y == 'Feria III' else 'In nomine Jesu'), 'glo': False, 'cre': False, 'pre': 'de Cruce'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            else:
                lent_masses = ['Sicut oculi', 'Domine refugium', 'Reminíscere',  'Confessio', 'De necessitatibus',
                               'Intret oratio', 'Redime me', 'Tibi dixit', 'Ne derelinquas me',
                               'Deus, in adjutorium', 'Ego autem', 'Lex Domini', 'In Deo laudabo', 'Ego clamavi',
                               'Ego autem', 'Salus populi', 'Fac mecum', 'Verba mea', 'Deus, in nomine', 'Exaudi, Deus',
                               'Cum sanctificatus', 'Lætetur cor', 'Meditatio', 'Sitientes', 'Miserere mihi',
                               'Expecta Dominum', 'Liberator meus', 'Omnia, quæ fecisti', 'Miserere mihi', 'Miserere mihi', ]

                if x == "IV in Quadragesima (Lætare)":
                    new_x = re.sub("\(Lætare\)", "", x)
                else:
                    new_x = x
                cycle.append(
                    [  # ! vespers
                        y + " infra Hebd " + new_x,
                        [18, 'feria'],
                        # // [9, 12, False, False, 0, 's'],
                        {'int': lent_masses[j-1], 'glo': False,
                            'cre': False, 'pre': 'de Quadragesima' if x != 'de Passione' else 'de Cruce'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        easter(year) - week(10 - i) + indays(j),
                    ]
                )
            j += 1
        i += 1
    cycle.append(
        [  # ! mass, vespers
            "Dominica Resurrectionis",
            [1, 'd I cl cum Oct privil I ord'],
            # // [False, 0],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
            easter(year)
        ]
    )  # ? should above be connected to extend() below?
    cycle.extend(
        [
            [  # ! mass, vespers
                "Feria II infra Oct. Paschæ",
                [2, 'd I cl'],
                # // [False, 3],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                easter(year) + indays(1),
            ],
            [  # ! mass, vespers
                "Feria III infra Oct. Paschæ",
                [2, 'd I cl'],
                # // [False, 3],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                easter(year) + indays(2),
            ],
            [  # ! mass, vespers
                "Feria IV infra Oct. Paschæ",
                [3, 'sd'],
                # // [False, 3],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                easter(year) + indays(3),
            ],
            [  # ! mass, vespers
                "Feria V infra Oct. Paschæ",
                [3, 'sd'],
                # // [False, 3],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                easter(year) + indays(4),
            ],
            [  # ! mass, vespers
                "Feria VI infra Oct. Paschæ",
                [3, 'sd'],
                # // [False, 3],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                easter(year) + indays(5),
            ],
            [  # ! mass, vespers
                "Sabbatum in Albis",
                [3, 'sd'],
                # // [False, 3],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
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
                        #! mass, vespers
                        "Solemnitas S. Joseph, Sponsi BMV C. et Ecclesiæ Universalis Patroni",
                        [2, 'd I cl cum Oct Communi'],
                        # // [False, 4],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        easter(year) + week(i) + indays(3),
                    ],
                    # TODO: We need all the days within the octave
                    [  # ! mass, vespers
                        "Octava Solemnitatis S. Joseph",
                        [13, 'dm'],
                        # // [False, 7],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        easter(year) + week(i + 1) + indays(3),
                    ],
                ]
            )
        if x == "Dominica V post Pascha":
            cycle.extend(
                [
                    [  # ! vespers
                        "In Rogationibus",
                        [21, 's'],
                        # // [9, 14, False, 10, 0, "sp"],
                        {'int': 'Exaudivit', 'glo': False,
                            'cre': False, 'pre': 'Paschalis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        easter(year) + week(i) + indays(1),
                    ],
                    [  # ! vespers
                        "In Rogationibus",
                        [21, 's'],
                        # // [9, 14, False, 10, 0, "sp"],
                        {'int': 'Exaudivit', 'glo': False,
                            'cre': False, 'pre': 'Paschalis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        easter(year) + week(i) + indays(2),
                    ],
                    [  # ! vespers
                        "In Rogationibus",
                        [21, 's'],
                        # // [9, 14, False, 10, 0, "sp"],
                        {'int': 'Exaudivit', 'glo': False,
                            'cre': False, 'pre': 'Paschalis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        easter(year) + week(i) + indays(3),
                    ],
                    [  # ! mass, vespers
                        "Vigilæ Ascensionis",
                        [18, 'feria'],
                        # // [7, 3],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        easter(year) + week(i) + indays(3),
                    ],
                    [  # ! vespers
                        "Ascensio DNJC",
                        [2, 'd I cl cum Oct privil 3 ord'],
                        # // [0, 4, 1, 1, 80, "d I cl cum Oct. Priv. III ordinis"],
                        {'int': 'Viri Galilæi', 'glo': True,
                            'cre': True, 'pre': 'et Communicantes de Ascensione'},
                        easter(year) + week(i) + indays(4),
                    ],
                    [  # ! vespers
                        "Oct. Ascensionis DNJC",
                        [13, 'dm'],
                        # // [3, 8, 3, 3, 80, "dm"],
                        {'int': 'Viri Galilæi', 'glo': True,
                            'cre': True, 'pre': 'et Communicantes de Ascensione'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        easter(year) + week(i) + indays(4+7),
                    ],
                ]
            )
            ascension_day = easter(year) + week(i) + indays(5)
        if x == "Dominica infra Octavam Ascensionis":
            j = 0
            for y in ROMANS[1:6]:
                # pass if the day w/in the octave is a sunday
                if (ascension_day + indays(j + 1)) == (easter(year) + week(i)):
                    pass
                elif (ascension_day + indays(j + 1)).strftime("%A") == "Saturday":
                    cycle.append(
                        [  # ! mass, vespers
                            "Sabbatum infra Oct. Ascensionis",
                            [16, 'sd'],
                            # // [5, 7],
                            {'int': 'Missa', 'glo': True,
                                'cre': True, 'pre': 'Communis'},
                            ascension_day + indays(j + 1),
                        ]
                    )
                else:
                    cycle.append(
                        [  # ! mass, vespers
                            "Feria " + y + " infra Oct. Ascensionis",
                            [16, 'sd'],
                            # // [5, 7],
                            {'int': 'Missa', 'glo': True,
                                'cre': True, 'pre': 'Communis'},
                            ascension_day + indays(j + 1),
                        ]
                    )
                j += 1
        if x == "Dominica in Albis":
            cycle.append(
                [  # ! mass, vespers
                    x,
                    [1, 'dm'],
                    # // [False, 0],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    easter(year) + week(i)
                ]
            )
        else:
            cycle.append(
                [  # ! mass, vespers
                    x,
                    [12, 'sd'],
                    # // [False, 2],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    easter(year) + week(i)
                ]
            )
        i += 1
    pent_date = easter(year) + week(i)
    cycle.extend(
        [
            [  # ! mass, vespers
                "Vigilia Pentecostes",
                [3, 'd I cl Vig privil I cl'],
                # // [7, 3],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                easter(year) + week(i) - indays(1),
            ],
            [  # ! mass, vespers
                "Dominica Pentecostes",
                [1, 'd I cl cum Oct privil I ord'],
                # // [0, 4],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                easter(year) + week(i),
            ],
        ]
    )
    j = 0
    for y in ROMANS[1:6]:
        if y == "II" or y == "III":
            cycle.append(
                [  # ! mass, vespers
                    "Feria " + y + " infra Oct. Pentecostes",
                    [2, 'd I cl'],
                    # // [0, 4],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    pent_date + indays(j + 1),
                ]
            )
        else:
            cycle.append(
                [  # ! mass, vespers
                    "Feria " + y + " infra Oct. Pentecostes",
                    [3, 'sd'],
                    # // [5, 4],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    pent_date + indays(j + 1),
                ]
            )
        j += 1
    cycle.append(
        [  # ! mass, vespers
            "Sabbatum infra Oct. Pentecostes",
            [3, 'sd'],
            # // [5, 4],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
            pent_date + indays(j + 1),
        ]
    )
    cycle.append(
        [  # ! mass, vespers
            "Feria IV Quatuor Temporum infra Oct. Pentecostes",
            [18, 'feria'],
            # // [False, 10],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
            easter(year) + week(i) + indays(3),
        ]
    )
    cycle.append(
        [  # ! mass, vespers
            "Feria VI Quatuor Temporum infra Oct. Pentecostes",
            [18, 'feria'],
            # // [False, 10],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
            easter(year) + week(i) + indays(5),
        ]
    )
    cycle.append(
        [  # ! mass, vespers
            "Sabbatum Quatuor Temporum infra Oct. Pentecostes",
            [18, 'feria'],
            # // [False, 10],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
            easter(year) + week(i) + indays(6),
        ]
    )
    i += 1
    # SUNDAYS AFTER PENTECOST
    prelim_pents = [
        [  # ! mass, vespers
            "Festum Sanctissimæ Trinitatis",
            [2, 'd I cl'],
            # // [False, 4],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
        ],
        [  # ! mass, vespers
            "Dominica infra Oct. Ssmi Corporis Christi (Dominica II post Pentecosten)",
            [12, 'sd'],
            # // [False, 2],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
        ],
        [  # ! mass, vespers
            "Dominica infra Oct. Ssmi Cordis DNJC (Dominica III post Pentecosten)",
            [12, 'sd'],
            # // [False, 2],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
        ],
    ]
    for x in prelim_pents:
        if x[0] == "Dominica infra Oct. Ssmi Corporis Christi (Dominica II post Pentecosten)":
            corpus_christi = easter(year) + week(i) - indays(3)
            j = 0
            for y in ROMANS[1:7]:
                if (corpus_christi + indays(j + 1)) == (easter(year) + week(i)):
                    pass
                else:
                    feria_index = int(
                        (corpus_christi + indays(j + 1)).strftime("%w")) - 1
                    fer_num = feria[feria_index]
                    cycle.append(
                        [
                            fer_num + " infra Oct. Ssmi Corporis Christi",
                            [9, 'sd'],
                            # // [False, 6],
                            {'int': 'Missa', 'glo': True,
                                'cre': True, 'pre': 'Communis'},
                            corpus_christi + indays(j + 1),
                        ]
                    )
                j += 1
            cycle.append(
                [  # ! mass, vespers
                    "Sanctissimi Corporis Christi",
                    [2, 'd I cl cum Oct privil 2 ord'],
                    # // [False, 4],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    corpus_christi,
                ]
            )
            cycle.append(
                [  # ! mass, vespers
                    "Octava Ssmi Corporis Christi",
                    [4, 'dm'],
                    # // [False, 8],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    corpus_christi + week(1),
                ]
            )
        if x[0] == "Dominica infra Oct. Ssmi Cordis DNJC (Dominica III post Pentecosten)":
            ssmi_cordis = easter(year) + week(i) - indays(2)
            j = 0
            for y in ROMANS[1:7]:
                if (ssmi_cordis + indays(j + 1)) == (easter(year) + week(i)):
                    pass
                else:
                    feria_index = int(
                        (ssmi_cordis + indays(j + 1)).strftime("%w")) - 1
                    fer_num = feria[feria_index]
                    cycle.append(
                        [  # ! mass, vespsers
                            fer_num + " infra Oct. Ssmi Cordis Jesu",
                            # ? is this supposed to be within a common octave?
                            [17, 'sd'],
                            # //[False, 7],
                            {'int': 'Missa', 'glo': True,
                                'cre': True, 'pre': 'Communis'},
                            ssmi_cordis + indays(j + 1),
                        ]
                    )
                j += 1
            cycle.append(
                [  # ! mass, vespers
                    "Sacratissimi Cordis Jesu",
                    [2, 'd I cl cum Oct privil 3 ord'],
                    # //[False, 4],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    ssmi_cordis,
                ]
            )
            cycle.append(
                [  # ! mass, vespers
                    "Octava Sacratissimi Cordis Jesu",
                    [13, 'dm'],
                    # //[False, 8],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    ssmi_cordis + week(1),
                ]
            )
        cycle.append([x[0], x[1], x[2], easter(year) + week(i)])
        i += 1
    sept_counter = 0
    for x in ROMANS[3:-1]:
        earliest_first_advent = str(year) + "-12-03"
        if easter(year) + week(i) >= datetime.strptime(
            earliest_first_advent, "%Y-%m-%d"
        ):
            break
        else:
            cycle.append(
                [  # ! mass, vespers
                    "Dominica " + x + " post Pentecosten",
                    [12, 'sd'],
                    # //[5, 10, 0, 0, 0, 'sd'],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    easter(year) + week(i),
                ]
            )
            if (easter(year) + week(i)).strftime("%B") == "September":
                if int((easter(year) + week(i)).strftime("%d")) <= 3:
                    sept_counter += 0
                else:
                    sept_counter += 1
            if sept_counter == 2:
                cycle.extend(
                    [
                        [  # ! mass, vespers
                            "Feria IV Quatuor Temporum Septembris",
                            [18, 'feria'],
                            # //[False, 14],
                            {'int': 'Missa', 'glo': True,
                             'cre': True, 'pre': 'Communis'},
                            easter(year) + week(i) + indays(3),
                        ],
                        [  # ! mass, vespers
                            "Feria VI Quatuor Temporum Septembris",
                            [18, 'feria'],
                            # //[False, 14],
                            {'int': 'Missa', 'glo': True,
                             'cre': True, 'pre': 'Communis'},
                            easter(year) + week(i) + indays(5),
                        ],
                        [  # ! mass, vespers
                            "Sabbatum Quatuor Temporum Septembris",
                            [18, 'feria'],
                            # //[False, 14],
                            {'int': 'Missa', 'glo': True,
                             'cre': True, 'pre': 'Communis'},
                            easter(year) + week(i) + indays(6),
                        ],
                    ]
                )

            if (easter(year) + week(i)).strftime("%B") == "November" and (easter(year) + week(i-1)).strftime("%B") == "October":
                # if the current Sunday is in November and the previous Sunday is in October... i.e. October's last Sunday
                christ_king = easter(year) + week(i) - week(1)
                cycle.append(
                    [  # ! vespers
                        'In Festo DNJC Regis',
                        [2, 'd I cl'],
                        # // [0, 4, 1, 1, 'd I cl'],
                        {'int': 'Dignus est', 'glo': True,
                            'cre': True, 'pre': 'de DNJC Rege'},
                        christ_king,
                    ],
                )
            i += 1
    # ? DNJC Regis is the last Sunday in October.
    # ADVENT
    christmas = datetime.strptime(str(year) + "-12-25", "%Y-%m-%d")
    lastadvent = christmas - findsunday(christmas)
    if christmas == lastadvent:  # prevents advent 4 and christmas occurance
        lastadvent -= week(1)
    advents = [
        "Dominica IV Adventus",
        "Dominica III Adventus",
        "Dominica II Adventus",
        "Dominica I Adventus",
    ]
    i = 0
    for x in advents:
        if x == "Dominica III Adventus":
            cycle.extend(
                [
                    [  # ! vespers
                        x,
                        [8, 'sd II cl'],
                        # // [5, 1, 0, 0, 0, 'sd'],
                        {'int': 'Populus Sion' if x == "Dominica II Adventus" else (
                            'Gaudete' if x == "Dominica III Adventus" else 'Rorate cæli'), 'glo': False, 'cre': True, 'pre': 'de Trinitate'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        lastadvent - week(i)
                    ],
                    [  # ! vespers
                        "Feria IV Quatuor Temporum in Adventus",
                        [18, 'feria'],
                        # //[9, False, False, 10, 's'],
                        {'int': 'Rorate cæli', 'glo': False,
                            'cre': False, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        lastadvent - week(i) + indays(3),
                    ],
                    [  # ! vespers
                        "Feria VI Quatuor Temporum in Adventus",
                        [18, 'feria'],
                        # //[9, False, False, 10, 's'],
                        {'int': 'Prope es tu', 'glo': False,
                            'cre': False, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        lastadvent - week(i) + indays(5),
                    ],
                    [  # ! vespers
                        "Sabbatum Quatuor Temporum in Adventus",
                        [18, 'feria'],
                        # // [9, False, False, 10, 's'],
                        {'int': 'Veni, et ostende', 'glo': False,
                            'cre': False, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        lastadvent - week(i) + indays(6),
                    ],
                ]
            )
        elif x == "Dominica I Adventus":  # because Dom I Advent is privileged
            cycle.append(
                [  # ! vespers
                    x,
                    [1, 'sd'],
                    # // [5, 0, 0, 0, 0, 'sd'],
                    {'int': 'Ad te levavi', 'glo': False,
                        'cre': True, 'pre': 'de Trinitate'},
                    {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                    lastadvent - week(i)
                ]
            )
        else:
            cycle.append(
                [  # ! vespers
                    x,
                    [8, 'sd II cl'],
                    # // [5, 1, 0, 0, 0, 'sd'],
                    {'int': 'Populus Sion' if x == "Dominica II Adventus" else (
                        'Gaudete' if x == "Dominica III Adventus" else 'Rorate cæli'), 'glo': False, 'cre': True, 'pre': 'de Trinitate'},
                    {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                    lastadvent - week(i)
                ]
            )
        i += 1
    # CHRISTMAS
    cycle.extend([
        [  # ! vespers
            "Vigilia Nativitas DNJC",
            [3, 'd I cl Vig privil I cl'],
            # // [3, 6, 6, 5, 'd'],
            {'int': 'Hodie scietis', 'glo': False,
                'cre': False, 'pre': 'Communis'},
            {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
            christmas - indays(1)
        ],  # TODO If the vigil is a Sunday, there is a commemoration, Creed, de Trinitate, but no Proper Last Gospel
        [  # ! vespers
            "Nativitas DNJC",
            [2, 'd I cl cum Oct privil 3 ord'],
            # // [0, 4, 1, 1, 80, 'd I cl cum Oct. Priv. III ord.'],
            {
                'Ad Primam Missam': {'int': 'Domine dixit', 'glo': True, 'cre': True, 'pre': 'et Communicantes (in hac Missa tantum dicitur "noctem") de Nativitate'},
                'Ad Secundam Missam': {'int': 'Lux fulgebit', 'glo': True, 'cre': True, 'pre': 'et Communicantes de Nativitate'},
                'Ad Tertiam Missam': {'int': 'Puer natus', 'glo': True, 'cre': True, 'pre': 'et Communicantes de Nativitate'},
            },
            {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
            christmas
        ],
    ]
    )
    if 5 <= int(christmas.strftime("%u")) <= 7 or christmas.strftime("%u") == 1:
        cycle.append(
            [  # ! mass, vespers
                "Dominica Infra Octavam Nativitatis reposita",
                [12, 'sd'],
                # // [False, 7],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                christmas + indays(5),
            ]
        )
    else:
        cycle.append(
            [  # ! vespers
                "Dominica Infra Octavam Nativitatis",
                [12, 'sd'],
                # // [5, 2, 0, 0, 0, 'sd'],
                {'int': 'Dum medium', 'glo': True, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                christmas + indays(7) - findsunday(christmas),
            ]
        )
    if (
        int(day(this_year, 12, 30).strftime("%u")) == 1
        or int(day(this_year, 12, 30).strftime("%u")) == 7
    ):
        cycle.append(
            [  # ! mass, vespers
                "Feria VI infra Octavam Nativitatis",
                [16, 'sd'],
                # // [False, 7],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                christmas + indays(5),
            ]
        )
    cycle.extend(
        [
            [  # ! vespers
                "S. Stephani Protomartyris",
                [10, 'd II cl cum Oct simplici'],
                # // [1, 5, 2, 2, 10, 'd II cl cum Oct simplici'],
                {'int': 'Sederunt', 'glo': True, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                christmas + indays(1),
            ],
            [  # ! vespers
                "S. Joannis Ap. Ev.",
                [10, 'd II cl cum Oct simplici'],
                # // [1, 5, 2, 2, 10, 'd II cl cum Oct simplici'],
                {'int': 'In medio ecclesiæ', 'glo': True, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                christmas + indays(2),
            ],
            [  # ! vespers
                "Ss Innocentium Mm.",
                [10, 'd II cl cum Oct simplici'],
                # // [1, 5, 2, 2, 10, 'd II cl cum Oct simplici'],
                {'int': 'Ex ore infantium', 'glo': True, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                christmas + indays(3),
            ],
            [  # ! vespers
                "S. Thomæ E.M.",
                [15, 'd'],
                # // [4, 9, 6, 5, 10, 'd'],
                {'int': 'Gaudeamus omnes', 'glo': True, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                christmas + indays(4),
            ],
            [  # ! mass, vespers
                "S. Silvestri I P.C.",
                [15, 'd'],
                # // [False, 5],
                {'int': 'Missa', 'glo': True, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                christmas + indays(6),
            ],
        ]
    )

    def make_dict(year: int):
        gen_file = "temporal/temporal_" + str(year)
        with open(gen_file + ".py", "w") as f:
            f.write("temporal = {")
            keylist = ["feast", "rank", "mass", ]  # "mass", ]
            memory = []
            for row in cycle:
                temporal_event = row[-1].strftime("%m/%d")
                if temporal_event in memory:
                    temporal_event += "."
                memory.append(temporal_event)
                mini_dict = str(
                    dict(
                        zip(
                            keylist,
                            [
                                row[0],
                                row[1],
                                row[2],
                                #re.sub("datetime.", r"", str(row[3]))
                                # row[3],
                            ],
                        )
                    )
                )
                f.write(
                    str("\n'" + temporal_event + "'" + ": " + mini_dict + ",")
                )
            f.write("}")
        f.close()
        dict_clean_2("temporal.temporal_", year)
    make_dict(year)


def app(year: int, diocese: str):
    build_temporal(year)
    latex_temporal_test(year)
    stitch(year, diocese)
    #dict_clean("calen.calendar_", year)


app(year=2022, diocese="roman")
