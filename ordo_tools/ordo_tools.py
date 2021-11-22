from datetime import timedelta, datetime
import dateutil.easter
import importlib
import re
from os import listdir

from ordo_tools.settings import YEAR

#===-===-=== GLOBALS ===-===-=== #

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


def global_year(year):
    global YEAR
    YEAR = year

# todo range for pentecost
# todo range for advent
# todo range for paschaltime
# todo range for lent

#===-===-=== CLASSES ===-===-=== #


class Feast:
    def __init__(self, feast_date: str, properties: dict):
        # todo #11 make a method that takes all the adjusted data and returns it as a dictionary
        self.feast_date = feast_date
        self.feast_date_display = datetime.strptime(self.feast_date.strip(
            'tranlsated ._')+'/'+str(YEAR), '%m/%d/%Y').strftime('%a, %b %-d')
        self.feast_properties = properties
        self.name = properties['feast']
        if 'infra_oct_name' in properties.keys():
            self.infra_octave_name = properties['infra_oct_name']
        self.rank_v = properties['rank'][-1]  # verbose
        self.rank_n = properties['rank'][0]   # numeric
        self.mass = {}
        if 'int' in properties['mass'].keys():
            self.mass = {'Ad Missam': properties['mass']}
        else:
            for x, y in properties['mass'].items():
                self.mass.update({x: y})
        self.vespers = properties['vespers'] if 'vespers' in properties.keys(
        ) else {'proper': False, 'admag': '', 'propers': {}, 'oration': ''}
        self.nobility = properties['nobility'] if 'nobility' in properties.keys(
        ) else ('0', '0', '0', '0', '0', '0', )
        self.office_type = properties['office_type']
        self.com_1 = self.Commemoration(
            properties['com_1']) if 'com_1' in properties.keys() else self.Commemoration(dict())
        self.com_2 = self.Commemoration(
            properties['com_2']) if 'com_2' in properties.keys() else self.Commemoration(dict())
        self.com_3 = self.Commemoration(
            properties['com_3']) if 'com_3' in properties.keys() else self.Commemoration(dict())
        self.com_4 = self.Commemoration(
            properties['com_4']) if 'com_4' in properties.keys() else self.Commemoration(dict())
        self.com_5 = self.Commemoration(
            properties['com_5']) if 'com_5' in properties.keys() else self.Commemoration(dict())

    class Commemoration:
        def __init__(self, detail: dict):
            self.details = detail
            self.com_mass = detail['mass'] if 'mass' in detail.keys() else None

        @property
        def com_feast(self) -> str:
            if 'feast' in self.details.keys():
                return '\n[\\textit{' + self.details['feast'] + '}]\n'
            else:
                return ''

        def com_glo_cre(self):
            gloria = self.com_mass['glo']
            creed = self.com_mass['cre']
            status = []
            if gloria == True:
                status.append('G, ')
            if creed == True:
                status.append('C, ')
            return status

        @property
        def com_mass2latex(self) -> str:
            # todo add orations
            latexed_mass = '\\textbf{Ad Missam:} \\textit{' + \
                self.com_mass['int'] + ', } '
            for x in self.com_glo_cre():
                latexed_mass += x
            latexed_mass += 'Præf ' + self.com_mass['pre'] + ', '
            return latexed_mass

    def date(self):
        return datetime.strptime('%m%d', self.feast_date)

    @property
    # todo #9 expand Preces method to provide for 1. Preces Feriales 2. Compline 3. Little Hours
    def preces(self) -> str:
        if self.rank_n <= 16:
            return ''
        else:
            return 'Preces'

    @property
    def feast(self) -> str:
        return self.feast_properties['feast']

    @property
    def updated_properties(self) -> dict:
        dic = {
            'feast': self.name,
            'rank': [self.rank_n, self.rank_v],
            'mass': self.mass,
            'vespers': self.vespers,
            'nobility': self.nobility,
            'office_type': self.office_type,
            'com_1': self.com_1.details,
            'com_2': self.com_2.details,
            'com_3': self.com_3.details,
            'com_4': self.com_4.details,
            'com_5': self.com_5.details,
        }
        return dic

    @property
    def office_type2latex(self) -> str:
        if self.office_type == False:
            off_type = 'Ord'
        elif self.office_type == 'feria':
            off_type = 'Fer'
        elif self.office_type == 'festiva':
            off_type = 'Festiv'
        elif self.office_type == 'dominica':
            off_type = 'Dom'
        else:
            return 'ERROR!'
        return 'Off ' + off_type

    def mass2latex(self) -> str:
        # todo add orations
        latexed_mass = ''
        status = []
        for y in self.mass.values():
            print(self.feast_date, self.mass.values())
            gloria = y['glo']
            creed = y['cre']
            if gloria == True and creed == True:
                status.append('G, C, ')
            elif gloria == True and creed == False:
                status.append('G, ')
            elif gloria == False and creed == True:
                status.append('C, ')
            else:
                status.append('')
        print(self.mass.items())
        i = 0
        for x, y in self.mass.items():
            latexed_mass += '\\textbf{' + x + \
                '}: \\textit{' + y['int'] + ',} ' + \
                status[i] + 'Pre ' + y['pre']
            i += 1
        return latexed_mass

    def commemoration2latex(self):
        com_list = '\n'
        if self.com_1 != False:
            com_list += self.com_1.com_feast
        elif self.com_2 != False:
            com_list += self.com_2.com_feast
        elif self.com_3 != False:
            com_list += self.com_3.com_feast
        elif self.com_4 != False:
            com_list += self.com_4.com_feast
        elif self.com_5 != False:
            com_list += self.com_5.com_feast
        else:
            return com_list + '\n\\textit{No Commemoration}'
        return com_list

#===-===-=== COMMON FUNCTIONS ===-===-=== #


def easter(year: int):
    return datetime(year=int(dateutil.easter.easter(year).strftime('%Y')), month=int(dateutil.easter.easter(year).strftime('%m')), day=int(dateutil.easter.easter(year).strftime('%d')))


def day(year: int, month: int, day: int):
    return datetime(year=year, month=month, day=day)


def week(i: int):
    return timedelta(weeks=i)


def indays(numdays: int):
    return timedelta(days=numdays)


def weekday(date: datetime):
    return date.strftime('%a')


def findsunday(date):
    return timedelta(days=int(date.strftime('%w')))


def find_extra_epiphany(pents):
    if pents == 23:
        pass
    else:
        return pents - 24


def leap_year(year: int):
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


def latex_replacement(string: str):
    return re.sub('&', '\&', re.sub('_', '\_', string))

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
        print('dictionary is in sanctoral/diocese')
        print(name)
        file_name = 'sanctoral/diocese/'+name+'.py'
        mdl_name = 'sanctoral.diocese.'+name
        dict_name = 'sanctoral'
        dict_name_json = 'sanctoral = {'
    elif name == 'temporal':
        print('dictionary is in temporal')
        print(name)
        file_name = 'temporal/'+name+'_'+str(YEAR)+'.py'
        mdl_name = 'temporal.'+name+'_'+str(YEAR)
        dict_name = 'temporal'
        dict_name_json = 'temporal = {'
    elif name == 'calendar':
        print('dictionary is in calendar')
        print(name)
        file_name = 'calen/'+name+'_'+str(YEAR)+'.py'
        mdl_name = 'calen.'+name+'_'+str(YEAR)
        dict_name = 'calen'
        dict_name_json = 'calen = {'
    else:
        print('could not find dictionary: ' + name)
        file_name = ''
        mdl_name = ''
        dict_name = ''
        dict_name_json = ''
    return (file_name, mdl_name, dict_name, dict_name_json)


def commit_to_dictionary(target_file: str, dic: dict) -> None:
    """ Takes a dictionary and writes it to a file.

    Args:
        target_file (str): file to write to
        dic (dict): dictionary to write
    """    
    def write_dictionary(target_file: tuple, dic: dict) -> None:
        """ Writes a dictionary to a file.

        Args:
            target_file (tuple): The name and path of the file to write to.
            dic (dict): dictionary to write

        Returns:
            None: Writes the dictionary to the file with no return.
        """        
        with open(target_file[0], 'a') as f:
            f.truncate(0)  # clean the file
            for i, line in enumerate(sorted(dic)):
                if i != 0:
                    f.write('\''+line+'\' : '+str(dic[line])+',\n')
                else:
                    f.write(target_file[-1])
            f.write('}')
            return 0
    write_dictionary(find_module(target_file), dic)
    return 0


def commemoration_ordering(direct: str) -> None:
    """ Adjusts the ordering of the commeorations so so that the first commemoration is always COM_1

    Args:
        direct (str): dictionary whose commemorations are to be ordered

    Returns:
        None: Commemorations are ordered without return.
    """    
    try:
        mdl = importlib.import_module(direct + str(YEAR))
    except ModuleNotFoundError:
        mdl = importlib.import_module(direct)
    try:
        dic = mdl.temporal
    except AttributeError:
        try:
            dic = mdl.calen
        except AttributeError:
            dic = mdl.sanctoral
        # todo use the Feast class for this
    for x in list(dic.keys()):
        for data in list(dic[x].keys()):
            if 'com_1' in data:
                continue
            elif 'com_2' in data:  # ! use a for loop for this
                dic[x].update({'com_1': dic[x]['com_2']})
                dic[x].pop('com_2')
                if 'com_3' in data:
                    dic[x].update({'com_2': dic[x]['com_3']})
                    dic[x].pop('com_3')
                    if 'com_4' in data:
                        dic[x].update({'com_3': dic[x]['com_4']})
                        dic[x].pop('com_4')
                        if 'com_5' in data:
                            dic[x].update({'com_4': dic[x]['com_5']})
                            dic[x].pop('com_5')
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
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
                                print(x, y)
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
                    # translation
                    if first.rank_n <= 4 and second.rank_n <= 10:
                        dic.update(
                            {first.feast_date.strip(flag): first.feast_properties})
                        dic.update(
                            {second.feast_date.strip(flag)+'_': second.feast_properties})
                    # no commemoration
                    elif first.rank_n <= 4 and second.rank_n > 10:
                        dic.update(
                            {first.feast_date.strip(flag): first.feast_properties})
                    # commemoration
                    # todo refine these ranges:
                    elif 19 > first.rank_n > 4 and 19 > second.rank_n >= 6:
                        first.com_1 = second.feast
                        dic.update(
                            {first.feast_date.strip(flag): first.feast_properties})
                    elif second.rank_n == 22:
                        dic.update(
                            {first.feast_date.strip(flag): first.feast_properties})
                    # no commemoration
                    else:
                        dic.update(
                            {first.feast_date.strip(flag): first.feast_properties})
                    if len(first.feast_date) == 6:
                        dic.pop(first.feast_date)
                    if len(second.feast_date) == 6:
                        dic.pop(second.feast_date)
    commit_to_dictionary(target_file=direct, dic=dic)
    return 0


def stitch(sanctoral: str) -> None:
    """ This function stitches the sanctoral and temporal dictionaries.

    Args:
        sanctoral (str): Sanctoral dictionary for the calendar.

    Returns:
        None: Creates the new calendar without returning anything.
    """    
    mdl_temporal = importlib.import_module(
        'temporal.temporal_'+str(YEAR)).temporal
    mdl_sanctoral = importlib.import_module(
        'sanctoral.diocese.'+sanctoral).sanctoral
    # ! add a method here to add the other modules required for the sanctoral cycle
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


def explode_octaves(region_diocese: str) -> None:
    """ Takes the Octaves in the Sanctoral cycle and explodes them into their days withing the octave.

    Args:
        region_diocese (str): diocese for the calendar to be generated.

    Returns:
        None: The days will be propagated without return.
    """    
    mdl = importlib.import_module(
        'sanctoral.diocese.'+region_diocese).sanctoral
    for x in sorted(mdl):
        feast = Feast(x, mdl[x])
        # todo have the program check the nobility to see if the feast is an octave
        if 'Oct' in feast.rank_v:
            if feast.nobility[2] == 4:  # common octave
                # todo update this to handle every octave type
                for k, y in enumerate(ROMANS[3:6], start=1):
                    feast.name = 'De '+y+' die infra'+feast.infra_octave_name
                    feast.rank_v = 'feria'
                    feast.rank_n = 18
                    mdl.update({str((datetime.strptime(feast.feast_date, '%m/%d')
                                     + indays(k)).strftime('%m/%d')) + '_': feast.updated_properties})
    return None
