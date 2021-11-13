import re
from datetime import datetime
from functions import *
from outputs import latex_full_cal_test

LENT_MASSES = ['Sicut oculi', 'Domine refugium', 'Reminíscere',  'Confessio', 'De necessitatibus',
               'Intret oratio', 'Redime me', 'Tibi dixit', 'Ne derelinquas me',
               'Deus, in adjutorium', 'Ego autem', 'Lex Domini', 'In Deo laudabo', 'Ego clamavi',
               'Ego autem', 'Salus populi', 'Fac mecum', 'Verba mea', 'Deus, in nomine', 'Exaudi, Deus',
               'Cum sanctificatus', 'Lætetur cor', 'Meditatio', 'Sitientes', 'Miserere mihi',
               'Expecta Dominum', 'Liberator meus', 'Omnia, quæ fecisti', 'Miserere mihi', 'Miserere mihi', ]


def build_temporal(year):
    year = int(year)
    cycle = []
    # ? maybe get rid of this ?
    feria = [
        "Feria II",
        "Feria III",
        "Feria IV",
        "Feria V",
        "Feria VI",
        "Sabbatum",
    ]
    circumcision = day(year, 1, 1)
    cycle.extend(
        [
            [  # ! vespers
                "Circumcisio DNJC et Oct. Nativitatis",
                [3, 'd II cl'],
                {'int': 'Dum medium', 'glo': True, 'com1': 'S. Telesphori PM',
                    'cre': True, 'pre': 'et Communicantes de Nativitate'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                circumcision,
            ],
            [  # ! vespers
                "Octava S. Stephani Protomartyris",
                [18, 's'],
                {'int': 'Sederunt', 'glo': True,
                    'cre': False, 'pre': 'de Nativitate'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                circumcision + indays(1),
            ],
            [  # ! mass, vespers
                "Octava S. Joannis Ap Ev",
                [18, 's'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                circumcision + indays(2),
            ],
            [  # ! mass, vespers
                "Octava Ss Innocentium Mm.",
                [18, 's'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
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
                {'int': 'In nomine Jesu', 'glo': True,
                    'cre': True, 'pre': 'de Nativitate'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                day(year, 1, 2),
            ]
        )
    else:
        cycle.append(
            [  # ! vespers
                "Ssmi Nominis Jesu",
                [10, 'd II cl'],
                {'int': 'In nomine Jesu', 'glo': True,
                    'cre': True, 'pre': 'de Nativitate'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                circumcision-findsunday(circumcision)+week(1),
            ]
        )
        # * this is the first instance if var i
    for i, x in enumerate(("Septuagesima", "Sexagesima", "Quinquagesima")):
        if x == "Septuagesima":
            septuadate = easter(year) - week(9 - i)
        cycle.append(
            [  # ! mass, vespers
                "Dominica in " + x,
                [8, 'sd II cl'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                easter(year) - week(9 - i),
            ]
        )
    epiphany = day(year, 1, 6)
    # ! use extend:
    cycle.append(
        [  # ! mass, vespers
            "Vigilia Epiphaniæ",
            [12, 'sd Vig privil 2 cl'],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
            {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
            (False,),
            epiphany - indays(1),
        ],
    )
    cycle.append(
        [  # ! mass, vespers
            "Epiphania DNJC",
            [2, 'd I cl cum Oct privil 2 ord'],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
            {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
            (False,),
            epiphany,
        ],
    )
    cycle.append(
        [  # ! mass, vespers
            "Octava Epiphaniæ",
            [13, 'dm'],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
            {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
            (False,),
            epiphany + indays(7),
        ],
    )
    if weekday(epiphany) == "Sun":
        first_epiph = epiphany + week(1)
    else:
        first_epiph = epiphany - findsunday(epiphany) + week(1)
    for i, x in enumerate(ROMANS[0:6]):
        if weekday(epiphany + indays(i+1)) != "Sun":
            cycle.append(
                [  # ! mass, vespers
                    "Feria "
                    + ROMANS[i]
                    + " infra Oct. Epiphaniæ",
                    [9, 'feria'],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                    (False,),
                    epiphany + indays(i+1),
                ],
            )
        else:
            pass
    epiph_counter, o = first_epiph, 0
    epiph_sundays = ["I", "II", "III", "IV", "V", "VI"]  # ! use ROMANS
    while epiph_counter.strftime('%m%d') != septuadate.strftime('%m%d'):
        if epiph_sundays[o] == 'I':
            if epiph_counter == day(year, 1, 13):
                cycle.extend(
                    [
                        [  # ! vespers
                            "In Octava Epiphaniæ",
                            [13, 'dm'],
                            {'int': 'Ecce advenit', 'glo': True,
                             'cre': True, 'pre': 'et Communicantes de Epiphania'},
                            {'proper': False, 'admag': '',
                                'propers': {}, 'oration': ''},
                            (False,),
                            epiph_counter,
                        ],
                        [  # ! mass, vespers
                            "S. Familiæ Jesu, Mariæ, Joseph",
                            [11, 'dm'],
                            {'int': 'Missa', 'glo': True,
                                'cre': True, 'pre': 'Communis'},
                            {'proper': False, 'admag': '',
                                'propers': {}, 'oration': ''},
                            (False,),
                            epiph_counter - indays(1),
                        ],
                    ]
                )
            else:
                cycle.append(
                    [  # ! mass, vespers
                        "S. Familiæ Jesu, Mariæ, Joseph; Dominica " +
                        epiph_sundays[o] + " infra Oct. Epiphaniæ",
                        [11, 'dm'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        epiph_counter,
                    ]
                )
        else:
            cycle.append(
                [  # ! mass, vespers
                    "Dominica " + epiph_sundays[o] + " post Epiphaniam",
                    [12, 'sd'],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                    (False,),
                    epiph_counter,
                ]
            )
        o += 1  # ? is enumerate possible?
        epiph_counter += week(1)  # ? this is probably too complicated
    for c, x in enumerate(["I in Quadragesima", "II in Quadragesima", "III in Quadragesima", "IV in Quadragesima (Lætare)", "de Passione", "in Palmis", ]):
        if x == "I in Quadragesima":
            cycle.extend(
                [
                    [  # ! mass, vespers
                        "Dies Cinerum",
                        [3, 'feria'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) - week(6-c) - indays(4),
                    ],
                    [  # ! mass, vespers
                        "Feria V post Diem Cinerum",
                        [18, 'feria'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) - week(6-c) - indays(3),
                    ],
                    [  # ! mass, vespers
                        "Feria VI post Diem Cinerum",
                        [18, 'feria'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) - week(6-c) - indays(2),
                    ],
                    [  # ! mass, vespers
                        "Sabbatum post Diem Cinerum",
                        [18, 'feria'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) - week(6-c) - indays(1),
                    ],
                ]
            )
        cycle.append(
            [  # ! mass, vespers
                "Dominica " + x,
                [1, 'sd I cl'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                easter(year) - week(6-c),
            ]
        )
        for j, y in enumerate(feria):
            if x == "de Passione" and y == "Feria VI":
                cycle.append(
                    [  # ! mass, vespers
                        "Septem Dolorum BMV",
                        [14, 'dm'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Feria IV":
                cycle.append(
                    [  # ! mass, vespers
                        "Feria IV Quatuor Temporum Quadragesimæ",
                        [3, 'feria'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Feria VI":
                cycle.append(
                    [  # ! mass, vespers
                        "Feria VI Quatuor Temporum Quadragesimæ",
                        [3, 'feria'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Sabbatum":
                cycle.append(
                    [  # ! mass, vespers
                        "Sabbatum Quatuor Temporum Quadragesimæ",
                        [3, 'feria'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
            elif x == "in Palmis" and y == "Feria V":
                cycle.append(
                    [  # ! mass, vespers
                        y + " in Cœna Domini",
                        [2, 'd I cl'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
            elif x == "in Palmis" and y == "Feria VI":
                cycle.append(
                    [  # ! mass, vespers
                        y + " in Parasceve",
                        [2, 'd I cl'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
            elif x == "in Palmis" and y == "Sabbatum":
                cycle.append(
                    [  # ! mass, vespers
                        "Sabbatum Sanctum",
                        [2, 'd I cl'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
            elif x == "in Palmis":
                cycle.append(
                    [  # ! vespers
                        y + " Majoris Hebd",
                        [3, 'feria'],
                        {'int': 'Judica, Domine' if y == 'Feria II' else (
                            'Nos autem' if y == 'Feria III' else 'In nomine Jesu'), 'glo': False, 'cre': False, 'pre': 'de Cruce'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
            else:
                if x == "IV in Quadragesima (Lætare)":
                    new_x = re.sub("\(Lætare\)", "", x)
                else:
                    new_x = x
                cycle.append(
                    [  # ! vespers
                        y + " infra Hebd " + new_x,
                        [18, 'feria'],
                        {'int': LENT_MASSES[j-1], 'glo': False,
                            'cre': False, 'pre': 'de Quadragesima' if x != 'de Passione' else 'de Cruce'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
        i += 1  # ! we need i here to count Lent correctly -- try enumerate()
    cycle.extend(
        [
            [  # ! mass, vespers
                "Dominica Resurrectionis",
                [1, 'd I cl cum Oct privil I ord'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                easter(year)
            ],
            [  # ! mass, vespers
                "Feria II infra Oct. Paschæ",
                [2, 'd I cl'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                easter(year) + indays(1),
            ],
            [  # ! mass, vespers
                "Feria III infra Oct. Paschæ",
                [2, 'd I cl'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                easter(year) + indays(2),
            ],
            [  # ! mass, vespers
                "Feria IV infra Oct. Paschæ",
                [3, 'sd'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                easter(year) + indays(3),
            ],
            [  # ! mass, vespers
                "Feria V infra Oct. Paschæ",
                [3, 'sd'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                easter(year) + indays(4),
            ],
            [  # ! mass, vespers
                "Feria VI infra Oct. Paschæ",
                [3, 'sd'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                easter(year) + indays(5),
            ],
            [  # ! mass, vespers
                "Sabbatum in Albis",
                [3, 'sd'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                easter(year) + indays(6),
            ],
        ]
    )
    post_pent = [
        "Dominica in Albis",
        "Dominica II post Pascha",
        "Dominica III post Pascha",
        "Dominica IV post Pascha",
        "Dominica V post Pascha",
        "Dominica infra Octavam Ascensionis",
    ]
    for i, x in enumerate(post_pent, start=1):
        # // i = i+1
        if x == "Dominica II post Pascha":
            cycle.extend(
                [
                    [
                        #! mass, vespers
                        "Solemnitas S. Joseph, Sponsi BMV C. et Ecclesiæ Universalis Patroni",
                        [2, 'd I cl cum Oct Communi'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) + week(i) + indays(3),
                    ],
                    # todo We need all the days within the octave
                    [  # ! mass, vespers
                        "Octava Solemnitatis S. Joseph",
                        [13, 'dm'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
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
                        {'int': 'Exaudivit', 'glo': False,
                            'cre': False, 'pre': 'Paschalis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) + week(i) + indays(1),
                    ],
                    [  # ! vespers
                        "In Rogationibus",
                        [21, 's'],
                        {'int': 'Exaudivit', 'glo': False,
                            'cre': False, 'pre': 'Paschalis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) + week(i) + indays(2),
                    ],
                    [  # ! vespers
                        "In Rogationibus",
                        [21, 's'],
                        {'int': 'Exaudivit', 'glo': False,
                            'cre': False, 'pre': 'Paschalis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) + week(i) + indays(3),
                    ],
                    [  # ! mass, vespers
                        "Vigilæ Ascensionis",
                        [18, 'feria'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) + week(i) + indays(3),
                    ],
                    [  # ! vespers
                        "Ascensio DNJC",
                        [2, 'd I cl cum Oct privil 3 ord'],
                        {'int': 'Viri Galilæi', 'glo': True,
                            'cre': True, 'pre': 'et Communicantes de Ascensione'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) + week(i) + indays(4),
                    ],
                    [  # ! vespers
                        "Oct. Ascensionis DNJC",
                        [13, 'dm'],
                        {'int': 'Viri Galilæi', 'glo': True,
                            'cre': True, 'pre': 'et Communicantes de Ascensione'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        easter(year) + week(i) + indays(4+7),
                    ],
                ]
            )
            ascension_day = easter(year) + week(i) + indays(5)
        if x == "Dominica infra Octavam Ascensionis":
            j = 0  # ! FIXME
            for y in ROMANS[1:6]:
                # pass if the day w/in the octave is a sunday
                if (ascension_day + indays(j + 1)) == (easter(year) + week(i)):
                    pass
                elif (ascension_day + indays(j + 1)).strftime("%A") == "Saturday":
                    cycle.append(
                        [  # ! mass, vespers
                            "Sabbatum infra Oct. Ascensionis",
                            [16, 'sd'],
                            {'int': 'Missa', 'glo': True,
                                'cre': True, 'pre': 'Communis'},
                            {'proper': False, 'admag': '',
                                'propers': {}, 'oration': ''},
                            (False,),
                            ascension_day + indays(j + 1),
                        ]
                    )
                else:
                    cycle.append(
                        [  # ! mass, vespers
                            "Feria " + y + " infra Oct. Ascensionis",
                            [16, 'sd'],
                            {'int': 'Missa', 'glo': True,
                                'cre': True, 'pre': 'Communis'},
                            {'proper': False, 'admag': '',
                                'propers': {}, 'oration': ''},
                            (False,),
                            ascension_day + indays(j + 1),
                        ]
                    )
                j += 1
        if x == "Dominica in Albis":
            cycle.append(
                [  # ! mass, vespers
                    x,
                    [1, 'dm'],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                    (False,),
                    easter(year) + week(i)
                ]
            )
        else:
            cycle.append(
                [  # ! mass, vespers
                    x,
                    [12, 'sd'],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                    (False,),
                    easter(year) + week(i)
                ]
            )
    pent_date = easter(year) + week(i+1)
    cycle.extend(
        [
            [  # ! mass, vespers
                "Vigilia Pentecostes",
                [3, 'd I cl Vig privil I cl'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                pent_date - indays(1),
            ],
            [  # ! mass, vespers
                "Dominica Pentecostes",
                [1, 'd I cl cum Oct privil I ord'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                pent_date,
            ],
        ]
    )
    for j, y in enumerate(ROMANS[1:6]):
        if y == "II" or y == "III":
            cycle.append(
                [  # ! mass, vespers
                    "Feria " + y + " infra Oct. Pentecostes",
                    [2, 'd I cl'],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                    (False,),
                    pent_date + indays(j + 1),
                ]
            )
        else:
            cycle.append(
                [  # ! mass, vespers
                    "Feria " + y + " infra Oct. Pentecostes",
                    [3, 'sd'],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                    (False,),
                    pent_date + indays(j + 1),
                ]
            )
    cycle.extend(
        [
            [  # ! mass, vespers
                "Sabbatum infra Oct. Pentecostes",
                [3, 'sd'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                pent_date + indays(j + 2),
            ],
            [  # ! mass, vespers
                "Feria IV Quatuor Temporum infra Oct. Pentecostes",
                [18, 'feria'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                easter(year) + week(i) + indays(3),
            ],
            [  # ! mass, vespers
                "Feria VI Quatuor Temporum infra Oct. Pentecostes",
                [18, 'feria'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                easter(year) + week(i) + indays(5),
            ],
            [  # ! mass, vespers
                "Sabbatum Quatuor Temporum infra Oct. Pentecostes",
                [18, 'feria'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                easter(year) + week(i) + indays(6),
            ],
        ]
    )
    i += 1
    prelim_pents = [
        [  # ! mass, vespers
            "Festum Sanctissimæ Trinitatis",
            [2, 'd I cl'],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
            {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
            (False,),
        ],
        [  # ! mass, vespers
            "Dominica infra Oct. Ssmi Corporis Christi (Dominica II post Pentecosten)",
            [12, 'sd'],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
            {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
            (False,),
        ],
        [  # ! mass, vespers
            "Dominica infra Oct. Ssmi Cordis DNJC (Dominica III post Pentecosten)",
            [12, 'sd'],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
            {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
            (False,),
        ],
    ]
    for l, x in enumerate(prelim_pents):
        if x[0] == "Dominica infra Oct. Ssmi Corporis Christi (Dominica II post Pentecosten)":
            corpus_christi = pent_date + week(2) - indays(3)
            for j, y in enumerate(ROMANS[1:7]):
                if (corpus_christi + indays(j+1)) == (pent_date + week(2)):
                    pass
                else:
                    feria_index = int(
                        (corpus_christi+indays(j+1)).strftime("%w"))-1
                    fer_num = feria[feria_index]
                    cycle.append(
                        [
                            fer_num + " infra Oct. Ssmi Corporis Christi",
                            [9, 'sd'],
                            {'int': 'Missa', 'glo': True,
                                'cre': True, 'pre': 'Communis'},
                            {'proper': False, 'admag': '',
                                'propers': {}, 'oration': ''},
                            (False,),
                            corpus_christi + indays(j + 1),
                        ]
                    )
            cycle.append(
                [  # ! mass, vespers
                    "Sanctissimi Corporis Christi",
                    [2, 'd I cl cum Oct privil 2 ord'],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                    (False,),
                    corpus_christi,
                ]
            )
            cycle.append(
                [  # ! mass, vespers
                    "Octava Ssmi Corporis Christi",
                    [4, 'dm'],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                    (False,),
                    corpus_christi + week(1),
                ]
            )
        if x[0] == "Dominica infra Oct. Ssmi Cordis DNJC (Dominica III post Pentecosten)":
            ssmi_cordis = pent_date + week(3) - indays(2)
            for j, y in enumerate(ROMANS[1:7]):
                if ssmi_cordis + indays(j + 1) == pent_date + week(3):
                    pass
                else:
                    feria_index = int(
                        (ssmi_cordis + indays(j + 1)).strftime("%w")) - 1
                    fer_num = feria[feria_index]
                    cycle.append(
                        [  # ! mass, vespsers
                            fer_num + " infra Oct. Ssmi Cordis DNJC",
                            # ? is this supposed to be within a common octave?
                            [17, 'sd'],
                            {'int': 'Missa', 'glo': True,
                                'cre': True, 'pre': 'Communis'},
                            {'proper': False, 'admag': '',
                                'propers': {}, 'oration': ''},
                            (False,),
                            ssmi_cordis + indays(j + 1),
                        ]
                    )
            cycle.extend(
                [
                    [  # ! mass, vespers
                        "Sacratissimi Cordis Jesu",
                        [2, 'd I cl cum Oct privil 3 ord'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (1, 0, 3, 1, 1, 0),
                        ssmi_cordis,
                    ],
                    [  # ! mass, vespers
                        "Octava Sacratissimi Cordis Jesu",
                        [13, 'dm'],
                        {'int': 'Missa', 'glo': True,
                            'cre': True, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        ssmi_cordis + week(1),
                    ],
                ]
            )
        cycle.append([x[0], x[1], x[2], x[3], x[4], pent_date + week(l+1)])
        i += 1  # ? does this have any purpose here?
    sept_counter = 0  # ? is enumerate possible here?
    for p, x in enumerate(ROMANS[3:-1]):
        post_pent_count = pent_date + week(4)
        earliest_first_advent = str(year) + "-12-03"
        if post_pent_count + week(p) >= datetime.strptime(
            earliest_first_advent, "%Y-%m-%d"
        ):
            break
        else:
            # todo add all the ferias during Pentecost
            cycle.append(
                [  # ! mass, vespers
                    "Dominica " + x + " post Pentecosten",
                    [12, 'sd'],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                    (False,),
                    post_pent_count + week(p),
                ]
            )
            if (post_pent_count + week(p)).strftime("%B") == "September":
                if int((post_pent_count + week(p)).strftime("%d")) <= 3:
                    sept_counter += 0
                else:
                    sept_counter += 1
            if sept_counter == 3:
                cycle.extend(
                    [
                        [  # ! mass, vespers
                            "Feria IV Quatuor Temporum Septembris",
                            [18, 'feria'],
                            {'int': 'Missa', 'glo': True,
                             'cre': True, 'pre': 'Communis'},
                            {'proper': False, 'admag': '',
                                'propers': {}, 'oration': ''},
                            (False,),
                            post_pent_count + week(p) + indays(3),
                        ],
                        [  # ! mass, vespers
                            "Feria VI Quatuor Temporum Septembris",
                            [18, 'feria'],
                            {'int': 'Missa', 'glo': True,
                             'cre': True, 'pre': 'Communis'},
                            {'proper': False, 'admag': '',
                                'propers': {}, 'oration': ''},
                            (False,),
                            post_pent_count + week(p) + indays(5),
                        ],
                        [  # ! mass, vespers
                            "Sabbatum Quatuor Temporum Septembris",
                            [18, 'feria'],
                            {'int': 'Missa', 'glo': True,
                             'cre': True, 'pre': 'Communis'},
                            {'proper': False, 'admag': '',
                                'propers': {}, 'oration': ''},
                            (False,),
                            post_pent_count + week(p) + indays(6),
                        ],
                    ]
                )

            if (post_pent_count + week(p)).strftime("%B") == "November" and (easter(year) + week(i-1)).strftime("%B") == "October":
                # if the current Sunday is in November and the previous Sunday is in October
                christ_king = post_pent_count + week(p) - week(1)
                cycle.append(
                    [  # ! vespers
                        'In Festo DNJC Regis',
                        [2, 'd I cl'],
                        {'int': 'Dignus est', 'glo': True,
                            'cre': True, 'pre': 'de DNJC Rege'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        christ_king,
                    ],
                )
            i += 1
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
    for i, x in enumerate(advents):
        if x == "Dominica III Adventus":
            cycle.extend(
                [
                    [  # ! vespers
                        x,
                        [8, 'sd II cl'],
                        {'int': 'Populus Sion' if x == "Dominica II Adventus" else (
                            'Gaudete' if x == "Dominica III Adventus" else 'Rorate cæli'), 'glo': False, 'cre': True, 'pre': 'de Trinitate'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        lastadvent - week(i)
                    ],
                    [  # ! vespers
                        "Feria IV Quatuor Temporum in Adventus",
                        [18, 'feria'],
                        {'int': 'Rorate cæli', 'glo': False,
                            'cre': False, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        lastadvent - week(i) + indays(3),
                    ],
                    [  # ! vespers
                        "Feria VI Quatuor Temporum in Adventus",
                        [18, 'feria'],
                        {'int': 'Prope es tu', 'glo': False,
                            'cre': False, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        lastadvent - week(i) + indays(5),
                    ],
                    [  # ! vespers
                        "Sabbatum Quatuor Temporum in Adventus",
                        [18, 'feria'],
                        {'int': 'Veni, et ostende', 'glo': False,
                            'cre': False, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        (False,),
                        lastadvent - week(i) + indays(6),
                    ],
                ]
            )
        elif x == "Dominica I Adventus":
            cycle.append(
                [  # ! vespers
                    x,
                    [1, 'sd'],
                    {'int': 'Ad te levavi', 'glo': False,
                        'cre': True, 'pre': 'de Trinitate'},
                    {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                    (False,),
                    lastadvent - week(i)
                ]
            )
        else:
            cycle.append(
                [  # ! vespers
                    x,
                    [8, 'sd II cl'],
                    {'int': 'Populus Sion' if x == "Dominica II Adventus" else (
                        'Gaudete' if x == "Dominica III Adventus" else 'Rorate cæli'),
                     'glo': False, 'cre': True, 'pre': 'de Trinitate'},
                    {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                    (False,),
                    lastadvent - week(i)
                ]
            )
    cycle.extend([
        [  # ! vespers
            "Vigilia Nativitas DNJC",
            [3, 'd I cl Vig privil I cl'],
            {'int': 'Hodie scietis', 'glo': False,
                'cre': False, 'pre': 'Communis'},
            {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
            (False,),
            christmas - indays(1)
        ],  # TODO If the vigil is a Sunday, there is a commemoration, Creed, de Trinitate, but no Proper Last Gospel
        [  # ! vespers
            "Nativitas DNJC",
            [2, 'd I cl cum Oct privil 3 ord'],
            {
                'Ad Primam Missam': {'int': 'Domine dixit', 'glo': True, 'cre': True, 'pre': 'et Communicantes (in hac Missa tantum dicitur "noctem") de Nativitate'},
                'Ad Secundam Missam': {'int': 'Lux fulgebit', 'glo': True, 'cre': True, 'pre': 'et Communicantes de Nativitate'},
                'Ad Tertiam Missam': {'int': 'Puer natus', 'glo': True, 'cre': True, 'pre': 'et Communicantes de Nativitate'},
            },
            {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
            (False,),
            christmas
        ],
    ]
    )
    if 5 <= int(christmas.strftime("%u")) <= 7 or christmas.strftime("%u") == 1:
        # todo this can be simplified
        cycle.append(
            [  # ! mass, vespers
                "Dominica Infra Octavam Nativitatis reposita",
                [12, 'sd'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                christmas + indays(5),
            ]
        )
    else:
        cycle.append(
            [  # ! vespers
                "Dominica Infra Octavam Nativitatis",
                [12, 'sd'],
                {'int': 'Dum medium', 'glo': True, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                christmas + indays(7) - findsunday(christmas),
            ]
        )
    if (
        int(day(year, 12, 30).strftime("%u")) == 1
        or int(day(year, 12, 30).strftime("%u")) == 7
    ):
        cycle.append(
            [  # ! mass, vespers
                "Feria VI infra Octavam Nativitatis",
                [16, 'sd'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                christmas + indays(5),
            ]
        )
    cycle.extend(
        [
            [  # ! vespers
                "S. Stephani Protomartyris",
                [10, 'd II cl cum Oct simplici'],
                {'int': 'Sederunt', 'glo': True, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                christmas + indays(1),
            ],
            [  # ! vespers
                "S. Joannis Ap. Ev.",
                [10, 'd II cl cum Oct simplici'],
                {'int': 'In medio ecclesiæ', 'glo': True, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                christmas + indays(2),
            ],
            [  # ! vespers
                "Ss Innocentium Mm.",
                [10, 'd II cl cum Oct simplici'],
                {'int': 'Ex ore infantium', 'glo': True, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                christmas + indays(3),
            ],
            [  # ! vespers
                "S. Thomæ E.M.",
                [15, 'd'],
                {'int': 'Gaudeamus omnes', 'glo': True, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                christmas + indays(4),
            ],
            [  # ! mass, vespers
                "S. Silvestri I P.C.",
                [15, 'd'],
                {'int': 'Missa', 'glo': True, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                {'proper': False, 'admag': '', 'propers': {}, 'oration': ''},
                (False,),
                christmas + indays(6),
            ],
        ]
    )

    def make_dict(year: int):
        gen_file = "temporal/temporal_" + str(year)
        with open(gen_file + ".py", "w") as f:
            f.write("temporal = {")
            keylist = ['feast', 'rank', 'mass', 'vespers']
            keylist_alt = ['feast', 'rank', 'mass', 'vespers', 'nobility']
            memory = []
            for row in cycle:
                temporal_event = row[-1].strftime("%m/%d")
                if temporal_event in memory:
                    temporal_event += "."
                memory.append(temporal_event)
                print(row[0]+' has the "nobility" key')
                mini_dict = str(
                    dict(
                        zip(
                            keylist_alt,
                            [
                                row[0],
                                row[1],
                                row[2],
                                row[3],
                                row[4],
                            ],
                        )
                    )
                )
                f.write(
                    str("\n'" + temporal_event + "'" + ": " + mini_dict + ",")
                )
            f.write("}")
        dict_clean("temporal.temporal_", year)
    make_dict(year)


def app(year: int, diocese: str):
    build_temporal(year)
    stitch(year, diocese)
    dict_clean("calen.calendar_", year)
    latex_full_cal_test(year)


# 2024 is a leap year
app(year=2022, diocese="roman")
