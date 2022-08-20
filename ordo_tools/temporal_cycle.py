import re
from datetime import datetime
from utils import (
        indays, day, weekday, findsunday, 
        week, easter, ROMANS, LENT_MASSES, 
        FERIA, find_extra_epiphany, PENTECOST_MASSES
        )

EMBER_DAYS = []

# TODO: this function should be broken down
# TODO: make ids for all the feasts

def build_temporal(year: int) -> dict:
    """ 
    Builds the temporal cycle for a given year and writes it to a file.
    """
    cycle = {}
    circumcision = day(year, 1, 1)
    cycle.update(
        {
            str(circumcision): "Circumcisio DNJC et Oct. Nativitatis",
            str(circumcision + indays(1)): "Octava S. Stephani Protomartyris",
            str(circumcision + indays(2)): "Octava S. Joannis Ap Ev",
            str(circumcision + indays(3)): "Octava Ss Innocentium Mm.",
        }
    )
    if (
            weekday(circumcision) == "Sun"
            or weekday(circumcision) == "Mon"
            or weekday(circumcision) == "Tue"
    ):
        cycle.update(
            {
                str(day(year, 1, 2)): "Ssmi Nominis Jesu",
            }
        )
    else:
        cycle.update(
            {
                str(circumcision-findsunday(circumcision)+week(1)): "Ssmi Nominis Jesu",
            }
        )
    for i, x in enumerate(("Septuagesima", "Sexagesima", "Quinquagesima")):
        if x == "Septuagesima":
            septuadate = easter(year) - week(9 - i)
        cycle.update(
            {
                str(easter(year) - week(9 - i)): "Dominica in " + x,
            }
        )
    epiphany = day(year, 1, 6)
    cycle.update(
        {
            str(epiphany - indays(1)): "Vigilia Epiphaniæ",
            str(epiphany): "Epiphania DNJC",
            str(epiphany + indays(7)): "Octava Epiphaniæ",
        }
    )
    if weekday(epiphany) == "Sun":
        first_epiph = epiphany + week(1)
    else:
        first_epiph = epiphany - findsunday(epiphany) + week(1)
    epiphany_sundays_counter = 1
    for i, x in enumerate(ROMANS[0: 6]):
        if weekday(epiphany + indays(i+1)) != "Sun":
            # TODO: the the global FERIA for these
            if weekday(epiphany + indays(i+1)) == "Sat":
                cycle.update(
                    {
                        str(epiphany + indays(i+1)): "Sabbato infra Oct. Epiphaniæ",
                    }
                )
            else:
                cycle.update(
                    {
                        str(epiphany + indays(i+1)): "De "+ROMANS[i+1]+" die infra Oct. Epiphaniæ",
                    }
                )
        else:
            pass
    epiph_counter, o = first_epiph, 0
    epiph_sundays = ["I", "II", "III", "IV", "V", "VI"]
    while epiph_counter.strftime('%m%d') != septuadate.strftime('%m%d'):
        if epiph_sundays[o] == 'I':
            if epiph_counter == day(year, 1, 13):
                # TODO: add ferias
                cycle.update(
                    {
                        str(epiph_counter): "In Octava Epiphaniæ",
                        str(epiph_counter - indays(1)): "S. Familiæ Jesu, Mariæ, Joseph",
                    }
                )
            else:
                cycle.update(
                    {
                        str(epiph_counter): "S. Familiæ Jesu, Mariæ, Joseph; Dominica "+epiph_sundays[o]+" infra Oct. Epiphaniæ",
                    }
                )
        else:
            cycle.update(
                {
                    str(epiph_counter): "Dominica "+epiph_sundays[o]+" post Epiphaniam",
                }
            )
            for t in range(6):
                cycle.update(
                    {
                        str(epiph_counter + indays(t+1)): 'De ea',
                    }
                )
            epiphany_sundays_counter += 1
        o += 1  #? is enumerate possible
        epiph_counter += week(1)  #! this is probably too complicated
    for c, x in enumerate(["I in Quadragesima", "II in Quadragesima", "III in Quadragesima", "IV in Quadragesima (Lætare)", "de Passione", "in Palmis", ]):
        if x == "I in Quadragesima":
            cycle.update(
                {
                    str(easter(year) - week(6-c) - indays(4)): "Dies Cinerum",
                    str(easter(year) - week(6-c) - indays(3)): "Feria V post Diem Cinerum",
                    str(easter(year) - week(6-c) - indays(2)): "Feria VI post Diem Cinerum",
                    str(easter(year) - week(6-c) - indays(1)): "Sabbatum post Diem Cinerum",
                }
            )
        cycle.update(
            {
                str(easter(year) - week(6-c)): "Dominica "+x,
            }
        )
        for j, y in enumerate(FERIA):
            if x == "de Passione" and y == "Feria VI":
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): "Septem Dolorum BMV",
                    }
                )
            # ! unite the redundant ifs
            elif x == "I in Quadragesima" and y == "Feria IV":
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): "Feria IV Quatuor Temporum Quadragesimæ",
                    }
                )
                EMBER_DAYS.append(easter(year) - week(6-c) + indays(j+1))
            elif x == "I in Quadragesima" and y == "Feria VI":
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): "Feria VI Quatuor Temporum Quadragesim",
                    }
                )
                EMBER_DAYS.append(easter(year) - week(6-c) + indays(j+1))
            elif x == "I in Quadragesima" and y == "Sabbatum":
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): "Sabbatum Quatuor Temporum Quadragesim",
                    }
                )
                EMBER_DAYS.append(easter(year) - week(6-c) + indays(j+1))
            elif x == "in Palmis" and y == "Feria V":
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): y + " in Cœna Domini",
                    }
                )
            elif x == "in Palmis" and y == "Feria VI":
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): y + " in Parasceve",
                    }
                )
            elif x == "in Palmis" and y == "Sabbatum":
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): "Sabbatum Sanctum",
                    }
                )
            elif x == "in Palmis":
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): y + " Majoris Hebd",
                    }
                )
            else:
                if x == "IV in Quadragesima (Lætare)":
                    new_x = re.sub("\(Lætare\)", "", x)
                else:
                    new_x = x
                cycle.update(
                    {
                        str(easter(year) - week(6-c) + indays(j+1)): y + " infra Hebd " + new_x,
                    }
                )
        i += 1
    cycle.update(
        {
            str(easter(year)): "Dominica Resurrectionis",
            str(easter(year) + indays(1)): "Feria II infra Oct. Paschæ",
            str(easter(year) + indays(2)): "Feria III infra Oct. Paschæ",
            str(easter(year) + indays(3)): "Feria IV infra Oct. Paschæ",
            str(easter(year) + indays(4)): "Feria V infra Oct. Paschæ",
            str(easter(year) + indays(5)): "Feria VI infra Oct. Paschæ",
            str(easter(year) + indays(6)): "Sabbatum in Albis",
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
                    str(easter(year) + week(i) + indays(3)): "Solemnitas S. Joseph, Sponsi BMV C. et Ecclesiæ Universalis Patroni",
                    # todo We need all the days within the octave
                    str(easter(year) + week(i + 1) + indays(3)): "Octava Solemnitatis S. Joseph",
                }
            )
        if x == "Dominica V post Pascha":
            ROGATION_MONDAY = easter(year) + week(i) + indays(1)
            cycle.update(
                {
                    str(easter(year) + week(i) + indays(1)): "Feria II in Rogationibus",
                    str(easter(year) + week(i) + indays(2)): "Feria III in Rogationibus",
                    str(easter(year) + week(i) + indays(3)): "Feria IV in Rogationibus in Vigilia Ascensionis ",
                    str(easter(year) + week(i) + indays(4)): "Ascensio DNJC",
                    str(easter(year) + week(i) + indays(4+7)): "Oct. Ascensionis DNJC",
                }
            )
            asc_day = easter(year) + week(i) + indays(5)
        if x == "Dominica infra Octavam Ascensionis":
            for j, y in enumerate(ROMANS[1: 6], start=1):
                if asc_day + indays(j) == easter(year) + week(i):
                    continue
                elif (asc_day + indays(j)).strftime("%A") == "Saturday":
                    cycle.update(
                        {
                            str(asc_day + indays(j)): "Sabbatum infra Oct. Ascensionis",
                        }
                    )
                else:
                    cycle.update(
                        {
                            str(asc_day + indays(j)): "De "+y+" die infra Oct. Ascensionis",
                        }
                    )
        if x == "Dominica in Albis":
            cycle.update(
                {
                    str(easter(year) + week(i)): x,
                }
            )
        else:
            cycle.update(
                {
                    str(easter(year) + week(i)): x,
                }
            )
    pent_date = easter(year) + week(i+1)
    cycle.update(
        {
            str(pent_date - indays(1)): "Sabbatum Vigilia Pentecostes",
            str(pent_date): "Dominica Pentecostes",
        }
    )
    for j, y in enumerate(ROMANS[1: 6]):
        if y == "II" or y == "III":
            cycle.update(
                {
                    str(pent_date + indays(j + 1)): "Feria "+y+" infra Oct. Pentecostes",
                    # ! Add all days within octave of pentecost
                }
            )
        else:
            cycle.update(
                {
                    str(pent_date + indays(j + 1)): "Feria " + y + " infra Oct. Pentecostes",
                }
            )
    cycle.update(
        {
            str(pent_date + indays(j + 2)): "Sabbatum infra Oct. Pentecostes",
            str(easter(year) + week(i+1) + indays(3)): "Feria IV Quatuor Temporum infra Oct. Pentecostes",
            str(easter(year) + week(i+1) + indays(5)): "Feria VI Quatuor Temporum infra Oct. Pentecostes",
            str(easter(year) + week(i+1) + indays(6)): "Sabbatum Quatuor Temporum infra Oct. Pentecostes",
        }
    )
    EMBER_DAYS.extend(
            [
                easter(year) + week(i+1) + indays(3), 
                easter(year) + week(i+1) + indays(5), 
                easter(year) + week(i+1) + indays(6)
                ]
            )
    i += 1
    prelim_pents = [
            "Festum Sanctissimæ Trinitatis",
            "Dominica infra Oct. Ssmi Corporis Christi (Dominica II post Pentecosten)",
            "Dominica infra Oct. Ssmi Cordis DNJC (Dominica III post Pentecosten)",
            ]
    for l, x in enumerate(prelim_pents):
        if x == "Dominica infra Oct. Ssmi Corporis Christi (Dominica II post Pentecosten)":
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
                            str(corpus_christi + indays(j + 1)): fer_num+" infra Oct. Ssmi Corporis Christi",
                        }
                    )
            cycle.update(
                {
                    str(corpus_christi): "Sanctissimi Corporis Christi",
                    str(corpus_christi + week(1)): "Octava Ssmi Corporis Christi",
                }
            )
        if x == "Dominica infra Oct. Ssmi Cordis DNJC (Dominica III post Pentecosten)":
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
                            # ? is this supposed to be within a common octave?
                            str(ssmi_cordis + indays(j + 1)): fer_num+" infra Oct. Ssmi Cordis DNJC",
                        }
                    )
            cycle.update(
                {
                    str(ssmi_cordis): "Sacratissimi Cordis Jesu",
                    str(ssmi_cordis + week(1)): "Octava Sacratissimi Cordis Jesu",
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
                    str(post_pent_count + week(p)): "Dominica "+x+" post Pentecosten",
                }
            )
            for t in range(6):
                cycle.update(
                    {
                        str(post_pent_count + week(p) + indays(t+1)): 'De ea',
                    }
                )
        elif count == 20 and post_pent_sundays == 23:
            cycle.update(  # TODO: anticipate the 23rd sunday and celebrate the 24th
                {
                    str(post_pent_count + week(p)): "Dominica XXIII et ultima post Pentecosten",
                }
            )
            for t in range(6):
                cycle.update(
                    {
                        str(post_pent_count + week(p) + indays(t+1)): 'De ea',
                    }
                )
            break
        elif count == post_pent_sundays-3:
            cycle.update(
                {
                    str(post_pent_count + week(p)): "Dominica " + x + " et ultima post Pentecosten",
                }
            )
            for t in range(6):
                cycle.update(
                    {
                        str(post_pent_count + week(p) + indays(t+1)): 'De ea',
                    }
                )
            break
        else:
            for y, x in enumerate(epiph_sunday_overflow, start=1):
                cycle.update(
                    {
                        str(post_pent_count + week(p+y)): 'Dominica '+ROMANS[p+y+3]+' post Pentecosten, '+x+'Epiphany',
                    }  
                )
                for t in range(6):
                    cycle.update(
                        {
                            str(post_pent_count + week(p+y) + indays(t+1)): 'De ea',
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
                    str(post_pent_count + week(p) + indays(3)): "Feria IV Quatuor Temporum Septembris",
                    str(post_pent_count + week(p) + indays(5)): "Feria VI Quatuor Temporum Septembris",
                    str(post_pent_count + week(p) + indays(6)): "Sabbatum Quatuor Temporum Septembris",
                }
            )
            EMBER_DAYS.extend(
                    [
                        post_pent_count + week(p) + indays(3),
                        post_pent_count + week(p) + indays(5), 
                        post_pent_count + week(p) + indays(6)
                        ]
                    )
        if (post_pent_count + week(p)).strftime("%B") == "November" and (post_pent_count + week(p-1)).strftime("%B") == "October":
            # if the current Sunday is in November and the previous Sunday is in October
            christ_king = post_pent_count + week(p) - week(1)
            cycle.update(
                {
                    str(christ_king): 'In Festo DNJC Regis',
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
        for k, y in enumerate(ROMANS[1: 6], start=1):
            cycle.update(
                {
                    str(lastadvent - week(i) + indays(k)): 'Feria '+y+" infra Hebd"+x.strip('Dominica'),
                }
            )
        else:
            cycle.update(
                {
                    str(lastadvent - week(i) + indays(6)): 'Sabbatum infra Hebd'+x.strip('Dominica'),
                }
            )
        if x == "Dominica III Adventus":
            cycle.update(
                {
                    str(lastadvent - week(i)): x,
                    str(lastadvent - week(i) + indays(3)): "Feria IV Quatuor Temporum in Adventus",
                    str(lastadvent - week(i) + indays(5)): "Feria VI Quatuor Temporum in Adventus",
                    str(lastadvent - week(i) + indays(6)): "Sabbatum Quatuor Temporum in Adventus",
                }
            )
            EMBER_DAYS.extend(
                    [
                        lastadvent - week(i) + indays(4),
                        lastadvent - week(i) + indays(5),
                        lastadvent - week(i) + indays(6)
                        ]
                    )
        elif x == "Dominica I Adventus":
            cycle.update(
                {
                    str(lastadvent - week(i)): x,
                }
            )
        else:
            cycle.update(
                {
                    str(lastadvent - week(i)): x,
                }
            )
    else:
        cycle.update(
            {
                str(christmas-indays(1)): "Vigilia Nativitas DNJC",
                # TODO: If the vigil is a Sunday, there is a commemoration, Creed, de Trinitate, but no Proper Last Gospel
                str(christmas): "Nativitas DNJC",
            }
        )
    if findsunday(christmas) == 0 or 1 or 2 or 3:
        # Dominica infra respsita on 30 if Sunday falls on 25, 26, 27 or 28
        cycle.update(
            {
                str(christmas + indays(5)): "Dominica Infra Octavam Nativitatis reposita",
            }
        )
    else:
        # NOTE: Dominica infra if Sunday falls on 29, 30 or 31
        cycle.update(
            {
                str(christmas + indays(7) - findsunday(christmas)): "Dominica Infra Octavam Nativitatis",
            }
        )
    if (
        int(day(year, 12, 30).strftime("%u")) == 1
        or int(day(year, 12, 30).strftime("%u")) == 7
    ):
        cycle.update(
            {
                str(christmas + indays(5)): "Feria VI infra Octavam Nativitatis",
            }
        )
    cycle.update(
        {
            str(christmas + indays(1)): "S. Stephani Protomartyris",
            str(christmas + indays(2)): "S. Joannis Ap Ev",
            str(christmas + indays(3)): "Ss Innocentium Mm",
            str(christmas + indays(4)): "S. Thomæ EM",
            str(christmas + indays(6)): "S. Silvestri I PC",
        }
    )
    # TODO: return the dict sorted
    return cycle


# NOTE: Testing purposes:

def test_temporal(year: int):
    temp_cycle = build_temporal(year=year)
    for item in sorted(temp_cycle):
        format = "%Y-%m-%d %H:%M:%S"
        date = datetime.strftime(datetime.strptime(item, format), '%a, %b %d')
        print(date + " --> " + temp_cycle[item])
    return None

test_year = int(input('test year: '))

print('-'*20)

test_temporal(test_year)


