from datetime import date
from datetime import datetime
from datetime import timedelta

from ordo_tools.helpers import days
from ordo_tools.helpers import advance_a_day
from ordo_tools.helpers import leap_year
from ordo_tools.helpers import findsunday
from ordo_tools.helpers import LENT_ENDS
from ordo_tools.helpers import LENT_BEGINS
from ordo_tools.helpers import LAST_ADVENT
from ordo_tools.helpers import FIRST_ADVENT


from ordo_tools.feast import Feast
from ordo_tools.settings import YEAR
from ordo_tools.temporal import Temporal
from sanctoral.diocese.roman import Sanctoral

from os import listdir

import importlib

from ordo_tools.parts import ROMANS




# def mart_letter(year) -> str:
#     """ Find the letter of the martyrology for a given year """
#     golden_number = (year + 1) % 19
#     if golden_number == 0:  # ? is this true?
#         golden_number = 19
#     return golden_number


# MARTYROLOGY = (lambda year: mart_letter(year))(YEAR)


def find_module(name: str) -> tuple:
    """
    Finds the module and the function within the module.
    """
    if '.' in name:
        name = name.split('.')[1].strip('_')
    if name + '.py' in listdir('sanctoral/diocese'):
        file_name = 'sanctoral/diocese/' + name + '.py'
        mdl_name = 'sanctoral.diocese.' + name
        dict_name = 'sanctoral'
        dict_name_json = 'sanctoral = {'
    elif name == 'temporal':
        file_name = 'temporal/' + name + '_' + str(YEAR) + '.py'
        mdl_name = 'temporal.' + name + '_' + str(YEAR)
        dict_name = 'temporal'
        dict_name_json = 'temporal = {'
    elif name == 'calendar':
        file_name = 'calen/' + name + '_' + str(YEAR) + '.py'
        mdl_name = 'calen.' + name + '_' + str(YEAR)
        dict_name = 'calen'
        dict_name_json = 'calen = {'
    else:
        file_name = ''
        mdl_name = ''
        dict_name = ''
        dict_name_json = ''
    return (file_name, mdl_name, dict_name, dict_name_json)

# TODO: maybe use a decorator to make this more readable?


def commit_to_dictionary(target_file: str, dic: dict) -> None:
    """
    Takes a dictionary and writes it to a file.
    """
    
    def update_calendar(data: dict) -> dict:
        """
        Updates the calendar file
        """
        cal = {}
        for x, y in data.items():
            cal.update({x: y})
        with open('calen/calendar_' + str(YEAR) + '.py', 'a') as f:
            f.truncate(0)
            f.write('from ordo_tools.helpers import day\n\n')
            f.write("class LiturgicalCalendar:\n\n")
            f.write("\tdef __init__(self):\n")
            f.write('\t\tself.data = {\n')
            for i, line in enumerate(sorted(cal)):
                date = f"""\t\t\tday(year={YEAR}, month={line.strftime('%m').lstrip('0')}, day={line.strftime('%d').lstrip('0')})"""
                if i != 0:
                    f.write(f"{date}: {cal[line]},\n")
                else:
                    f.write(f"{date}: {cal[line]},\n")
            f.write('\t\t}\n\n')
            f.write('\t\tdef data(self) -> dict:\n')
            f.write('\t\t\treturn self.data')

        return None

    update_calendar(data=dic)

    return dic


def explode_octaves(region_diocese: str) -> dict:
    # todo reimplement this to have a seperate dictionary for these
    """ Takes the Octaves in the Sanctoral cycle and explodes them into
    their days within the octave."""
    mdl = importlib.import_module(
        'sanctoral.diocese.' + region_diocese).sanctoral
    return_dict = {}
    for x in sorted(mdl):
        feast = Feast(x, mdl[x])
        if 'Oct' in feast.rank_v:
            if feast.nobility[2] == 4:  # common octave
                # todo update this to handle every octave type
                # * this is an ok use of ROMANS
                for k, y in enumerate(ROMANS[3:6], start=1):
                    feast.name = 'De ' + y + ' die infra '
                    + feast.infra_octave_name
                    feast.rank_v = 'feria'
                    feast.rank_n = 18
                    return_dict.update(
                        {
                            str((datetime.strptime(feast.feast_date, '%m/%d')
                                + days(k)).strftime('%m/%d')) + '_':
                            feast.updated_properties
                        }
                    )
        else:
            return_dict.update({feast.feast_date: feast.feast_properties})
    return return_dict


def add_commemoration(feast: Feast, commemoration: Feast) -> dict:
    """ Adds one feast as the commemoration of another feast """
    for x in feast.coms.keys():
        if feast.coms[x] == '':
            feast.coms[x] = commemoration.feast_properties
            break
        else:
            pass
    return feast.updated_properties

# * maybe use recursion to solve problems with transfers?


def rank_by_nobility(feast_1: Feast, feast_2: Feast) -> dict:
    """ Takes two feasts and returns the one with the higher rank."""
    ranks_1 = feast_1.nobility
    ranks_2 = feast_2.nobility
    for x in range(len(ranks_1)):
        if ranks_1[x] < ranks_2[x]:
            return {'higher': feast_1, 'lower': feast_2}
        elif ranks_1[x] > ranks_2[x]:
            return {'higher': feast_2, 'lower': feast_1}
        else:
            pass
    return {'higher': feast_1, 'lower': feast_2}


transfer_dict = {}

# * TRY to use ranges for special times: regualar, epiphnay, etc.


def rank_occurring_feasts(
        date: str,
        sanctoral_feast: dict,
        temporal_feast: dict
) -> dict:
    """ This function ranks the feasts occurring on a given date."""
    ranked_feasts = {}
    sanct = Feast(date, sanctoral_feast)
    tempo = Feast(date, temporal_feast)
    if sanct.rank_n == tempo.rank_n:
        transfer_date = date+timedelta(days=1)
        ranked_feasts.update(
            {
                date: rank_by_nobility(
                    sanct, tempo)['higher'].feast_properties,
                transfer_date: rank_by_nobility(
                    sanct, tempo)['lower'].feast_properties,
            }
        )
    else:
        candidates = {
            sanct.rank_n: sanct,
            tempo.rank_n: tempo,
        }
        higher = candidates[sorted(candidates)[0]]
        lower = candidates[sorted(candidates)[1]]
        if lower == 22:  # take care of simple feasts
            pass
        if higher.rank_n <= 4:  # feasts that exclude commemorations
            if lower.rank_n <= 10:
                ranked_feasts.update({date: higher.feast_properties})
                transfer_dict.update({date: lower.feast_properties})
            else:
                ranked_feasts.update({date: higher.feast_properties})
        elif 14 <= lower.rank_n <= 16:  # impeded dm, d and sd
            # see p. 309 Matters Liturgical
            if higher.rank_n == 12 or 19:
                ranked_feasts.update(
                    {date: add_commemoration(
                        feast=higher, commemoration=lower)}
                )
            else:
                ranked_feasts.update(
                    {date: add_commemoration(
                        feast=higher, commemoration=lower)}
                )
        else:
            ranked_feasts.update(
                {date: add_commemoration(feast=higher, commemoration=lower)}
            )
    return ranked_feasts


def add_sanctoral_feasts(temporal_dict: dict, sanctoral_dict: dict) -> dict:
    """
    Adds the sanctoral feasts to the temporal feast dictionary.
    """
    sanctoral = sanctoral_dict.copy()
    temporal = temporal_dict.copy()
    full_calendar = {}
    for x in sanctoral.keys():
        if x in temporal.keys():
            ranked_feast = rank_occurring_feasts(
                date=x,
                sanctoral_feast=sanctoral[x],
                temporal_feast=temporal[x]
            )
            full_calendar.update(ranked_feast)
        else:
            full_calendar.update({x: sanctoral[x]})
    return full_calendar


def dict_clean(direct: str, str_flag: str) -> None:
    """
    Resolves conflicts between the sanctoral and temporal dictionaries,
    which are flagged with either a period or an underscore.
    """
    dict_information = find_module(direct)
    dictionary = importlib.import_module(dict_information[1])
    try:
        dic = dictionary.__dict__[dict_information[2]]
    except KeyError:
        pass
    else:
        flag = str_flag
        for x in sorted(dic):
            if flag in x:
                continue
            if x + flag in sorted(dic):
                rank_occurring_feasts(
                    date=x,
                    sanctoral_feast=dic[x],
                    temporal_feast=dic[x + flag]
                )
        else:
            commit_to_dictionary(target_file=direct, dic=dic)
    return 0


def dict_clean_mini(direct: str, str_flag: str) -> None:
    """
    Resolves conflicts in a single file, which are flagged with either
    a period or an underscore.
    """
    dict_information = find_module(direct)
    dictionary = importlib.import_module(dict_information[1])
    dic = dictionary.__dict__[dict_information[2]]
    flag = str_flag
    list_of_keys = [k for k in dic.keys()]
    for x in list_of_keys:
        if flag in x:
            continue
        if x + flag in dic.keys():
            new_rank = rank_occurring_feasts(
                date=x, sanctoral_feast=dic[x], temporal_feast=dic[x + flag]
            )
            dic.update(new_rank)
            del dic[x + flag]
    else:
        return dic


def leap_year_solver(dic: dict) -> dict:
    """ Solves the leap year problem. """
    return dic


def transfer_feasts(dic: dict) -> dict:
    """ Solves the transfer feast problem. """
    for x in transfer_dict.keys():
        trans_feast = Feast(x, transfer_dict[x])
        # look one day ahead
        target_date = advance_a_day(trans_feast.date)
        if target_date not in dic.keys():
            dic.update(target_date, trans_feast.feast_properties)
        else:
            # ! apply the ranking rules
            pass
    return dic


# TODO: this might be a real piece of work to try to salvage

def stitch_calendars(diocese='roman') -> None:
    """ Stitches the temporal and sanctoral calendars together. """

    temporal = Temporal(YEAR).return_temporal()

    # if leap_year(YEAR):
    #     # TODO: add the leapyear changes
    #     pass
    # else:
    #     # sanctoral = dict_clean_mini(diocese, '.')
        # TEST:
    if diocese == 'roman':
        sanctoral = Sanctoral(YEAR).data if leap_year(YEAR) is False else Sanctoral(YEAR).leapyear()
    else:
        pass # this will be a headache
    full_calendar = add_sanctoral_feasts(temporal, sanctoral).copy()
    for y in temporal.keys():
        # if len(y) == 6:
        #     pass
        if y in sanctoral.keys():
            continue
        else:
            full_calendar.update({y: temporal[y]})

    if len(transfer_dict) > 0:
        pass
        full_calendar = transfer_feasts(full_calendar)
    else:
        pass

    return commit_to_dictionary(
        target_file='calendar',
        dic=full_calendar,
    )


def our_ladys_saturday(direct: str) -> None:
    """ Adds all the Saturday Offices of the Blessed Virgin
     to the temporal calendar """
    # todo add mass number according to season
    office = {
        'feast': 'De Sancta Maria in Sabbato',
        'rank': [21, 's'],
        'color': 'white',
        'mass': {
            'int': 'Salve sancta parens',
            'glo': True,
            'cre': False,
            'pre': 'de B Maria Virg (et te in Veneratione)'
        },
        'com_1': {'oration': 'Deus qui corda', },
        'com_2': {'oration': 'Ecclesiæ', },
        'matins': {},
        'lauds': {},
        'prime': {'responsory': 'Qui natus est', 'preces': True},
        'little_hours': {},
        'vespers': {
            'proper': False,
            'admag': ('firstVespers', 'secondVerspers'),
            'propers': {},
            'oration': ''
        },
        'compline': {},
        'office_type': 'ut in pr loco',
        'nobility': (8, 2, 6, 13, 3, 0,),
    }
    dict_information = find_module(direct)
    dictionary = importlib.import_module(dict_information[1])
    dic = dictionary.__dict__[dict_information[2]]
    begin_year = date(YEAR, 1, 1)
    if begin_year.strftime('%A') == 'Saturday':
        saturday = begin_year
    else:
        saturday = begin_year - days(findsunday(begin_year) + 6)
    while saturday <= date(YEAR, 12, 31):
        if LENT_BEGINS.date() <= saturday <= LENT_ENDS.date():
            saturday += days(7)
            continue
        elif FIRST_ADVENT.date() <= saturday <= LAST_ADVENT.date():
            saturday += days(7)
            continue
        # todo #19 #18 also Ember Days, Vigils
        else:
            try:
                saturday_in_temporal = Feast(feast_date=saturday.strftime(
                    '%m%d'), properties=dic[saturday.strftime('%m/%d')])
            except KeyError:
                if saturday.strftime('%m/%d') + '.' in sorted(dic):
                    pass  # we can presume that it is impossible
                else:
                    dic.update({saturday.strftime('%m/%d'): office})
            else:
                dic.update(
                    rank_occurring_feasts(
                        date=saturday.strftime('%m/%d'),
                        sanctoral_feast=office,
                        temporal_feast=saturday_in_temporal.feast_properties
                    )
                )
            saturday = saturday + days(7)
    commit_to_dictionary(target_file='calendar', dic=dic)
    return None


def commit_temporal() -> None:
    """
    Commits the temporal calendar to the temporal dictionary.
    """
    from temporal_cycle import build_temporal
    cycle = build_temporal(YEAR)
    gen_file = "temporal/temporal_" + str(YEAR)
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
    our_ladys_saturday('temporal')

    return None

def build(diocese='roman', country=None) -> dict:
    return stitch_calendars(diocese=diocese)

# def liturgical_calendar(year: int):
#     return importlib.import_module(f'calen.calendar_{year}').LiturgicalCalendar

