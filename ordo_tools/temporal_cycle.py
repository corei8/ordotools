import re
from datetime import datetime, date
from ordo_tools.utils import dict_clean, our_ladys_saturday, indays, day, weekday, findsunday, week, easter, ROMANS, LENT_MASSES, FERIA, find_extra_epiphany, PENTECOST_MASSES


def build_temporal(year: int) -> None:
    """ Builds the temporal cycle for a given year and writes it to a file.

    Args:
            year (int): Year for the temporal cycle

    Returns:
            None
    """
    cycle = {}
    # todo make cycle a dictionary
    circumcision = day(year, 1, 1)
    cycle.update(
        {
            str(circumcision): {  # ! vespers
                'feast': "Circumcisio DNJC et Oct. Nativitatis",
                'rank': [3, 'd II cl'],
                'com_1': {'feast': 'S. Telesphori PM'},
                'color': 'white',
                'mass': {'int': 'Puer natus', 'glo': True, 'cre': True, 'pre': 'et Comm de Nativitate'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': 'festiva',
                'nobility': (False,),
            },
            str(circumcision + indays(1)): {  # ! vespers
                'feast': "Octava S. Stephani Protomartyris",
                'rank': [18, 's'],
                'color': 'white',
                'mass': {'int': 'Sederunt', 'glo': True, 'cre': False, 'pre': 'de Nativitate'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': False,
                'nobility': (False,),
            },
            str(circumcision + indays(2)): {  # ! vespers
                'feast': "Octava S. Joannis Ap Ev",
                'rank': [18, 's'],
                'color': 'red',
                'mass': {'int': 'Introit', 'glo': True, 'cre': True, 'pre': 'Communis'},
                'vespers': {'proper': False, 'admag': [
                    'firstVespers', 'secondVerspers'], 'propers': {}, 'oration': ''},
                'office_type': False,
                'nobility': (False,),
            },
            str(circumcision + indays(3)): {  # ! vespers
                'feast': "Octava Ss Innocentium Mm.",
                'rank': [18, 's'],
                'color': 'red',
                'mass': {'int': 'Ex ore infantium', 'glo': True, 'cre': True, 'pre': 'Communis'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': False,
                'nobility': (False,),
            },
        }
    )
    if (
            weekday(circumcision) == "Sun"
            or weekday(circumcision) == "Mon"
            or weekday(circumcision) == "Tue"
    ):
        cycle.update(
            {
                str(day(year, 1, 2)): {  # ! vespers
                    'feast': "Ssmi Nominis Jesu",
                    'rank': [10, 'd II cl'],
                    'color': 'color',
                    'mass': {'int': 'In nomine Jesu', 'glo': True, 'cre': True, 'pre': 'de Nativitate'},
                    'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                    'office_type': 'festiva',
                    'nobility': (False,),
                }
            }
        )
    else:
        cycle.update(
            {
                str(circumcision-findsunday(circumcision)+week(1)): {  # ! vespers
                    'feast': "Ssmi Nominis Jesu",
                    'rank': [10, 'd II cl'],
                    'color': 'white',
                    'mass': {'int': 'In nomine Jesu', 'glo': True, 'cre': True, 'pre': 'de Nativitate'},
                    'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                    'office_type': 'festiva',
                    'nobility': (False,),
                }
            }
        )
    for i, x in enumerate(("Septuagesima", "Sexagesima", "Quinquagesima")):
        if x == "Septuagesima":
            septuadate = easter(year) - week(9 - i)
        cycle.update(
            {
                str(easter(year) - week(9 - i)): {  # ! mass, vespers
                    'feast': "Dominica in " + x,
                    'rank': [8, 'sd II cl'],
                    'color': 'white',
                    'mass': {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                    'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                    'office_type': 'dominica',
                    'nobility': (False,),
                },
            }
        )
    epiphany = day(year, 1, 6)
    cycle.update(
        {
            str(epiphany - indays(1)): {  # ! vespers
                'feast': "Vigilia Epiphaniæ",
                'rank': [12, 'sd Vig privil 2 cl'],
                'color': 'white',
                'mass': {'int': 'Dum medium silentium', 'glo': True, 'cre': True, 'pre': 'de Nativitate'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': 'feria',
                'nobility': (False,)
            },
            str(epiphany): {  # ! vespers
                'feast': "Epiphania DNJC",
                'rank': [2, 'd I cl cum Oct privil 2 ord'],
                'color': 'white',
                'mass': {'int': 'Ecce advenit', 'glo': True, 'cre': True, 'pre': 'de Epiphania'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': 'festiva',
                'nobility': (False,)
            },
            str(epiphany + indays(7)): {  # ! mass, vespers
                'feast': "Octava Epiphaniæ",
                'rank': [13, 'dm'],
                'color': 'white',
                'mass': {'int': 'Ecce advenit', 'glo': True, 'cre': True, 'pre': 'Communis'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': False,
                'nobility': (False,)

            },
        }
    )
    if weekday(epiphany) == "Sun":
        first_epiph = epiphany + week(1)
    else:
        first_epiph = epiphany - findsunday(epiphany) + week(1)
    epiphany_sundays_counter = 1
    for i, x in enumerate(ROMANS[0: 6]):
        if weekday(epiphany + indays(i+1)) != "Sun":
            cycle.update(
                {
                    str(epiphany + indays(i+1)): {  # ! mass, vespers
                        'feast': "De "+ROMANS[i+1]+" die infra Oct. Epiphaniæ",
                        'rank': [9, 'feria'],
                        'color': 'white',
                        'mass': {'int': 'Ecce advenit', 'glo': True, 'cre': True, 'pre': 'Communis'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': False,
                        'nobility': (False,),
                    },
                }
            )
        else:
            pass
    epiph_counter, o = first_epiph, 0
    epiph_sundays = ["I", "II", "III", "IV", "V", "VI"]
    while epiph_counter.strftime('%m%d') != septuadate.strftime('%m%d'):
        if epiph_sundays[o] == 'I':
            if epiph_counter == day(year, 1, 13):
                cycle.update(
                    {
                        str(epiph_counter): {  # ! vespers
                            'feast': "In Octava Epiphaniæ",
                            'rank': [13, 'dm'],
                            'color': 'white',
                            'mass': {'int': 'Ecce advenit', 'glo': True, 'cre': True, 'pre': 'et Comm de Epiphania'},
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': False,
                            'nobility': (False,),
                        },
                        str(epiph_counter - indays(1)): {  # ! vespers
                            'feast': "S. Familiæ Jesu, Mariæ, Joseph",
                            'rank': [11, 'dm'],
                            'color': 'white',
                            'mass': {'int': 'Exultat', 'glo': True, 'cre': True, 'pre': 'et communcantes de Epiphania'},
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': False,
                            'nobility': (False,),
                        },
                    }
                )
            else:
                cycle.update(
                    {
                        str(epiph_counter): {  # !  vespers
                            'feast': "S. Familiæ Jesu, Mariæ, Joseph; Dominica "+epiph_sundays[o]+" infra Oct. Epiphaniæ",
                            'rank': [11, 'dm'],
                            'color': 'white',
                            'mass': {'int': 'In excelso', 'glo': True, 'cre': True, 'pre': 'et Comm de Epiphania'},
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': False,
                            'nobility': (False,),
                        }
                    }
                )
        else:
            cycle.update(
                {
                    str(epiph_counter): {  # ! vespers
                        'feast': "Dominica "+epiph_sundays[o]+" post Epiphaniam",
                        'rank': [12, 'sd'],
                        'color': 'white',
                        'mass': {'int': 'Omnis terra', 'glo': True, 'cre': True, 'pre': 'de Ssma Trinitate'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'dominica',
                        'nobility': (False,),
                    }
                }
            )
            epiphany_sundays_counter += 1
        o += 1  # ? is enumerate possible?
        epiph_counter += week(1)  # ? this is probably too complicated
    for c, x in enumerate(["I in Quadragesima", "II in Quadragesima", "III in Quadragesima", "IV in Quadragesima (Lætare)", "de Passione", "in Palmis", ]):
        if x == "I in Quadragesima":
            cycle.update(
                {
                    str(easter(year) - week(6-c) - indays(4)): {  # ! vespers
                        'feast': "Dies Cinerum",
                        'rank': [3, 's I cl'],
                        'color': 'violet',
                        'mass': {'int': 'Misereris', 'glo': True, 'cre': True, 'pre': 'de Quadragesima'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'feria',
                        'nobility': (False,),
                    },
                    str(easter(year) - week(6-c) - indays(3)): {  # ! mass, vespers
                        'feast': "Feria V post Diem Cinerum",
                        'rank': [18, 's'],
                        'color': 'violet',
                        'mass': {'int': 'Dum clamarem', 'glo': False, 'cre': False, 'pre': 'de Quadragesima'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'feria',
                        'nobility': (False,),
                    },
                    str(easter(year) - week(6-c) - indays(2)): {  # ! vespers
                        'feast': "Feria VI post Diem Cinerum",
                        'rank': [18, 's'],
                        'color': 'violet',
                        'mass': {'int': 'Audivit', 'glo': False, 'cre': False, 'pre': 'de Quadragesima'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'feria',
                        'nobility': (False,),
                    },
                    str(easter(year) - week(6-c) - indays(1)): {  # ! mass, vespers
                        'feast': "Sabbatum post Diem Cinerum",
                        'rank': [18, 's'],
                        'color': 'violet',
                        'mass': {'int': 'Audivit', 'glo': False, 'cre': False, 'pre': 'de Quadragesima'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'feria',
                        'nobility': (False,),
                    },
                }
            )
        cycle.update(
            {
                str(easter(year) - week(6-c)): {
                    'feast': "Dominica "+x,
                    'rank': [1, 'sd I cl'],
                    'color': 'violet',
                    'mass': {'int': 'Invocabit me', 'glo': False, 'cre': True, 'pre': 'de Quadragesima'},
                    'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                    'office_type': 'dominica',
                    'nobility': (False,),
                }
            }
        )
        for j, y in enumerate(FERIA):
            if x == "de Passione" and y == "Feria VI":
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): {  # ! vespers
                            'feast': "Septem Dolorum BMV",
                            'rank': [14, 'dm'],
                            'color': 'violet',
                            'mass': {'int': 'Stabant', 'glo': False, 'seq': 'Stabat Mater', 'cre': True, 'pre': 'de B. Maria Virg.'},
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': False,
                            'nobility': (False,),
                        }
                    }
                )
            elif x == "I in Quadragesima" and y == "Feria IV":
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): {  # ! vespers
                            'feast': "Feria IV Quatuor Temporum Quadragesimæ",
                            'rank': [3, 's'],
                            'color': 'violet',
                            'mass': {'int': 'Reminiscere', 'glo': False, 'cre': False, 'pre': 'de Quadragesima'},
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': False,
                            'nobility': (False,),
                        }
                    }
                )
            elif x == "I in Quadragesima" and y == "Feria VI":
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): {  # ! vespers
                            'feast': "Feria VI Quatuor Temporum Quadragesim",
                            'rank': [3, 's'],
                            'color': 'violet',
                            'mass': {'int': 'De necessitatibus', 'glo': False, 'cre': False, 'pre': 'de Quadragesima'},
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': False,
                            'nobility': (False,),
                        }
                    }
                )
            elif x == "I in Quadragesima" and y == "Sabbatum":
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): {  # ! vespers
                            'feast': "Sabbatum Quatuor Temporum Quadragesim",
                            'rank': [3, 's'],
                            'color': 'violet',
                            'mass': {'int': 'Intret', 'glo': False, 'cre': False, 'pre': 'de Quadragesima'},
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': False,
                            'nobility': (False,),
                        }
                    }
                )
            elif x == "in Palmis" and y == "Feria V":
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): {  # ! vespers
                            'feast': y + " in Cœna Domini",
                            'rank': [2, 'd I cl'],
                            'color': 'white',
                            'mass': {'int': 'Nos autem', 'glo': True, 'cre': False, 'pre': 'de Cruce'},
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': False,
                            'nobility': (False,),
                        }
                    }
                )
            elif x == "in Palmis" and y == "Feria VI":
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): {  # ! vespers
                            'feast': y + " in Parasceve",
                            'rank': [2, 'd I cl'],
                            'color': 'black',
                            'mass': {'int': 'Haec dicit', 'glo': False, 'cre': False, 'pre': ''},
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': False,
                            'nobility': (False,),
                        }
                    }
                )
            elif x == "in Palmis" and y == "Sabbatum":
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): {  # ! vespers
                            'feast': "Sabbatum Sanctum",
                            'rank': [2, 'd I cl'],
                            'color': 'violet',
                            'mass': {'int': 'In Missa', 'glo': True, 'cre': False, 'pre': 'Te quidem'},
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': False,
                            'nobility': (False,),
                        }
                    }
                )
            elif x == "in Palmis":
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): {  # ! vespers
                            'feast': y + " Majoris Hebd",
                            'rank': [3, 's'],
                            'color': 'violet',
                            'mass': {'int': 'Judica, Domine' if y == 'Feria II' else ('Nos autem' if y == 'Feria III' else 'In nomine Jesu'), 'glo': False, 'cre': False, 'pre': 'de Cruce'},
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': False,
                            'nobility': (False,),
                        }
                    }
                )
            else:
                if x == "IV in Quadragesima (Lætare)":
                    new_x = re.sub("\(Lætare\)", "", x)
                else:
                    new_x = x
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): {  # ! vespers
                            'feast': y + " infra Hebd " + new_x,
                            'rank': [18, 'sd I cl'],
                            'color': 'violet',
                            'mass': {'int': LENT_MASSES[j-1], 'glo': False, 'cre': False, 'pre': 'de Quadragesima' if x != 'de Passione' else 'de Cruce'},
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': False,
                            'nobility': (False,),
                        }
                    }
                )
        i += 1
    cycle.update(
        {
            str(easter(year)): {  # !  vespers
                'feast': "Dominica Resurrectionis",
                'rank': [1, 'd I cl cum Oct privil I ord'],
                'color': 'white',
                'mass': {'int': 'Ressurexi', 'glo': True, 'seq': 'Victimae paschali laudes', 'cre': True, 'pre': 'Paschalis'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': 'festiva',
                'nobility': (False,),
            },
            str(easter(year) + indays(1)): {  # ! vespers
                'feast': "Feria II infra Oct. Paschæ",
                'rank': [2, 'd I cl'],
                'color': 'white',
                'mass': {'int': 'Introduxit', 'glo': True, 'seq': 'Victimae paschali laudes', 'cre': True, 'pre': 'et Comm et Hanc Igitur, ut in die Paschae'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': False,
                'nobility': (False,),
            },
            str(easter(year) + indays(2)): {  # ! vespers
                'feast': "Feria III infra Oct. Paschæ",
                'rank': [2, 'd I cl'],
                'color': 'white',
                'mass': {'int': 'Aqua sapientiae', 'glo': True, 'seq': 'Victimae paschali laudes', 'cre': True, 'pre': 'et Comm et Hanc Igitur, ut in die Paschae'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': False,
                'nobility': (False,),
            },
            str(easter(year) + indays(3)): {  # ! vespers
                'feast': "Feria IV infra Oct. Paschæ",
                'rank': [3, 'sd'],
                'color': 'white',
                'mass': {'int': 'Venite', 'glo': True, 'seq': 'Victimae paschali laudes', 'cre': True, 'pre': 'et Comm et Hanc Igitur, ut in die Paschae'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': False,
                'nobility': (False,),
            },
            str(easter(year) + indays(4)): {  # ! vespers
                'feast': "Feria V infra Oct. Paschæ",
                'rank': [3, 'sd'],
                'color': 'white',
                'mass': {'int': 'Victricem', 'glo': True, 'seq': 'Victimae paschali laudes', 'cre': True, 'pre': 'et Comm et Hang Igitur, ut in die Paschae'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': False,
                'nobility': (False,),
            },
            str(easter(year) + indays(5)): {  # ! vespers
                'feast': "Feria VI infra Oct. Paschæ",
                'rank': [3, 'sd'],
                'color': 'white',
                'mass': {'int': 'Eduxit eos', 'glo': True, 'seq': 'Victimae paschali laudes', 'cre': True, 'pre': 'et Comm et Hanc Igitur, ut in die Paschae'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': False,
                'nobility': (False,),
            },
            str(easter(year) + indays(6)): {  # ! vespers
                'feast': "Sabbatum in Albis",
                'rank': [3, 'sd'],
                'color': 'white',
                'mass': {'int': 'Eduxit Dominus', 'glo': True, 'seq': 'Victimae paschali laudes', 'cre': True, 'pre': 'et Comm et Hanc Igitur, ut in die Paschae'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': False,
                'nobility': (False,),
            },
        }
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
            cycle.update(
                {
                    str(easter(year) + week(i) + indays(3)): {  # ! mass, vespers
                        'feast': "Solemnitas S. Joseph, Sponsi BMV C. et Ecclesiæ Universalis Patroni",
                        # ! No octave (?)
                        'rank': [2, 'd I cl cum Oct Communi'],
                        'color': 'white',
                        'mass': {'int': 'Justus ut palma', 'glo': True, 'cre': True, 'pre': 'de S. Joseph'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': False,
                        'nobility': (False,),
                    },
                    # todo We need all the days within the octave
                    str(easter(year) + week(i + 1) + indays(3)): {  # ! mass, vespers
                        'feast': "Octava Solemnitatis S. Joseph",
                        'rank': [13, 'dm'],
                        'color': 'white',
                        'mass': {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': False,
                        'nobility': (False,),
                    },
                }
            )
        if x == "Dominica V post Pascha":
            cycle.update(
                {
                    str(easter(year) + week(i) + indays(1)): {  # ! vespers
                        'feast': "Feria II in Rogationibus",
                        'rank': [18, 'feria'],
                        'color': 'violet',
                        'mass': {'int': 'Exaudivit', 'glo': False, 'cre': True, 'pre': 'Paschalis'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'feria',
                        'nobility': (0, 0, 0, 13, 0, 0,),
                    },
                    str(easter(year) + week(i) + indays(2)): {  # ! vespers
                        'feast': "Feria III in Rogationibus",
                        'rank': [18, 'feria'],
                        'color': 'violet',
                        'mass': {'int': 'Exaudivit', 'glo': False, 'cre': True, 'pre': 'Paschalis'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'feria',
                        'nobility': (0, 0, 0, 13, 0, 0,),
                    },
                    str(easter(year) + week(i) + indays(3)): {  # ! vespers
                        'feast': "Feria IV in Rogationibus in Vigilia Ascensionis ",
                        'rank': [18, 'feria'],
                        'color': 'violet',
                        'mass': {'int': 'Exaudivit', 'glo': False, 'cre': True, 'pre': 'Paschalis'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'feria',
                        'nobility': (9, 2, 6, 13, 3, 0,),
                    },
                    str(easter(year) + week(i) + indays(4)): {  # ! vespers
                        'feast': "Ascensio DNJC",
                        'rank': [2, 'd I cl cum Oct privil 3 ord'],
                        'color': 'white',
                        'mass': {'int': 'Viri Galilæi', 'glo': True, 'cre': True, 'pre': 'et Comm de Ascensione'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'festiva',
                        'nobility': (False,),
                    },
                    str(easter(year) + week(i) + indays(4+7)): {  # ! vespers
                        'feast': "Oct. Ascensionis DNJC",
                        'rank': [13, 'dm'],
                        'color': 'white',
                        'mass': {'int': 'Viri Galilæi', 'glo': True, 'cre': True, 'pre': 'et Comm de Ascensione'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': False,
                        'nobility': (False,),
                    },
                }
            )
            ascension_day = easter(year) + week(i) + indays(5)
        if x == "Dominica infra Octavam Ascensionis":
            for j, y in enumerate(ROMANS[1: 6], start=1):
                if ascension_day + indays(j) == easter(year) + week(i):
                    continue
                elif (ascension_day + indays(j)).strftime("%A") == "Saturday":
                    cycle.update(
                        {
                            str(ascension_day + indays(j)): {  # ! vespers
                                'feast': "Sabbatum infra Oct. Ascensionis",
                                'rank': [16, 'sd'],
                                'color': 'white',
                                'mass': {'int': 'Exaudi, Domine', 'glo': True, 'cre': False, 'pre': 'de Ascensione'},
                                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                                'office_type': False,
                                'nobility': (False,),
                            }
                        }
                    )
                else:
                    cycle.update(
                        {
                            str(ascension_day + indays(j)): {  # ! vespers
                                'feast': "De "+y+" die infra Oct. Ascensionis",
                                'rank': [16, 'sd'],
                                'color': 'white',
                                'mass': {'int': 'Viri galilaei', 'glo': True, 'cre': False, 'pre': 'de Ascensione'},
                                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                                'office_type': False,
                                'nobility': (False,),
                            }
                        }
                    )
        if x == "Dominica in Albis":
            cycle.update(
                {
                    str(easter(year) + week(i)): {  # ! vespers
                        'feast': x,
                        'rank': [1, 'dm I cl'],
                        'color': 'white',
                        'mass': {'int': 'Quasi modo', 'glo': True, 'cre': True, 'pre': 'Paschalis'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'dominica',
                        'nobility': (False,),
                    }
                }
            )
        else:
            cycle.update(
                {
                    str(easter(year) + week(i)): {  # ! mass, vespers
                        'feast': x,
                        'rank': [12, 'sd'],
                        'color': 'white',
                        'mass': {'int': 'Missa', 'glo': True, 'cre': True, 'pre': 'Communis'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'dominica',
                        'nobility': (False,),
                    }
                }
            )
    pent_date = easter(year) + week(i+1)
    cycle.update(
        {
            str(pent_date - indays(1)): {  # ! vespers
                'feast': "Sabbatum Vigilia Pentecostes",
                'rank': [3, 'd I cl Vig privil I cl'],
                'color': 'red',
                'mass': {'int': 'Cum sanctificatus', 'glo': True, 'cre': False, 'pre': 'et Comm et Hanc Igitur de Pentecoste'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': False,
                'nobility': (False,),
            },
            str(pent_date): {  # ! vespers
                'feast': "Dominica Pentecostes",
                'rank': [1, 'd I cl cum Oct privil I ord'],
                'color': 'red',
                'mass': {'int': 'Spiritus Domini', 'glo': True, 'seq': 'Veni, Sancte Spiritus', 'cre': True, 'pre': 'et Comm et Hanc Igitur de Pentecoste'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': 'festiva',
                'nobility': (False,),
            },
        }
    )
    for j, y in enumerate(ROMANS[1: 6]):
        if y == "II" or y == "III":
            cycle.update(
                {
                    str(pent_date + indays(j + 1)): {  # ! vespers # ! Add all days within octave of pentecost
                        'feast': "Feria "+y+" infra Oct. Pentecostes",
                        'rank': [2, 'd I cl'],
                        'color': 'red',
                        'mass': {'int': 'Cibavit eos', 'glo': True, 'cre': True, 'seq': 'Veni, Sancte Spiritus', 'pre': 'et Comm et Hanc Igitur de Pentecoste'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'feria',
                        'nobility': (False,),
                    }
                }
            )
        else:
            cycle.update(
                {
                    str(pent_date + indays(j + 1)): {  # ! vespers
                        'feast': "Feria " + y + " infra Oct. Pentecostes",
                                                'rank': [3, 'd I cl'],
                                                'color': 'red',
                                                'mass': {'int': 'Accepite jucunditatem', 'glo': True, 'seq': 'Veni, Sancte Spiritus', 'cre': True, 'pre': 'et Comm et Hanc Igitur de Pentecoste'},
                                                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                                                'office_type': 'feria',
                                                'nobility': (False,),
                    }
                }
            )
    cycle.update(
        {
            str(pent_date + indays(j + 2)): {  # ! mass, vespers
                'feast': "Sabbatum infra Oct. Pentecostes",
                'rank': [3, 'sd'],
                'color': 'red',
                'mass': {'int': 'Missa', 'glo': True, 'seq': 'Veni, Sancte Spiritus', 'cre': True, 'pre': 'Communis'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': 'feria',
                'nobility': (False,),
            },
            str(easter(year) + week(i) + indays(3)): {  # ! vespers
                'feast': "Feria IV Quatuor Temporum infra Oct. Pentecostes",
                'rank': [18, 'sd'],
                'color': 'red',
                'mass': {'int': 'Deus, dum egredereris', 'glo': True, 'seq': 'Veni, Sancte Spiritus', 'cre': True, 'pre': 'et Comm et Hanc Igitur de Pentecoste'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': 'feria',
                'nobility': (False,),
            },
            str(easter(year) + week(i) + indays(5)): {  # ! vespers
                'feast': "Feria VI Quatuor Temporum infra Oct. Pentecostes",
                'rank': [18, 'sd'],
                'color': 'red',
                'mass': {'int': 'Repleatur os meum', 'glo': True, 'seq': 'Veni, Sancte Spiritus', 'cre': True, 'pre': 'et Comm et Hanc Igitur de Pentecoste'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': 'feria',
                'nobility': (False,),
            },
            str(easter(year) + week(i) + indays(6)): {  # ! vespers
                'feast': "Sabbatum Quatuor Temporum infra Oct. Pentecostes",
                'rank': [18, 'sd'],
                'color': 'red',
                'mass': {'int': 'Caritas Dei', 'glo': True, 'seq': 'Veni, Sancte Spiritus', 'cre': True, 'pre': 'et Comm et Hanc Igitur de Pentecoste'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': 'feria',
                'nobility': (False,),
            },
        }
    )
    i += 1
    prelim_pents = [
        {  # ! vespers
            'feast': "Festum Sanctissimæ Trinitatis",
            'rank': [2, 'd I cl'],
            'color': 'white',
            'mass': {'int': 'Benedicta sit', 'glo': True, 'cre': True, 'pre': 'de Ssma Trinitate'},
            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
            'office_type': 'festiva',
            'nobility': (False,)
        },
        {  # ! vespers
            'feast': "Dominica infra Oct. Ssmi Corporis Christi (Dominica II post Pentecosten)",
            'rank': [12, 'sd'],
            'color': 'white',
            'mass': {'int': 'Factus est', 'glo': True, 'seq': 'Lauda, Sion, Salvatorem', 'cre': True, 'pre': 'de Nativitate, vel de Ssma Trinitate'},
            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
            'office_type': 'dominica',
            'nobility': (False,)
        },
        {  # ! mass, vespers
            'feast': "Dominica infra Oct. Ssmi Cordis DNJC (Dominica III post Pentecosten)",
            'rank': [12, 'sd'],
            'color': 'white',
            'mass': {'int': 'Respice in me', 'glo': True, 'cre': True, 'pre': 'de sacratissimo Code Jesu'},
            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
            'office_type': 'dominica',
            'nobility': (False,)
        },
    ]
    for l, x in enumerate(prelim_pents):
        if x['feast'] == "Dominica infra Oct. Ssmi Corporis Christi (Dominica II post Pentecosten)":
            corpus_christi = pent_date + week(2) - indays(3)
            for j, y in enumerate(ROMANS[1: 7]):
                if (corpus_christi + indays(j+1)) == (pent_date + week(2)):
                    pass  # ? necessary?
                else:
                    feria_index = int(
                        (corpus_christi+indays(j+1)).strftime("%w"))-1
                    fer_num = FERIA[feria_index]
                    cycle.update(
                        {
                            str(corpus_christi + indays(j + 1)): {
                                'feast': fer_num+" infra Oct. Ssmi Corporis Christi",
                                'rank': [9, 'sd'],
                                'color': 'white',
                                'mass': {'int': 'Factus est', 'glo': True, 'seq': 'Lauda, Sion, Salvatorem', 'cre': True, 'pre': 'de Nativitate'},
                                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                                'office_type': 'feria',
                                'nobility': (False,),
                            }
                        }
                    )
            cycle.update(
                {
                    str(corpus_christi): {  # ! vespers
                        'feast': "Sanctissimi Corporis Christi",
                        'rank': [2, 'd I cl cum Oct privil 2 ord'],
                        'color': 'white',
                        'mass': {'int': 'Cibavit eos', 'glo': True, 'seq': 'Lauda, Sion', 'cre': True, 'pre': 'de Nativitate'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'festiva',
                        'nobility': (False,),
                    },
                    str(corpus_christi + week(1)): {  # ! vespers
                        'feast': "Octava Ssmi Corporis Christi",
                        'rank': [4, 'dm'],
                        'color': 'white',
                        'mass': {'int': 'Cibavit eos', 'glo': True, 'seq': 'Lauda, Sion', 'cre': True, 'pre': 'de Nativitate'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': False,
                        'nobility': (False,),
                    }
                }
            )
        if x['feast'] == "Dominica infra Oct. Ssmi Cordis DNJC (Dominica III post Pentecosten)":
            ssmi_cordis = pent_date + week(3) - indays(2)
            for j, y in enumerate(ROMANS[1: 7]):
                if ssmi_cordis + indays(j + 1) == pent_date + week(3):
                    pass
                else:
                    feria_index = int(
                        (ssmi_cordis + indays(j + 1)).strftime("%w")) - 1
                    fer_num = FERIA[feria_index]
                    cycle.update(
                        {
                            str(ssmi_cordis + indays(j + 1)): {  # ! vespers
                                'feast': fer_num+" infra Oct. Ssmi Cordis DNJC",
                                # ? is this supposed to be within a common octave?
                                'rank': [17, 'sd'],
                                'color': 'white',
                                'mass': {'int': 'Respice in me', 'glo': True, 'cre': True, 'pre': 'de Ssmo Corde Iesu vel de Ssma Trinitate'},
                                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                                'office_type': 'dominica',
                                'nobility': (False,),
                            },
                        }
                    )
            cycle.update(
                {
                    str(ssmi_cordis): {  # ! mass, vespers
                        'feast': "Sacratissimi Cordis Jesu",
                        'rank': [2, 'd I cl cum Oct privil 3 ord'],
                        'color': 'white',
                        'mass': {'int': 'Cogitationes', 'glo': True, 'cre': True, 'pre': 'de Ssmo Corde Iesu'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'festiva',
                        'nobility': (1, 0, 3, 1, 1, 0),
                    },
                    str(ssmi_cordis + week(1)): {  # ! mass, vespers
                        'feast': "Octava Sacratissimi Cordis Jesu",
                        'rank': [13, 'dm'],
                        'color': 'white',
                        'mass': {'int': 'Cogitationes', 'glo': True, 'cre': True, 'pre': 'de Ssmo Corde Iesu'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': False,
                        'nobility': (False,),
                    },
                }
            )
        cycle.update({str(pent_date+week(l+1)): x})
        i += 1
    sept_counter = 0
    christmas = datetime.strptime(str(year) + "-12-25", "%Y-%m-%d")
    lastadvent = christmas - findsunday(christmas)
    post_pent_sundays = int((((lastadvent - week(4))-pent_date)/7).days)-1
    post_pent_count = pent_date + week(4)
    epiph_sunday_overflow = ROMANS[6-find_extra_epiphany(
        post_pent_sundays): find_extra_epiphany(post_pent_sundays)+2]
    for count, x in enumerate(ROMANS[3: post_pent_sundays+1], start=1):
        p = count - 1
        if count <= 20:
            cycle.update(
                {
                    str(post_pent_count + week(p)): {  # ! vespers
                        'feast': "Dominica "+x+" post Pentecosten",
                        'rank': [12, 'sd'],
                        'color': 'green',
                        'mass': {'int': PENTECOST_MASSES[p], 'glo': True, 'cre': True, 'pre': 'de Trinitate'},
                        'com_1': {'oration': 'A cunctis', },
                        'com_2': {'oration': 'ad libitum', },
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'dominica',
                        'nobility': (False,),
                    },
                }
            )
            for t in range(6):
                cycle.update(
                    {
                        str(post_pent_count + week(p) + indays(t+1)): {  # ! vespers
                            'feast': 'De ea',
                            'rank': [22, 's'],
                            'color': 'green',
                            'mass': {'int': PENTECOST_MASSES[p], 'note': 'de Dom præc', 'glo': True, 'cre': False, 'pre': 'Communis'},
                            'com_1': {'oration': 'A cunctis', },
                            'com_2': {'oration': 'ad libitum', },
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': 'feria',
                            'nobility': (8, 2, 6, 13, 3, 0,),
                        },
                    }
                )
        elif count == 20 and post_pent_sundays == 23:
            cycle.update(  # todo anticipate the 23rd sunday and celebrate the 24th
                {
                    str(post_pent_count + week(p)): {  # ! vespers
                        'feast': "Dominica XXIII et ultima post Pentecosten",
                        'rank': [12, 'sd'],
                        'color': 'green',
                        'mass': {'int': PENTECOST_MASSES[-1], 'glo': True, 'cre': True, 'pre': 'de Trinitate'},
                        'com_1': {'oration': 'A cunctis', },
                        'com_2': {'oration': 'ad libitum', },
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': False,
                        'nobility': (False,),
                    },
                }
            )
            for t in range(6):
                cycle.update(
                    {
                        str(post_pent_count + week(p) + indays(t+1)): {  # ! vespers
                            'feast': 'De ea',
                            'rank': [22, 's'],
                            'color': 'green',
                            'mass': {'int': PENTECOST_MASSES[-1], 'note': 'de Dom præc', 'glo': True, 'cre': False, 'pre': 'Communis'},
                            'com_1': {'oration': 'A cunctis', },
                            'com_2': {'oration': 'ad libitum', },
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': 'feria',
                            'nobility': (8, 2, 6, 13, 3, 0,),
                        },
                    }
                )
            break
        elif count == post_pent_sundays-3:
            cycle.update(
                {
                    str(post_pent_count + week(p)): {  # ! vespers
                        'feast': "Dominica " + x + " et ultima post Pentecosten",
                        'rank': [12, 'sd'],
                        'color': 'green',
                        'mass': {'int': PENTECOST_MASSES[-1], 'glo': True, 'cre': True, 'pre': 'de Trinitate'},
                        'com_1': {'oration': 'A cunctis', },
                        'com_2': {'oration': 'ad libitum', },
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'dominica',
                        'nobility': (False,),
                    },
                }
            )
            for t in range(6):
                cycle.update(
                    {
                        str(post_pent_count + week(p) + indays(t+1)): {  # ! vespers
                            'feast': 'De ea',
                            'rank': [22, 's'],
                            'color': 'green',
                            'mass': {'int': PENTECOST_MASSES[-1], 'note': 'de Dom præc', 'glo': True, 'cre': False, 'pre': 'Communis'},
                            'com_1': {'oration': 'A cunctis', },
                            'com_2': {'oration': 'ad libitum', },
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': 'feria',
                            'nobility': (8, 2, 6, 13, 3, 0,),
                        },
                    }
                )
            break
        else:
            for y, x in enumerate(epiph_sunday_overflow, start=1):
                cycle.update(
                    {
                        str(post_pent_count + week(p+y)): {  # ! vespers
                            'feast': 'Dominica '+ROMANS[p+y+3]+' post Pentecosten, '+x+'Epiphany',
                            'rank': [12, 'sd'],
                            'color': 'green',
                            'mass': {'int': 'Dicit Dominus', 'glo': True, 'cre': True, 'pre': 'de Trinitate'},
                            'com_1': {'oration': 'A cunctis', },
                            'com_2': {'oration': 'ad libitum', },
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': 'dominica',
                            'nobility': (False,),
                        },
                    }  # ! vespers
                )
                for t in range(6):
                    cycle.update(
                        {
                            str(post_pent_count + week(p+y) + indays(t+1)): {  # ! vespers
                                'feast': 'De ea',
                                'rank': [22, 's'],
                                'color': 'green',
                                'mass': {'int': 'Dicit Dominus', 'note': 'de Dom præc', 'glo': True, 'cre': False, 'pre': 'Communis'},
                                'com_1': {'oration': 'A cunctis', },
                                'com_2': {'oration': 'ad libitum', },
                                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                                'office_type': 'feria',
                                'nobility': (8, 2, 6, 13, 3, 0,),
                            },
                        }
                    )
        if (post_pent_count + week(p)).strftime("%B") == "September":
            if int((post_pent_count + week(p)).strftime("%d")) <= 3:
                sept_counter += 0
            else:
                sept_counter += 1
        if sept_counter == 3:
            cycle.update(
                {
                    str(post_pent_count + week(p) + indays(3)): {  # ! vespers
                        'feast': "Feria IV Quatuor Temporum Septembris",
                        'rank': [18, 's'],
                        'color': 'violet',
                        'mass': {'int': 'Exsultate Deo', 'glo': False, 'cre': False, 'pre': 'Communis'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'feria',
                        'nobility': (False,),
                    },
                    str(post_pent_count + week(p) + indays(5)): {  # ! vespers
                        'feast': "Feria VI Quatuor Temporum Septembris",
                        'rank': [18, 's'],
                        'color': 'violet',
                        'mass': {'int': 'Laetetur cor', 'glo': False, 'cre': False, 'pre': 'Communis'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'feria',
                        'nobility': (False,),
                    },
                    str(post_pent_count + week(p) + indays(6)): {  # ! vespers
                        'feast': "Sabbatum Quatuor Temporum Septembris",
                        'rank': [18, 's'],
                        'color': 'violet',
                        'mass': {'int': 'Venite, adoremus', 'glo': False, 'cre': False, 'pre': 'Communis'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'feria',
                        'nobility': (False,),
                    },
                }
            )

            if (post_pent_count + week(p)).strftime("%B") == "November" and (easter(year) + week(i-1)).strftime("%B") == "October":
                # if the current Sunday is in November and the previous Sunday is in October
                christ_king = post_pent_count + week(p) - week(1)
                cycle.update(
                    {
                        str(christ_king): {  # ! vespers
                            'feast': 'In Festo DNJC Regis',
                            'rank': [2, 'd I cl'],
                            'color': 'white',
                            'mass': {'int': 'Dignus est', 'glo': True, 'cre': True, 'pre': 'de DNJC Rege'},
                            'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                            'office_type': 'festiva',
                            'nobility': (False,),
                        },
                    }
                )
            i += 1
    if christmas == lastadvent:  # prevents 4th Sunday of Advent and Christmas occurance
        lastadvent -= week(1)
    advents = [
        "Dominica IV Adventus",
        "Dominica III Adventus",
        "Dominica II Adventus",
        "Dominica I Adventus",
    ]
    for i, x in enumerate(advents):
        for k, y in enumerate(ROMANS[3: 7], start=1):
            cycle.update(
                {
                    str(lastadvent - week(i) + indays(k)): {  # ! mass, vespers
                        'feast': 'Feria '+y+" infra Hebd"+x.strip('Dominica'),
                        'rank': [18, 'feria'],
                        'color': 'violet',
                        'mass': {'int': 'Ad te levavi' if x == 'Dominica I Adventus' else ('Populus Sion' if x == "Dominica II Adventus" else ('Gaudete' if x == "Dominica III Adventus" else 'Rorate cæli')), 'glo': False, 'cre': False, 'pre': 'Communis'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'feria',
                        'nobility': (9, 2, 6, 13, 3, 0),
                    },
                }
            )
        cycle.update(
            {
                str(lastadvent - week(i) + indays(6)): {  # ! mass, vespers
                    'feast': 'Sabbatum infra Hebd'+x.strip('Dominica'),
                    'rank': [18, 'feria'],
                    'color': 'violet',
                    'mass': {'int': 'Ad te levavi' if x == 'Dominica I Adventus' else ('Populus Sion' if x == "Dominica II Adventus" else ('Gaudete' if x == "Dominica III Adventus" else 'Rorate cæli')), 'glo': False, 'cre': False, 'pre': 'Communis'},
                    'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                    'office_type': 'feria',
                    'nobility': (9, 2, 6, 13, 3, 0),
                },
            }
        )
        if x == "Dominica III Adventus":
            cycle.update(
                {
                    str(lastadvent - week(i)): {  # ! vespers
                        'feast': x,
                        'rank': [8, 'sd II cl'],
                        'color': 'violet',
                        'mass': {'int': 'Populus Sion' if x == "Dominica II Adventus" else ('Gaudete' if x == "Dominica III Adventus" else 'Rorate cæli'), 'glo': False, 'cre': True, 'pre': 'de Trinitate'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'dominica',
                        'nobility': (False,),
                    },
                    str(lastadvent - week(i) + indays(3)): {  # ! vespers
                        'feast': "Feria IV Quatuor Temporum in Adventus",
                        'rank': [18, 's'],
                        'color': 'violet',
                        'mass': {'int': 'Rorate cæli', 'glo': False, 'cre': False, 'pre': 'Communis'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'feria',
                        'nobility': (9, 2, 6, 13, 3, 0),
                    },
                    str(lastadvent - week(i) + indays(5)): {  # ! vespers
                        'feast': "Feria VI Quatuor Temporum in Adventus",
                        'rank': [18, 's'],
                        'color': 'violet',
                        'mass': {'int': 'Prope es tu', 'glo': False, 'cre': False, 'pre': 'Communis'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'feria',
                        'nobility': (9, 2, 6, 13, 3, 0),
                    },
                    str(lastadvent - week(i) + indays(6)): {  # ! vespers
                        'feast': "Sabbatum Quatuor Temporum in Adventus",
                        'rank': [18, 's'],
                        'color': 'violet',
                        'mass': {'int': 'Veni, et ostende', 'glo': False, 'cre': False, 'pre': 'Communis'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'feria',
                        'nobility': (9, 2, 6, 13, 3, 0),
                    },
                }
            )
        elif x == "Dominica I Adventus":
            cycle.update(
                {
                    str(lastadvent - week(i)): {  # ! vespers
                        'feast': x,
                        'rank': [1, 'sd'],
                        'color': 'violet',
                        'mass': {'int': 'Ad te levavi', 'glo': False, 'cre': True, 'pre': 'de Trinitate'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'dominica',
                        'nobility': (False,),
                    },
                }
            )
        else:
            cycle.update(
                {
                    str(lastadvent - week(i)): {  # ! vespers
                        'feast': x,
                        'rank': [8, 'sd II cl'],
                        'color': 'violet',
                        'mass': {'int': 'Populus Sion' if x == "Dominica II Adventus" else ('Gaudete' if x == "Dominica III Adventus" else 'Rorate cæli'), 'glo': False, 'cre': True, 'pre': 'de Trinitate'},
                        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                        'office_type': 'dominica',
                        'nobility': (False,),
                    },
                }
            )
    cycle.update(
        {
            str(christmas-indays(1)): {  # ! vespers
                'feast': "Vigilia Nativitatis DNJC",
                'rank': [3, 'd I cl Vig privil I cl'],
                'color': 'violet',
                'mass': {'int': 'Hodie scietis', 'glo': False, 'cre': False, 'pre': 'Communis'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': 'feria',
                'nobility': (False,),
            },
            # TODO If the vigil is a Sunday, there is a commemoration, Creed, de Trinitate, but no Proper Last Gospel
            str(christmas): {  # ! vespers
                'feast': "Nativitas DNJC",
                'rank': [2, 'd I cl cum Oct privil 3 ord'],
                'color': 'white',
                'mass': {
                    'Ad Primam Missam': {'int': 'Domine dixit', 'glo': True, 'cre': True, 'pre': 'et Comm (in hac Missa tantum dicitur "noctem") de Nativitate'},
                    'Ad Secundam Missam': {'int': 'Lux fulgebit', 'glo': True, 'cre': True, 'pre': 'et Comm de Nativitate'},
                    'Ad Tertiam Missam': {'int': 'Puer natus', 'glo': True, 'cre': True, 'pre': 'et Comm de Nativitate'},
                },
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': 'festiva',
                'nobility': (False,),
            },
        }
    )
    if 5 <= int(christmas.strftime("%u")) <= 7 or christmas.strftime("%u") == 1:
        # todo this can be simplified
        cycle.update(
            {
                str(christmas + indays(5)): {  # ! mass, vespers
                    'feast': "Dominica Infra Octavam Nativitatis reposita",
                    'rank': [12, 'sd'],
                    'color': 'white',
                    'mass': {'int': 'Dum medium silentium', 'glo': True, 'cre': True, 'pre': 'de Comm de Nativitate'},
                    'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                    'office_type': 'dominica',
                    'nobility': (False,),
                },
            }
        )
    else:
        cycle.update(
            {
                str(christmas + indays(7) - findsunday(christmas)): {  # ! vespers
                    'feast': "Dominica Infra Octavam Nativitatis",
                    'rank': [12, 'sd'],
                    'color': 'white',
                    'mass': {'int': 'Dum medium', 'glo': True, 'cre': True, 'pre': 'et Comm de Nativitate'},
                    'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                    'office_type': 'dominica',
                    'nobility': (False,),
                },
            }
        )
    if (
        int(day(year, 12, 30).strftime("%u")) == 1
        or int(day(year, 12, 30).strftime("%u")) == 7
    ):
        cycle.update(
            {
                str(christmas + indays(5)): {  # ! mass, vespers
                    'feast': "Feria VI infra Octavam Nativitatis",
                    'rank': [16, 'sd'],
                    'color': 'white',
                    'mass': {'int': 'Puer natus est nobis', 'glo': True, 'cre': True, 'pre': 'et Comm de Nativitate'},
                    'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''}, 'office_type': 'feria',
                    'nobility': (False,),
                },
            }
        )
    cycle.update(
        {
            str(christmas + indays(1)): {  # ! vespers
                'feast': "S. Stephani Protomartyris",
                'rank': [10, 'd II cl cum Oct simplici'],
                'color': 'red',
                'mass': {'int': 'Sederunt', 'glo': True, 'cre': True, 'pre': 'et Comm de Nativitate'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': 'festiva',
                'nobility': (False,),
            },
            str(christmas + indays(2)): {  # ! vespers
                'feast': "S. Joannis Ap Ev",
                'rank': [10, 'd II cl cum Oct simplici'],
                'color': 'red',
                'mass': {'int': 'In medio ecclesiæ', 'glo': True, 'cre': True, 'pre': 'et Comm de Nativitate'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': 'festiva',
                'nobility': (False,),
            },
            str(christmas + indays(3)): {  # ! vespers
                'feast': "Ss Innocentium Mm",
                'rank': [10, 'd II cl cum Oct simplici'],
                'color': 'violet',
                'mass': {'int': 'Ex ore infantium', 'glo': True, 'cre': True, 'pre': 'et Comm de Nativitate'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': 'festiva',
                'nobility': (False,),
            },
            str(christmas + indays(4)): {  # ! vespers
                'feast': "S. Thomæ EM",
                'rank': [15, 'd'],
                'color': 'red',
                'mass': {'int': 'Gaudeamus omnes', 'glo': True, 'cre': True, 'pre': 'et Comm de Nativitate'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': 'festiva',
                'nobility': (False,),
            },
            str(christmas + indays(6)): {  # ! vespers
                'feast': "S. Silvestri I PC",
                'rank': [15, 'd'],
                'color': 'white',
                'mass': {'int': 'Si diligis me', 'glo': False, 'cre': True, 'pre': 'et Comm de Nativitate'},
                'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
                'office_type': 'festiva',
                'nobility': (False,),
            },
        }
    )

    def make_dict(year: int):
        gen_file = "temporal/temporal_" + str(year)
        with open(gen_file + ".py", "w") as f:
            f.write("temporal = {")
            memory = []
            for k, v in cycle.items():
                temporal_event = date.fromisoformat(k[0:10]).strftime("%m/%d")
                if temporal_event in memory:
                    temporal_event += "."
                memory.append(temporal_event)
                f.write(
                    str("\n'" + temporal_event + "'" + ": " + str(v) + ",")
                )
            f.write("}")
        dict_clean('temporal', '.')

    make_dict(year)

    our_ladys_saturday('temporal')
