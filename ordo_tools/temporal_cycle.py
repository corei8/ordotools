import re
from datetime import datetime
from ordo_tools.ordo_tools import *


def build_temporal(year):
    year = int(year)
    cycle = []
    # ? maybe get rid of this ?
    circumcision = day(year, 1, 1)
    cycle.extend(
        [
            [  # ! vespers
                "Circumcisio DNJC et Oct. Nativitatis",
                [3, 'd II cl'],
                {'feast': 'S. Telesphori PM'},
                {'int': 'Puer natus', 'glo': True, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                circumcision,
            ],
            [  # ! vespers
                "Octava S. Stephani Protomartyris",
                [18, 's'],
                {'int': 'Sederunt', 'glo': True,
                    'cre': False, 'pre': 'de Nativitate'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                circumcision + indays(1),
            ],
            [  # ! vespers
                "Octava S. Joannis Ap Ev",
                [18, 's'],
                {'int': 'Introit', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                circumcision + indays(2),
            ],
            [  # ! vespers
                "Octava Ss Innocentium Mm.",
                [18, 's'],
                {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
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
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
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
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
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
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                easter(year) - week(9 - i),
            ]
        )
    epiphany = day(year, 1, 6)
    # ! use extend:
    cycle.append(
        [  # ! vespers
            "Vigilia Epiphaniæ",
            [12, 'sd Vig privil 2 cl'],
            {'int': 'Dum medium silentium', 'glo': True,
                'cre': True, 'pre': 'de Nativitate'},
            {'proper': False, 'admag': [
                'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
            False,
            (False,),
            epiphany - indays(1),
        ],
    )
    cycle.append(
        [  # ! vespers
            "Epiphania DNJC",
            [2, 'd I cl cum Oct privil 2 ord'],
            {'int': 'Ecce advenit', 'glo': True,
                'cre': True, 'pre': 'de Epiphania'},
            {'proper': False, 'admag': [
                'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
            False,
            (False,),
            epiphany,
        ],
    )
    cycle.append(
        [  # ! mass, vespers
            "Octava Epiphaniæ",
            [13, 'dm'],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
            {'proper': False, 'admag': [
                'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
            False,
            (False,),
            epiphany + indays(7),
        ],
    )
    if weekday(epiphany) == "Sun":
        first_epiph = epiphany + week(1)
    else:
        first_epiph = epiphany - findsunday(epiphany) + week(1)
    epiphany_sundays_counter = 1
    for i, x in enumerate(ROMANS[0:6]):
        if weekday(epiphany + indays(i+1)) != "Sun":
            cycle.append(
                [  # ! mass, vespers
                    "De "
                    + ROMANS[i+1]
                    + " die infra Oct. Epiphaniæ",
                    [9, 'feria'],
                    {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    {'proper': False, 'admag': [
                        'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                    False,
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
                             'cre': True, 'pre': 'et Comm de Epiphania'},
                            {'proper': False, 'admag': '',
                                'propers': {}, 'oration': ''},
                            False,
                            (False,),
                            epiph_counter,
                        ],
                        [  # ! vespers
                            "S. Familiæ Jesu, Mariæ, Joseph",
                            [11, 'dm'],
                            {'int': 'Exultat', 'glo': True,
                                'cre': True, 'pre': 'et communcantes de Epiphania'},
                            {'proper': False, 'admag': '',
                                'propers': {}, 'oration': ''},
                            False,
                            (False,),
                            epiph_counter - indays(1),
                        ],
                    ]
                )
            else:
                cycle.append(
                    [  # !  vespers
                        "S. Familiæ Jesu, Mariæ, Joseph; Dominica " +
                        epiph_sundays[o] + " infra Oct. Epiphaniæ",
                        [11, 'dm'],
                        {'int': 'In excelso', 'glo': True,
                            'cre': True, 'pre': 'et Comm de Epiphania'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        epiph_counter,
                    ]
                )
        else:
            cycle.append(
                [  # ! vespers
                    "Dominica " + epiph_sundays[o] + " post Epiphaniam",
                    [12, 'sd'],
                    {'int': 'Omnis terra', 'glo': True,
                        'cre': True, 'pre': 'de Ssma Trinitate'},
                    {'proper': False, 'admag': [
                        'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                    False,
                    (False,),
                    epiph_counter,
                ]
            )
            epiphany_sundays_counter += 1
        o += 1  # ? is enumerate possible?
        epiph_counter += week(1)  # ? this is probably too complicated
    for c, x in enumerate(["I in Quadragesima", "II in Quadragesima", "III in Quadragesima", "IV in Quadragesima (Lætare)", "de Passione", "in Palmis", ]):
        if x == "I in Quadragesima":
            cycle.extend(
                [
                    [  # ! vespers
                        "Dies Cinerum",
                        [3, 's I cl'],
                        {'int': 'Misereris', 'glo': True,
                            'cre': True, 'pre': 'de Quadragesima'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        easter(year) - week(6-c) - indays(4),
                    ],
                    [  # ! mass, vespers
                        "Feria V post Diem Cinerum",
                        [18, 's'],
                        {'int': 'Dum clamarem', 'glo': False,
                            'cre': False, 'pre': 'de Quadragesima'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        easter(year) - week(6-c) - indays(3),
                    ],
                    [  # ! vespers
                        "Feria VI post Diem Cinerum",
                        [18, 's'],
                        {'int': 'Audivit', 'glo': False,
                            'cre': False, 'pre': 'de Quadragesima'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        easter(year) - week(6-c) - indays(2),
                    ],
                    [  # ! mass, vespers
                        "Sabbatum post Diem Cinerum",
                        [18, 's'],
                        {'int': 'Audivit', 'glo': False,
                            'cre': False, 'pre': 'de Quadragesima'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        easter(year) - week(6-c) - indays(1),
                    ],
                ]
            )
        cycle.append(
            [  # ! mass, vespers
                "Dominica " + x,
                [1, 'sd I cl'],
                {'int': 'Missa', 'glo': False, 'cre': True, 'pre': 'de Quadragesima'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                easter(year) - week(6-c),
            ]
        )
        for j, y in enumerate(FERIA):
            if x == "de Passione" and y == "Feria VI":
                cycle.append(
                    [  # ! vespers
                        "Septem Dolorum BMV",
                        [14, 'dm'],
                        {'int': 'Stabant', 'glo': False, 'seq': 'Stabat Mater',
                            'cre': True, 'pre': 'de B. Maria Virg.'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Feria IV":
                cycle.append(
                    [  # ! vespers
                        "Feria IV Quatuor Temporum Quadragesimæ",
                        [3, 's'],
                        {'int': 'Reminiscere', 'glo': False,
                            'cre': False, 'pre': 'de Quadragesima'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Feria VI":
                cycle.append(
                    [  # ! vespers
                        "Feria VI Quatuor Temporum Quadragesimæ",
                        [3, 's'],
                        {'int': 'De necessitatibus', 'glo': False,
                            'cre': False, 'pre': 'de Quadragesima'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
            elif x == "I in Quadragesima" and y == "Sabbatum":
                cycle.append(
                    [  # ! vespers
                        "Sabbatum Quatuor Temporum Quadragesimæ",
                        [3, 's'],
                        {'int': 'Intret', 'glo': False,
                            'cre': False, 'pre': 'de Quadragesima'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
            elif x == "in Palmis" and y == "Feria V":
                cycle.append(
                    [  # ! vespers
                        y + " in Cœna Domini",
                        [2, 'd I cl'],
                        {'int': 'Nos autem', 'glo': True,
                            'cre': False, 'pre': 'de Cruce'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
            elif x == "in Palmis" and y == "Feria VI":
                cycle.append(
                    [  # ! vespers
                        y + " in Parasceve",
                        [2, 'd I cl'],
                        {'int': 'Haec dicit', 'glo': False,
                            'cre': False, 'pre': ''},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
            elif x == "in Palmis" and y == "Sabbatum":
                cycle.append(
                    [  # ! mass, vespers
                        "Sabbatum Sanctum",
                        [2, 'd I cl'],
                        {'int': 'In Missa', 'glo': True,
                            'cre': False, 'pre': 'Te quidem'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
            elif x == "in Palmis":
                cycle.append(
                    [  # ! vespers
                        y + " Majoris Hebd",
                        [3, 's'],
                        {'int': 'Judica, Domine' if y == 'Feria II' else (
                            'Nos autem' if y == 'Feria III' else 'In nomine Jesu'), 'glo': False, 'cre': False, 'pre': 'de Cruce'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
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
                        [18, 'sd I cl'],
                        {'int': LENT_MASSES[j-1], 'glo': False,
                            'cre': False, 'pre': 'de Quadragesima' if x != 'de Passione' else 'de Cruce'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        easter(year) - week(6-c) + indays(j+1),
                    ]
                )
        i += 1  # ! we need i here to count Lent correctly -- try enumerate()
    cycle.extend(
        [
            [  # !  vespers
                "Dominica Resurrectionis",
                [1, 'd I cl cum Oct privil I ord'],
                {'int': 'Ressurexi', 'glo': True, 'seq': 'Victimae paschali laudes',
                    'cre': True, 'pre': 'Paschalis'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                easter(year)
            ],
            [  # ! vespers
                "Feria II infra Oct. Paschæ",
                [2, 'd I cl'],
                {'int': 'Introduxit', 'glo': True, 'seq': 'Victimae paschali laudes',
                    'cre': True, 'pre': 'et communicantes et Hanc Igitur, ut in die Paschae'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                easter(year) + indays(1),
            ],
            [  # ! vespers
                "Feria III infra Oct. Paschæ",
                [2, 'd I cl'],
                {'int': 'Aqua sapientiae', 'glo': True, 'seq': 'Victimae paschali laudes',
                    'cre': True, 'pre': 'et communicantes et Hanc Igitur, ut in die Paschae'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                easter(year) + indays(2),
            ],
            [  # ! vespers
                "Feria IV infra Oct. Paschæ",
                [3, 'sd'],
                {'int': 'Venite', 'glo': True, 'seq': 'Victimae paschali laudes',
                    'cre': True, 'pre': 'et Communicantes et Hanc Igitur, ut in die Paschae'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                easter(year) + indays(3),
            ],
            [  # ! vespers
                "Feria V infra Oct. Paschæ",
                [3, 'sd'],
                {'int': 'Victricem', 'glo': True, 'seq': 'Victimae paschali laudes',
                    'cre': True, 'pre': 'et Communicantes et Hang Igitur, ut in die Paschae'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                easter(year) + indays(4),
            ],
            [  # ! vespers
                "Feria VI infra Oct. Paschæ",
                [3, 'sd'],
                {'int': 'Eduxit eos', 'glo': True, 'seq': 'Victimae paschali laudes',
                    'cre': True, 'pre': 'et Communicantes et Hanc Igitur, ut in die Paschae'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                easter(year) + indays(5),
            ],
            [  # ! vespers
                "Sabbatum in Albis",
                [3, 'sd'],
                {'int': 'Eduxit Dominus', 'glo': True, 'seq': 'Victimae paschali laudes',
                    'cre': True, 'pre': 'et Communicantes et Hanc Igitur, ut in die Paschae'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
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
                        False,
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
                        False,
                        (False,),
                        easter(year) + week(i + 1) + indays(3),
                    ],
                ]
            )
        if x == "Dominica V post Pascha":
            cycle.extend(
                [
                    [  # ! vespers
                        "Feria II in Rogationibus",
                        [18, 'feria'],
                        {'int': 'Exaudivit', 'glo': False,
                            'cre': True, 'pre': 'Paschalis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (0, 0, 0, 13, 0, 0,),
                        easter(year) + week(i) + indays(1),
                    ],
                    [  # ! vespers
                        "Feria III in Rogationibus",
                        [18, 'feria'],
                        {'int': 'Exaudivit', 'glo': False,
                            'cre': True, 'pre': 'Paschalis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (0, 0, 0, 13, 0, 0,),
                        easter(year) + week(i) + indays(2),
                    ],
                    [  # ! vespers
                        "Feria IV in Rogationibus in Vigilia Ascensionis ",
                        [18, 'feria'],
                        {'int': 'Exaudivit', 'glo': False,
                            'cre': True, 'pre': 'Paschalis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (9, 2, 6, 13, 3, 0,),
                        easter(year) + week(i) + indays(3),
                    ],
                    [  # ! vespers
                        "Ascensio DNJC",
                        [2, 'd I cl cum Oct privil 3 ord'],
                        {'int': 'Viri Galilæi', 'glo': True,
                            'cre': True, 'pre': 'et Comm de Ascensione'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        easter(year) + week(i) + indays(4),
                    ],
                    [  # ! vespers
                        "Oct. Ascensionis DNJC",
                        [13, 'dm'],
                        {'int': 'Viri Galilæi', 'glo': True,
                            'cre': True, 'pre': 'et Comm de Ascensione'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        easter(year) + week(i) + indays(4+7),
                    ],
                ]
            )
            ascension_day = easter(year) + week(i) + indays(5)
        if x == "Dominica infra Octavam Ascensionis":
            for j, y in enumerate(ROMANS[1:6], start=1):
                if ascension_day + indays(j) == easter(year) + week(i):
                    continue
                elif (ascension_day + indays(j)).strftime("%A") == "Saturday":
                    cycle.append(
                        [  # ! vespers
                            "Sabbatum infra Oct. Ascensionis",
                            [16, 'sd'],
                            {'int': 'Missa', 'glo': True,
                                'cre': False, 'pre': 'de Ascensione'},
                            {'proper': False, 'admag': '',
                                'propers': {}, 'oration': ''},
                            False,
                            (False,),
                            ascension_day + indays(j),
                        ]
                    )
                else:
                    cycle.append(
                        [  # ! vespers
                            "De " + y + " die infra Oct. Ascensionis",
                            [16, 'sd'],
                            {'int': 'Viri galilaei', 'glo': True,
                                'cre': False, 'pre': 'de Ascensione'},
                            {'proper': False, 'admag': '',
                                'propers': {}, 'oration': ''},
                            False,
                            (False,),
                            ascension_day + indays(j),
                        ]
                    )
        if x == "Dominica in Albis":
            cycle.append(
                [  # ! vespers
                    x,
                    [1, 'dm'],
                    {'int': 'Quasi modo', 'glo': True,
                        'cre': True, 'pre': 'Paschalis'},
                    {'proper': False, 'admag': [
                        'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                    False,
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
                    {'proper': False, 'admag': [
                        'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                    False,
                    (False,),
                    easter(year) + week(i)
                ]
            )
    pent_date = easter(year) + week(i+1)
    cycle.extend(
        [
            [  # ! vespers
                "Sabbatum Vigilia Pentecostes",
                [3, 'd I cl Vig privil I cl'],
                {'int': 'Cum sanctificatus', 'glo': True, 'cre': False,
                    'pre': 'et Communicantes et Hanc Igitur de Pentecoste'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                pent_date - indays(1),
            ],
            [  # ! vespers
                "Dominica Pentecostes",
                [1, 'd I cl cum Oct privil I ord'],
                {'int': 'Spiritus Domini', 'glo': True, 'seq': 'Veni, Sancte Spiritus',
                    'cre': True, 'pre': 'et Communicantes et Hanc Igitur de Pentecoste'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                pent_date,
            ],
        ]
    )
    for j, y in enumerate(ROMANS[1:6]):
        if y == "II" or y == "III":
            cycle.append(
                [  # ! vespers
                    "Feria " + y + " infra Oct. Pentecostes",
                    [2, 'd I cl'],
                    {'int': 'Cibavit eos', 'glo': True, 'cre': True, 'seq': 'Veni, Sancte Spiritus',
                        'pre': 'et Communicantes et Hanc Igitur de Pentecoste'},
                    {'proper': False, 'admag': [
                        'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                    False,
                    (False,),
                    pent_date + indays(j + 1),
                ]
            )
        else:
            cycle.append(
                [  # ! mass, vespers
                    "Feria " + y + " infra Oct. Pentecostes",
                    [3, 'd I cl'],
                    {'int': 'Accepite jucunditatem', 'glo': True, 'seq': 'Veni, Sancte Spiritus',
                        'cre': True, 'pre': 'et Communicantes et Hanc Igitur de Pentecoste'},
                    {'proper': False, 'admag': [
                        'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                    False,
                    (False,),
                    pent_date + indays(j + 1),
                ]
            )
    cycle.extend(
        [
            [  # ! mass, vespers
                "Sabbatum infra Oct. Pentecostes",
                [3, 'sd'],
                {'int': 'Missa', 'glo': True, 'seq': 'Veni, Sancte Spiritus',
                    'cre': True, 'pre': 'Communis'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                pent_date + indays(j + 2),
            ],
            [  # ! vespers
                "Feria IV Quatuor Temporum infra Oct. Pentecostes",
                [18, 'sd'],
                {'int': 'Deus, dum egredereris', 'glo': True, 'seq': 'Veni, Sancte Spiritus',
                    'cre': True, 'pre': 'et Communicantes et Hanc Igitur de Pentecoste'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                easter(year) + week(i) + indays(3),
            ],
            [  # ! vespers
                "Feria VI Quatuor Temporum infra Oct. Pentecostes",
                [18, 'sd'],
                {'int': 'Repleatur os meum', 'glo': True, 'seq': 'Veni, Sancte Spiritus',
                    'cre': True, 'pre': 'et Communicantes et Hanc Igitur de Pentecoste'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                easter(year) + week(i) + indays(5),
            ],
            [  # ! vespers
                "Sabbatum Quatuor Temporum infra Oct. Pentecostes",
                [18, 'sd'],
                {'int': 'Caritas Dei', 'glo': True, 'seq': 'Veni, Sancte Spiritus',
                    'cre': True, 'pre': 'et Communicantes et Hanc Igitur de Pentecoste'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                easter(year) + week(i) + indays(6),
            ],
        ]
    )
    i += 1
    prelim_pents = [
        [  # ! vespers
            "Festum Sanctissimæ Trinitatis",
            [2, 'd I cl'],
            {'int': 'Benedicta sit', 'glo': True,
                'cre': True, 'pre': 'de Ssma Trinitate'},
            {'proper': False, 'admag': [
                'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
            False,
            (False,),
        ],
        [  # ! vespers
            "Dominica infra Oct. Ssmi Corporis Christi (Dominica II post Pentecosten)",
            [12, 'sd'],
            {'int': 'Factus est', 'glo': True, 'seq': 'Lauda, Sion, Salvatorem',
                'cre': True, 'pre': 'de Nativitate, vel de Ssma Trinitate'},
            {'proper': False, 'admag': [
                'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
            False,
            (False,),
        ],
        [  # ! mass, vespers
            "Dominica infra Oct. Ssmi Cordis DNJC (Dominica III post Pentecosten)",
            [12, 'sd'],
            {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
            {'proper': False, 'admag': [
                'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
            False,
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
                    fer_num = FERIA[feria_index]
                    cycle.append(
                        [
                            fer_num + " infra Oct. Ssmi Corporis Christi",
                            [9, 'sd'],
                            {'int': 'Missa', 'glo': True, 'seq': 'Lauda, Sion, Salvatorem',
                                'cre': True, 'pre': 'Communis'},
                            {'proper': False, 'admag': '',
                                'propers': {}, 'oration': ''},
                            False,
                            (False,),
                            corpus_christi + indays(j + 1),
                        ]
                    )
            cycle.append(
                [  # ! vespers
                    "Sanctissimi Corporis Christi",
                    [2, 'd I cl cum Oct privil 2 ord'],
                    {'int': 'Cibavit eos', 'glo': True, 'seq': 'Lauda, Sion',
                        'cre': True, 'pre': 'de Nativitate'},
                    {'proper': False, 'admag': [
                        'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                    False,
                    (False,),
                    corpus_christi,
                ]
            )
            cycle.append(
                [  # ! vespers
                    "Octava Ssmi Corporis Christi",
                    [4, 'dm'],
                    {'int': 'Cibavit eos', 'glo': True, 'seq': 'Lauda, Sion',
                        'cre': True, 'pre': 'de Nativitate'},
                    {'proper': False, 'admag': [
                        'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                    False,
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
                    fer_num = FERIA[feria_index]
                    cycle.append(
                        [  # ! mass, vespsers
                            fer_num + " infra Oct. Ssmi Cordis DNJC",
                            # ? is this supposed to be within a common octave?
                            [17, 'sd'],
                            {'int': 'Respice in me', 'glo': True,
                                'cre': True, 'pre': 'de Ssmo Corde Iesu vel de Ssma Trinitate'},
                            {'proper': False, 'admag': '',
                                'propers': {}, 'oration': ''},
                            False,
                            (False,),
                            ssmi_cordis + indays(j + 1),
                        ]
                    )
            cycle.extend(
                [
                    [  # ! mass, vespers
                        "Sacratissimi Cordis Jesu",
                        [2, 'd I cl cum Oct privil 3 ord'],
                        {'int': 'Cogitationes', 'glo': True,
                            'cre': True, 'pre': 'de Ssmo Corde Iesu'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (1, 0, 3, 1, 1, 0),
                        ssmi_cordis,
                    ],
                    [  # ! mass, vespers
                        "Octava Sacratissimi Cordis Jesu",
                        [13, 'dm'],
                        {'int': 'Cogitationes', 'glo': True,
                            'cre': True, 'pre': 'de Ssmo Corde Iesu'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        ssmi_cordis + week(1),
                    ],
                ]
            )
        cycle.append([x[0], x[1], x[2], x[3], x[4],
                     x[5], pent_date + week(l+1)])
        i += 1  # ? does this have any purpose here?
    sept_counter = 0  # ? is enumerate possible here?
    christmas = datetime.strptime(str(year) + "-12-25", "%Y-%m-%d")
    lastadvent = christmas - findsunday(christmas)
    post_pent_sundays = int((((lastadvent - week(4))-pent_date)/7).days)-1
    post_pent_count = pent_date + week(4)
    epiph_sunday_overflow = ROMANS[6-find_extra_epiphany(
        post_pent_sundays): find_extra_epiphany(post_pent_sundays)+2]
    for count, x in enumerate(ROMANS[3:post_pent_sundays+1], start=1):
        p = count - 1
        if count <= 20:
            cycle.append(
                [  # ! vespers
                    "Dominica " + x + " post Pentecosten",
                    [12, 'sd'],
                    {'int': PENTECOST_MASSES[p], 'glo': True,
                        'cre': True, 'pre': 'de Trinitate'},
                    {'proper': False, 'admag': [
                        'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                    False,
                    (False,),
                    post_pent_count + week(p),
                ]
            )
            for t in range(6):
                cycle.append(
                    [  # ! vespers
                        'De ea',
                        [22, 's'],
                        {'int': PENTECOST_MASSES[p], 'note': 'de Dom præc', 'glo': True,
                         'cre': False, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (8, 2, 6, 13, 3, 0,),
                        post_pent_count + week(p) + indays(t+1),
                    ]
                )
        elif count == 20 and post_pent_sundays == 23:
            cycle.append(  # todo anticipate the 23rd sunday and celebrate the 24th
                [  # ! vespers
                    "Dominica XXIII et ultima post Pentecosten",
                    [12, 'sd'],
                    {'int': PENTECOST_MASSES[-1], 'glo': True,
                        'cre': True, 'pre': 'de Trinitate'},
                    {'proper': False, 'admag': [
                        'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                    False,
                    (False,),
                    post_pent_count + week(p),
                ],
            )
            for t in range(6):
                cycle.append(
                    [  # ! vespers
                        'De ea',
                        [22, 's'],
                        {'int': PENTECOST_MASSES[-1], 'note': 'de Dom præc', 'glo': True,
                         'cre': False, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (8, 2, 6, 13, 3, 0,),
                        post_pent_count + week(p) + indays(t+1),
                    ]
                )
            break
        elif count == post_pent_sundays-3:
            cycle.append(
                [  # ! vespers
                    "Dominica " + x + " et ultima post Pentecosten",
                    [12, 'sd'],
                    {'int': PENTECOST_MASSES[-1], 'glo': True,
                        'cre': True, 'pre': 'de Trinitate'},
                    {'proper': False, 'admag': [
                        'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                    False,
                    (False,),
                    post_pent_count + week(p),
                ]
            )
            for t in range(6):
                cycle.append(
                    [  # ! vespers
                        'De ea',
                        [22, 's'],
                        {'int': PENTECOST_MASSES[-1], 'note': 'de Dom præc', 'glo': True,
                         'cre': False, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (8, 2, 6, 13, 3, 0,),
                        post_pent_count + week(p) + indays(t+1),
                    ]
                )
            break
        else:
            for y, x in enumerate(epiph_sunday_overflow, start=1):
                cycle.append(
                    [  # ! vespers
                        "Dominica " + ROMANS[p+y+3]
                        + " post Pentecosten, " + x + 'Epiphany',
                        [12, 'sd'],
                        {'int': 'Dicit Dominus', 'glo': True,
                            'cre': True, 'pre': 'de Trinitate'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        post_pent_count + week(p+y),
                    ]
                )
                for t in range(6):
                    cycle.append(
                        [  # ! vespers
                            'De ea',
                            [22, 's'],
                            {'int': 'Dicit Dominus', 'note': 'de Dom præc', 'glo': True,
                             'cre': False, 'pre': 'Communis'},
                            {'proper': False, 'admag': '',
                                'propers': {}, 'oration': ''},
                            False,
                            (8, 2, 6, 13, 3, 0,),
                            post_pent_count + week(p+y) + indays(t+1),
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
                    [  # ! vespers
                        "Feria IV Quatuor Temporum Septembris",
                        [18, 's'],
                        {'int': 'Exsultate Deo', 'glo': False,
                            'cre': False, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        post_pent_count + week(p) + indays(3),
                    ],
                    [  # ! vespers
                        "Feria VI Quatuor Temporum Septembris",
                        [18, 's'],
                        {'int': 'Laetetur cor', 'glo': False,
                            'cre': False, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
                        (False,),
                        post_pent_count + week(p) + indays(5),
                    ],
                    [  # ! vespers
                        "Sabbatum Quatuor Temporum Septembris",
                        [18, 's'],
                        {'int': 'Venite, adoremus', 'glo': False,
                            'cre': False, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        False,
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
                        False,
                        (False,),
                        christ_king,
                    ],
                )
            i += 1
    if christmas == lastadvent:  # prevents advent 4 and christmas occurance
        lastadvent -= week(1)
    advents = [
        "Dominica IV Adventus",
        "Dominica III Adventus",
        "Dominica II Adventus",
        "Dominica I Adventus",
    ]
    advent_introits = []
    for i, x in enumerate(advents):
        for k, y in enumerate(ROMANS[3:7], start=1):
            cycle.append(
                [  # ! mass, vespers
                    'Feria ' + y + " infra Hebd" + x.strip('Dominica'),
                    [18, 'feria'],
                    {'int': 'Ad te levavi' if x == 'Dominica I Adventus' else ('Populus Sion' if x == "Dominica II Adventus" else (
                            'Gaudete' if x == "Dominica III Adventus" else 'Rorate cæli')), 'glo': False,
                     'cre': False, 'pre': 'Communis'},
                    {'proper': False, 'admag': '',
                     'propers': {}, 'oration': ''},
                    'feria',
                    (9, 2, 6, 13, 3, 0),
                    lastadvent - week(i) + indays(k),
                ]
            )
        cycle.append(
            [  # ! mass, vespers
                'Sabbatum infra Hebd' + x.strip('Dominica'),
                [18, 'feria'],
                {'int': 'Ad te levavi' if x == 'Dominica I Adventus' else ('Populus Sion' if x == "Dominica II Adventus" else (
                    'Gaudete' if x == "Dominica III Adventus" else 'Rorate cæli')), 'glo': False,
                 'cre': False, 'pre': 'Communis'},
                {'proper': False, 'admag': '',
                 'propers': {}, 'oration': ''},
                'feria',
                (9, 2, 6, 13, 3, 0),
                lastadvent - week(i) + indays(6),
            ]
        )
        if x == "Dominica III Adventus":
            cycle.extend(
                [
                    [  # ! vespers
                        x,
                        [8, 'sd II cl'],
                        # ? Not really necessary?
                        {'int': 'Populus Sion' if x == "Dominica II Adventus" else (
                            'Gaudete' if x == "Dominica III Adventus" else 'Rorate cæli'), 'glo': False, 'cre': True, 'pre': 'de Trinitate'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        'dominica',
                        (False,),
                        lastadvent - week(i)
                    ],
                    [  # ! vespers
                        "Feria IV Quatuor Temporum in Adventus",
                        [18, 's'],
                        {'int': 'Rorate cæli', 'glo': False,
                            'cre': False, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        'feria',
                        (9, 2, 6, 13, 3, 0),
                        lastadvent - week(i) + indays(3),
                    ],
                    [  # ! vespers
                        "Feria VI Quatuor Temporum in Adventus",
                        [18, 's'],
                        {'int': 'Prope es tu', 'glo': False,
                            'cre': False, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        'feria',
                        (9, 2, 6, 13, 3, 0),
                        lastadvent - week(i) + indays(5),
                    ],
                    [  # ! vespers
                        "Sabbatum Quatuor Temporum in Adventus",
                        [18, 's'],
                        {'int': 'Veni, et ostende', 'glo': False,
                            'cre': False, 'pre': 'Communis'},
                        {'proper': False, 'admag': '',
                            'propers': {}, 'oration': ''},
                        'feria',
                        (9, 2, 6, 13, 3, 0),
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
                    {'proper': False, 'admag': [
                        'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                    'dominica',
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
                    {'proper': False, 'admag': [
                        'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                    'dominica',
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
            {'proper': False, 'admag': [
                'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
            False,
            (False,),
            christmas - indays(1)
        ],  # TODO If the vigil is a Sunday, there is a commemoration, Creed, de Trinitate, but no Proper Last Gospel
        [  # ! vespers
            "Nativitas DNJC",
            [2, 'd I cl cum Oct privil 3 ord'],
            {
                'Ad Primam Missam': {'int': 'Domine dixit', 'glo': True, 'cre': True, 'pre': 'et Comm (in hac Missa tantum dicitur "noctem") de Nativitate'},
                'Ad Secundam Missam': {'int': 'Lux fulgebit', 'glo': True, 'cre': True, 'pre': 'et Comm de Nativitate'},
                'Ad Tertiam Missam': {'int': 'Puer natus', 'glo': True, 'cre': True, 'pre': 'et Comm de Nativitate'},
            },
            {'proper': False, 'admag': [
                'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
            False,
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
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
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
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
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
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
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
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                christmas + indays(1),
            ],
            [  # ! vespers
                "S. Joannis Ap. Ev.",
                [10, 'd II cl cum Oct simplici'],
                {'int': 'In medio ecclesiæ', 'glo': True, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                christmas + indays(2),
            ],
            [  # ! vespers
                "Ss Innocentium Mm.",
                [10, 'd II cl cum Oct simplici'],
                {'int': 'Ex ore infantium', 'glo': True, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                christmas + indays(3),
            ],
            [  # ! vespers
                "S. Thomæ E.M.",
                [15, 'd'],
                {'int': 'Gaudeamus omnes', 'glo': True, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                christmas + indays(4),
            ],
            [  # ! vespers
                "S. Silvestri I P.C.",
                [15, 'd'],
                {'int': 'Si diligis me', 'glo': False, 'cre': True,
                    'pre': 'et Communicantes de Nativitate'},
                {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                False,
                (False,),
                christmas + indays(6),
            ],
        ]
    )

    def make_dict(year: int):
        gen_file = "temporal/temporal_" + str(year)
        with open(gen_file + ".py", "w") as f:
            f.write("temporal = {")
            keylist_alt = ['feast', 'rank', 'com_1',
                           'mass', 'vespers', 'office_type', 'nobility']
            keylist = ['feast', 'rank', 'mass',
                       'vespers', 'office_type', 'nobility']
            memory = []
            for row in cycle:
                temporal_event = row[-1].strftime("%m/%d")
                if temporal_event in memory:
                    temporal_event += "."
                memory.append(temporal_event)
                # todo simplify this
                if len(row) <= 7:
                    mini_dict = str(
                        dict(
                            zip(
                                keylist,
                                [
                                    row[0],
                                    row[1],
                                    row[2],
                                    row[3],
                                    row[4],
                                    row[5],
                                ],
                            )
                        )
                    )
                # just for the circumcision
                elif len(row) == 8:
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
                                    row[5],
                                    row[6],
                                ],
                            )
                        )
                    )
                else:
                    pass 
                f.write(
                    str("\n'" + temporal_event + "'" + ": " + mini_dict + ",")
                )
            f.write("}")
        dict_clean('temporal', '.')
    make_dict(year)
