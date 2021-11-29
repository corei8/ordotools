from datetime import timedelta, datetime, date
import dateutil.easter
import importlib
import re
from os import listdir
from ordo_tools.settings import YEAR
from ordo_tools.feast import Feast


ROMANS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII',
          'VIII', 'IX', 'X', 'XI', 'XII', 'XIII',
          'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX',
          'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV',
          'XXVI', 'XXVII', 'XXVIII', ]

LENT_MASSES = ('Sicut oculi', 'Domine refugium', 'Reminíscere',  'Confessio', 'De necessitatibus',
               'Intret oratio', 'Redime me', 'Tibi dixit', 'Ne derelinquas me',
               'Deus, in adjutorium', 'Ego autem', 'Lex Domini', 'In Deo laudabo', 'Ego clamavi',
               'Ego autem', 'Salus populi', 'Fac mecum', 'Verba mea', 'Deus, in nomine', 'Exaudi, Deus',
               'Cum sanctificatus', 'Lætetur cor', 'Meditatio', 'Sitientes', 'Miserere mihi',
               'Expecta Dominum', 'Liberator meus', 'Omnia, quæ fecisti', 'Miserere mihi', 'Miserere mihi',)

# beginning with the fourth Sunday after Pentecost
PENTECOST_MASSES = ('Dominus illuminatio', 'Exaudi, Domine', 'Dominus fortitudo', 'Omnes gentes',
                    'Suscepimus', 'Ecce Deus', 'Cum clamarem', 'Deus in loco',
                    'Deus in adjutorium', 'Respice Domine', 'Protector noster', 'Inclina Domine',
                    'Miserere mihi', 'Justus es', 'Da pacem', 'Salus populi',
                    'Omnia', 'In voluntate tua', 'Si iniquitates', 'Dicit Dominus',
                    'Dicit Dominus',)

EPIPHANY_MASSES = ('', )

FERIA = [
    'Feria II',
    'Feria III',
    'Feria IV',
    'Feria V',
    'Feria VI',
    'Sabbatum',
]


def findsunday(date: datetime) -> timedelta:
    """ return the distance of the datetime date from the previous Sunday, as a days timedelta """
    return timedelta(days=int(date.strftime('%w')))


CHRISTMAS = datetime.strptime(str(YEAR) + "-12-25", "%Y-%m-%d")

FIRST_ADVENT = CHRISTMAS - findsunday(CHRISTMAS) - timedelta(weeks=3)


def easter(year: int) -> datetime:
    """ return the date of easter for this year """
    return datetime(
        year=int(dateutil.easter.easter(year).strftime('%Y')),
        month=int(dateutil.easter.easter(year).strftime('%m')),
        day=int(dateutil.easter.easter(year).strftime('%d'))
    )


# ! check this one -- does it start on the following Sunday?
LENT_BEGINS = easter(YEAR) - timedelta(weeks=6, days=4)

LENT_ENDS = easter(YEAR) - timedelta(days=1)

# todo adjust this to use the easter function
EASTER_SEASON_START = datetime(
    year=int(dateutil.easter.easter(YEAR).strftime('%Y')),
    month=int(dateutil.easter.easter(YEAR).strftime('%m')),
    day=int(dateutil.easter.easter(YEAR).strftime('%d'))
) + timedelta(days=8)

EASTER_SEASON_END = datetime(
    year=int(dateutil.easter.easter(YEAR).strftime('%Y')),
    month=int(dateutil.easter.easter(YEAR).strftime('%m')),
    day=int(dateutil.easter.easter(YEAR).strftime('%d'))
) + timedelta(days=39)

# PENTECOST_SEASON_START = easter(YEAR) + week(i+1)

# todo range for pentecost

# todo range for lent


def day(year: int, month: int, day: int) -> datetime:
    return datetime(year=year, month=month, day=day)


def week(i: int) -> timedelta:
    """ return a timedelta week, with integers as the input """
    return timedelta(weeks=i)


def indays(numdays: int) -> timedelta:
    """ return a timedelta day(s), with integers as the input """
    return timedelta(days=numdays)


def weekday(date: datetime) -> str:
    """ return the weekday, with datetime as the input """
    return date.strftime('%a')


def find_extra_epiphany(pents: int) -> int:
    """ return the number of Sundays not celebrated after Epiphany """
    if pents == 23:
        pass
    else:
        return pents - 24


def leap_year(year: int) -> bool:
    """ return true if year is a leap year """
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def latex_replacement(string: str) -> str:
    """ return a string formatted for LaTeX with escape characters """
    return re.sub('&', '\&', re.sub('_', '\_', string))


def translate_month(month: str) -> str:
    """ return the latin name for a given english month """
    months_in_latin = {
        'January': 'Januarius',
        'February': 'Februarius',
        'March': 'Martius',
        'April': 'Aprilis',
        'May': 'Majus',
        'June': 'Junis',
        'July': 'Julius',
        'August': 'Augustus',
    }
    if month in months_in_latin:
        return months_in_latin[month]
    else:
        return month

#===-===-=== HEAVY-HITTING FUNCTIONS ===-===-=== #


def find_module(name: str) -> tuple:
    """ Finds the module and the function within the module.

    Args:
        name (str): Name of the dictionary to find.

    Returns:
        tuple: Contains the name of the module, the function within the module, the name of the dictionary and the file name.
    """
    if '.' in name:
        name = name.split('.')[1].strip('_')
    if name+'.py' in listdir('sanctoral/diocese'):
        file_name = 'sanctoral/diocese/'+name+'.py'
        mdl_name = 'sanctoral.diocese.'+name
        dict_name = 'sanctoral'
        dict_name_json = 'sanctoral = {'
    elif name == 'temporal':
        file_name = 'temporal/'+name+'_'+str(YEAR)+'.py'
        mdl_name = 'temporal.'+name+'_'+str(YEAR)
        dict_name = 'temporal'
        dict_name_json = 'temporal = {'
    elif name == 'calendar':
        file_name = 'calen/'+name+'_'+str(YEAR)+'.py'
        mdl_name = 'calen.'+name+'_'+str(YEAR)
        dict_name = 'calen'
        dict_name_json = 'calen = {'
    else:
        file_name = ''
        mdl_name = ''
        dict_name = ''
        dict_name_json = ''
    return (file_name, mdl_name, dict_name, dict_name_json)

# todo maybe use a decorator to make this more readable?


def commit_to_dictionary(target_file: str, dic: dict) -> None:
    """ Takes a dictionary and writes it to a file.

    Args:
        target_file (str): file to write to
        dic (dict): dictionary to write
    """
    # def write_dictionary(dict_data: tuple, dic: dict) -> None:
    #     """ Writes a dictionary to a file """
    #     # ? do we have to write to a file every time?
    #     with open(dict_data[0], 'a') as f:
    #         f.truncate(0)  # clean the file
    #         for i, line in enumerate(sorted(dic)):
    #             if i != 0:
    #                 f.write('\''+line+'\' : '+str(dic[line])+',\n')
    #             else:
    #                 f.write(dict_data[-1]+'\''+line +
    #                         '\' : '+str(dic[line])+',\n')
    #         f.write('}')
    #         return None
    # # write_dictionary(find_module(target_file), dic)
    # todo update the parent funtion to use the children dependent upon the target_file
    def update_calendar(data: dict) -> None:
        """ Updates the calendar file """
        cal = importlib.import_module('calen.calendar_'+str(YEAR)).calen
        for x, y in data.items():
            cal.update({x: y})
        with open('calen/calendar_'+str(YEAR)+'.py', 'a') as f:
            f.truncate(0)
            f.write('calen = {\n')
            for i, line in enumerate(sorted(cal)):
                if i != 0:
                    f.write('\''+line+'\' : '+str(cal[line])+',\n')
                else:
                    f.write('\''+line+'\' : '+str(cal[line])+',\n')
            f.write('}')
        return None

    update_calendar(data=dic)

    return None


def explode_octaves(region_diocese: str) -> dict:
    """ Takes the Octaves in the Sanctoral cycle and explodes them into their days within the octave.

    Args:
        region_diocese (str): diocese for the calendar to be generated.

    Returns:
        Dict: Dictionary to be stitched to the temporal calendar.
    """
    mdl = importlib.import_module(
        'sanctoral.diocese.'+region_diocese).sanctoral
    return_dict = {}
    for x in sorted(mdl):
        feast = Feast(x, mdl[x])
        if 'Oct' in feast.rank_v:
            if feast.nobility[2] == 4:  # common octave
                # todo update this to handle every octave type
                for k, y in enumerate(ROMANS[3:6], start=1):
                    feast.name = 'De '+y+' die infra '+feast.infra_octave_name
                    feast.rank_v = 'feria'
                    feast.rank_n = 18
                    return_dict.update({str((datetime.strptime(feast.feast_date, '%m/%d') +
                                             indays(k)).strftime('%m/%d'))+'_': feast.updated_properties})
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
    """ Takes two feasts and returns the one with the higher rank.

    Args:
        feast_1 (Feast): First feast to be compared.
        feast_2 (Feast): Second feast to be compared.

    Returns:
        dict: dictionary of the higher ranked feast and the transfered feast.
    """
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


def rank_occurring_feasts(date: str, sanctoral_feast: dict, temporal_feast: dict) -> dict:
    """ This function ranks the feasts occurring on a given date.

    Args:
        date (str): Date for which the feasts are to be ranked.
        sanctoral_feast (dict): Sanctoral feast dictionary.
        temporal_feast (dict): Temporal feast dictionary.
    """
    ranked_feasts = {}
    sanct = Feast(date, sanctoral_feast)
    tempo = Feast(date, temporal_feast)
    if sanct.rank_n == tempo.rank_n:
        # nobility check
        transfer_date = datetime.strptime(date, '%m/%d')+timedelta(days=1)
        print(date)
        ranked_feasts.update(
            {
                date: rank_by_nobility(sanct, tempo)['higher'].feast_properties,
                transfer_date.strftime('%m/%d'): rank_by_nobility(sanct, tempo)['lower'].feast_properties,
            }
        )
    else:
        candidates = {
            sanct.rank_n: sanct,
            tempo.rank_n: tempo,
        }
        higher = candidates[sorted(candidates)[0]]
        lower = candidates[sorted(candidates)[1]]
        if higher.rank_n <= 4:  # feasts that exclude commemorations
            # transfer
            if lower.rank_n <= 10:
                transfer_date = (datetime.strptime(date, '%m/%d') +
                                 timedelta(days=1)).strftime('%m/%d')
                ranked_feasts.update({transfer_date: lower.feast_properties})
            else:
                pass  # lesser feast can be ignored
            ranked_feasts.update({date: higher.feast_properties})
        elif 14 <= lower.rank_n <= 16:  # impeded double majors, doubles and semidoubles
            # todo exclude this commemoration in privileged feasts, etc. p. 309 Matters Liturgical
            if higher.rank_n == 12 or 19:
                ranked_feasts.update(
                    {date: add_commemoration(
                        feast=higher, commemoration=lower)}
                )
            elif higher.rank_n < higher.rank_n:
                ranked_feasts.update(
                    {date: add_commemoration(
                        feast=higher, commemoration=lower)}
                )
            else:
                pass
        else:
            ranked_feasts.update({date: higher.feast_properties})
    return ranked_feasts


def add_sanctoral_feasts(temporal_dict: dict, sanctoral_dict: dict) -> dict:
    """ Adds the sanctoral feasts to the temporal feast dictionary.

    Args:
        temporal_dict (dict): Temporal feast dictionary.
        sanctoral_feast (dict): Sanctoral feast dictionary.
    """
    sanctoral = sanctoral_dict.copy()
    temporal = temporal_dict.copy()
    full_calendar = {}
    for x in sanctoral.keys():
        if x in temporal.keys():
            ranked_feast = rank_occurring_feasts(
                date=x, sanctoral_feast=sanctoral[x], temporal_feast=temporal[x]
            )
            full_calendar.update(ranked_feast)
        else:
            full_calendar.update({x: sanctoral[x]})
    return full_calendar


def dict_clean(direct: str, str_flag: str) -> None:
    """ Resolves conflicts between the sanctoral and temporal dictionaries, which are flagged with either a period or an underscore.

    Args:
        direct (str): The calendar to be cleaned.
        str_flag (str): The flag to be used to identify the conflicts, either . or _.
    """
    dict_information = find_module(direct)
    dictionary = importlib.import_module(dict_information[1])
    dic = dictionary.__dict__[dict_information[2]]
    flag = str_flag
    for x in sorted(dic):
        if flag in x:
            continue
        if x+flag in sorted(dic):
            rank_occurring_feasts(
                date=x, sanctoral_feast=dic[x], temporal_feast=dic[x+flag])
    else:
        commit_to_dictionary(target_file=direct, dic=dic)
    return 0


def dict_clean_mini(direct: str, str_flag: str) -> None:
    """ Resolves conflicts in a single file, which are flagged with either a period or an underscore.

    Args:
        direct (str): The calendar to be cleaned.
        str_flag (str): The flag to be used to identify the conflicts, either . or _.
    """
    dict_information = find_module(direct)
    dictionary = importlib.import_module(dict_information[1])
    dic = dictionary.__dict__[dict_information[2]]
    flag = str_flag
    list_of_keys = [k for k in dic.keys()]
    for x in list_of_keys:
        if flag in x:
            continue
        if x+flag in dic.keys():
            new_rank = rank_occurring_feasts(
                date=x, sanctoral_feast=dic[x], temporal_feast=dic[x+flag]
                )
            dic.update(new_rank)
            del dic[x+flag]
    else:
        return dic


def leap_year_solver(dic: dict) -> dict:
    # if status == True:
    #     # solve the leap year problem
    #     return dic
    # else:
    #     for x in sorted(dic):
    #             if x+'.' in sorted(dic):
    #                 cleaned_date = rank_occurring_feasts(
    #                     date=x,
    #                     sanctoral_feast=dic[x],
    #                     temporal_feast=dic[x+'.']
    #                 )
    #                 dic.update(cleaned_date)
    #                 del dic[x+'.']
    #             else:
    #                 pass
    return dic

def stitch_calendars(direct: str) -> None:
    """ stitch the temporal and sanctoral calendars together 

    Args: 
        direct (str): dictionary name of the sanctoral calendar
    """
    temp_dict_information = find_module('calendar')
    temp_dictionary = importlib.import_module(temp_dict_information[1])
    temporal = temp_dictionary.__dict__[temp_dict_information[2]]
    # assume that the temporal calendar is already cleaned and correctly ordered
    if leap_year(YEAR) == True:
        pass  # work on this later
        # update the calendar with the leap year feasts
    else:
        sanctoral = dict_clean_mini(direct, '.')
        full_calendar = add_sanctoral_feasts(temporal, sanctoral).copy()
        for y in temporal.keys():
            if len(y) == 6: 
                print(f'problem with {y}')
            if y in sanctoral.keys():
                continue
            else:
                full_calendar.update({y: temporal[y]})
    commit_to_dictionary(
        target_file='calendar',
        dic=full_calendar,
    )
    return None


def our_ladys_saturday(direct: str) -> None:
    """ Adds all the Saturday Offices of the Blessed Virgin to the temporal calendar """
    # todo add mass number according to season
    office = {
        'feast': 'De Sancta Maria in Sabbato',
        'rank': [21, 's'],
        'color': 'white',
        'mass': {'int': 'Salve sancta parens', 'glo': True, 'cre': False, 'pre': 'de B Maria Virg (et te in Veneratione)'},
        'com_1': {'oration': 'Deus qui corda', },
        'com_2': {'oration': 'Ecclesiæ', },
        'matins': {},
        'lauds': {},
        'prime': {'responsory': 'Qui natus est', 'preces': True},
        'little_hours': {},
        'vespers': {'proper': False, 'admag': ('firstVespers', 'secondVerspers'), 'propers': {}, 'oration': ''},
        'compline': {},
        'office_type': 'ut in pr loco',
        'nobility': (8, 2, 6, 13, 3, 0,),
    }
    dict_information = find_module(direct)
    dictionary = importlib.import_module(dict_information[1])
    dic = dictionary.__dict__[dict_information[2]]
    # todo add ranges where Our Lady's Saturday is impossible (Advent, Lent, Ember Days, Vigils)
    begin_year = date(YEAR, 1, 1)
    if begin_year.strftime('%A') == 'Saturday':
        saturday = begin_year
    else:
        saturday = begin_year - indays(findsunday(begin_year)+6)
    while saturday <= date(YEAR, 12, 31):
        try:
            saturday_in_temporal = Feast(feast_date=saturday.strftime(
                '%m%d'), properties=dic[saturday.strftime('%m/%d')])
        except KeyError:
            if saturday.strftime('%m/%d')+'.' in sorted(dic):
                pass  # we can presume that it is impossible
            else:
                dic.update({saturday.strftime('%m/%d'): office})
        else:
            dic.update(
                rank_occurring_feasts(date=saturday.strftime(
                    '%m/%d'), sanctoral_feast=office, temporal_feast=saturday_in_temporal.feast_properties)
            )
        saturday = saturday + indays(7)
    commit_to_dictionary(target_file='calendar', dic=dic)
    return None


def commit_temporal() -> None:
    from ordo_tools.temporal_cycle import build_temporal
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
