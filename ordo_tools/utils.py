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
    def write_dictionary(target_file: tuple, dic: dict) -> None:
        """ Writes a dictionary to a file """
        with open(target_file[0], 'a') as f:
            f.truncate(0)  # clean the file
            for i, line in enumerate(sorted(dic)):
                if i != 0:
                    f.write('\''+line+'\' : '+str(dic[line])+',\n')
                else:
                    f.write(target_file[-1]+'\''+line +
                            '\' : '+str(dic[line])+',\n')
            f.write('}')
            return 0
    write_dictionary(find_module(target_file), dic)
    return 0


def dict_clean(direct: str, str_flag: str) -> None:
    """ Resolves conflicts between the sanctoral and temporal dictionaries, which are flagged with either a period or an underscore.

    Args:
        direct (str): The calendar to be cleaned.
        str_flag (str): The flag to be used to identify the conflicts, either . or _.

    Returns:
        None: Confliecs are resolved without return.
    """
    dict_information = find_module(direct)
    dictionary = importlib.import_module(dict_information[1])
    dic = dictionary.__dict__[dict_information[2]]
    flag = str_flag
    for x in sorted(dic):
        nobility_free = True
        if len(x) >= 6:
            continue
        else:
            second_ = Feast(x, dic[x])
            if not second_.feast_date+flag in sorted(dic):
                continue
            else:
                second_ = Feast(x, dic[x])
                first_ = Feast(second_.feast_date+flag,
                               dic[second_.feast_date+flag])
                if second_.rank_n > first_.rank_n:
                    first, second = first_, second_
                elif second_.rank_n == first_.rank_n:
                    less_noble, more_noble = first_, second_
                    for x, y in zip(
                        second_.nobility,
                        first_.nobility
                    ):
                        for i in range(6):
                            if x == y:
                                continue
                            elif x != y:
                                if x > y:
                                    less_noble, more_noble = first_, second_
                                    break
                                else:
                                    less_noble, more_noble = second_, first_
                                    break
                        else:
                            pass
                    rank = second_.rank_n
                    if rank <= 10:  # ! refine this to exclude all but D1 and D2
                        dic.update(
                            {more_noble.feast_date.strip(
                                flag): more_noble.feast_properties}
                        )
                        dic.update(
                            {less_noble.feast_date.strip(
                                flag)+' tranlsated': less_noble.feast_properties}
                        )
                    else:
                        more_noble.com_1 = {
                            'com_1': less_noble.feast_properties}
                        dic.update({more_noble.feast_date.strip(
                            flag): more_noble.feast_properties})
                    if len(more_noble.feast_date) == 6:
                        dic.pop(more_noble.feast_date)
                    if len(less_noble.feast_date) == 6:
                        dic.pop(less_noble.feast_date)
                    nobility_free = False
                    pass
                else:
                    first, second = second_, first_
                if nobility_free == False:
                    pass
                else:
                    # * translation
                    # ! is this still working for the translations?
                    if first.rank_n <= 4 and second.rank_n <= 10:
                        dic.update(
                            {first.feast_date.strip(flag): first.feast_properties})
                        dic.update(
                            {second.feast_date.strip(flag)+'_': second.feast_properties})
                    # * no commemoration
                    elif first.rank_n <= 4 and second.rank_n > 10:
                        dic.update(
                            {first.feast_date.strip(flag): first.feast_properties})
                    # * commemoration
                    # todo refine these ranges:
                    elif 19 > first.rank_n > 4 and 19 > second.rank_n >= 6:
                        first.com_1 = second.feast
                        dic.update(
                            {first.feast_date.strip(flag): first.feast_properties})
                    elif second.rank_n == 22:
                        dic.update(
                            {first.feast_date.strip(flag): first.feast_properties})
                    # * no commemoration
                    else:
                        dic.update(
                            {first.feast_date.strip(flag): first.feast_properties})
                    if len(first.feast_date) == 6:
                        dic.pop(first.feast_date)
                    if len(second.feast_date) == 6:
                        dic.pop(second.feast_date)
    commit_to_dictionary(target_file=direct, dic=dic)
    return 0


def stitch(sanctoral: dict) -> None:
    """ This function stitches the sanctoral and temporal dictionaries.

    Args:
        sanctoral (str): Sanctoral dictionary for the calendar.

    Returns:
        None: Creates the new calendar without returning anything.
    """
    mdl_temporal = importlib.import_module(
        'temporal.temporal_'+str(YEAR)).temporal
    mdl_sanctoral = sanctoral
    # todo add a method here to add the other modules required for the sanctoral cycle
    mdlt, mdls = sorted(mdl_temporal), sorted(mdl_sanctoral)
    calen = {}
    if leap_year(YEAR) == False:
        pass
    else:
        for event in mdls:
            if not 'leapdate' in mdl_sanctoral[event]:
                pass
            else:
                new_date = mdl_sanctoral[event].get('leapdate')
                mdl_sanctoral.update({new_date if not new_date in mdl_sanctoral else (
                    new_date+'.' if not new_date+'.' in mdl_sanctoral else new_date+'_'): mdl_sanctoral[event]})
    for x in mdls:
        feast = Feast(x, mdl_sanctoral[x])
        calen.update(
            {feast.feast_date+'.' if x in mdlt else feast.feast_date: feast.feast_properties}
        )
    for y in mdlt:
        feast = Feast(y, mdl_temporal[y])
        calen.update({feast.feast_date: feast.feast_properties})
    commit_to_dictionary(target_file='calendar', dic=calen)
    return 0


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
        if feast.coms[x] != '':
            pass
        else:
            feast.coms.update({x: commemoration.feast_properties})
        return feast
    

def rank_occurring_feasts(date: str, sanctoral_feast: dict, temporal_feast: dict) -> dict:
    """ This function ranks the feasts occurring on a given date.

    Args:
        date (str): Date for which the feasts are to be ranked.
    """ 
    ranked_feasts = {}
    sanct = Feast(date, sanctoral_feast)
    tempo = Feast(date, temporal_feast)
    if sanct.rank_n == tempo.rank_n:
        pass # nobility check
    else:
        higher = max(sanct.rank_n, tempo.rank_n)
        lower = min(sanct.rank_n, tempo.rank_n)
        if higher >= 4:
            if lower >= 10:
                lower_date = (datetime.strptime(date, '%m/%d')+timedelta(days=1)).strftime('%m/%d')
                ranked_feasts.update({lower_date: lower.feast_properties})
            else:
                pass
            ranked_feasts.update({date: higher.feast_properties})
        elif higher >= 10:
            if lower >= 10:
                # transfer the feast
                lower_date = (datetime.strptime(date, '%m/%d')+timedelta(days=1)).strftime('%m/%d')
                ranked_feasts.update({lower_date: lower.feast_properties})
            elif 10 < lower >= 16:
                # commemorate the feast
                ranked_feasts.update(
                    {date: add_commemoration(feast=higher, commemoration=lower)}
                    )
            ranked_feasts.update({date: higher.feast_properties})
            ranked_feasts.update({date: sanct.feast_properties})
    return ranked_feasts
    
    
    

def stitch_calendars(direct: dict) -> None:
    """ stitch the temporal and sanctoral calendars together """
    dict_information = find_module(direct)
    dictionary = importlib.import_module(dict_information[1])
    sanctoral = dictionary.__dict__[dict_information[2]]
    temporal = importlib.import_module('calendar_'+str(YEAR)).calendar
    # assume that the temporal calendar is already cleaned and correctly ordered
    full_calendar = {}
    if leap_year(YEAR) == True:
        pass
    for x in sanctoral.keys():
        if x not in temporal.keys():
            full_calendar.update({x: sanctoral[x]})
        elif x in temporal.keys():
            pass # check the ranking
        else:
            print("WARNING! problem with " + x + " in the temporal calendar -- stitch_calendars().")
    else:
        commit_to_dictionary(target_file='calendar', dic=full_calendar)
    return None            
            
    

def our_ladys_saturday(direct: str) -> None:
    """ Adds all the Saturday Offices of the Blessed Virgin to the temporal calendar """
    # todo add mass number according to season
    office = {
        'feast': 'De Sancta Maria in Sabbato',
        'rank': [20, 's'],
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
        if saturday.strftime('%m/%d') in sorted(dic):
            if not saturday.strftime('%m/%d')+'.' in sorted(dic):
                dic.update({saturday.strftime('%m/%d')+'.': office})
            else:
                pass  # we can presume that it is impossible
        else:
            dic.update({saturday.strftime('%m/%d'): office})
        saturday = saturday + indays(7)
    commit_to_dictionary(target_file='calendar', dic=dic)
    return None
