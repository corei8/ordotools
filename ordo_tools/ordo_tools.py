from datetime import timedelta, datetime
import dateutil.easter
import importlib
import re

#===-===-=== GLOBALS ===-===-=== #

ROMANS = ["I", "II", "III", "IV", "V", "VI", "VII",
          "VIII", "IX", "X", "XI", "XII", "XIII",
          "XIV", "XV", "XVI", "XVII", "XVIII", "XIX",
          "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV",
          "XXVI", "XXVII", "XXVIII", ]

#===-===-=== CLASSES ===-===-=== #


class Feast:
    def __init__(self, feast_date: str, properties: dict):
        self.feast_date = feast_date
        self.name = properties['feast']
        print(self.name)
        self.properties = properties
        self.mass = properties['mass'] if not 'Ad Primam Missam' in self.properties['mass'].keys(
        ) else False
        self.tri_mass = properties['mass'] if self.mass == False else False
        self.vespers = properties['vespers'] if 'vespers' in properties.keys(
        ) else {'proper': False, 'admag': '', 'propers': {}, 'oration': ''}
        self.nobility = properties['nobility'] if 'nobility' in properties.keys(
        ) else ('0', '0', '0', '0', '0', '0', )
        self.com_1 = self.Commemoration(
            properties['com_1']) if 'com_1' in properties.keys() else False
        self.com_2 = self.Commemoration(
            properties['com_2']) if 'com_2' in properties.keys() else False
        self.com_3 = self.Commemoration(
            properties['com_3']) if 'com_3' in properties.keys() else False
        self.com_4 = self.Commemoration(
            properties['com_4']) if 'com_4' in properties.keys() else False
        self.com_5 = self.Commemoration(
            properties['com_5']) if 'com_5' in properties.keys() else False
        self.office_type = properties['office_type']

    class Commemoration:
        def __init__(self, detail: dict):
            self.details = detail
            # self.com_mass = detail['mass']

        def feast(self):
            # ! make all the results of commemorations dictionaries
            return self.details['feast'] if type(self.details) == dict else self.details

    def date(self):
        return datetime.strptime('%m%d', self.feast_date)

    def feast(self):
        return self.properties['feast']

    def office_type2latex(self):
        if self.office_type == False:
            off_type = 'Ord'
        elif self.office_type == 'feria':
            off_type = 'Fer'
        elif self.office_type == 'festiva':
            off_type = 'Festiv'
        elif self.office_type == 'dominica':
            off_type = 'Dom'
        else:
            return 0
        return 'Off ' + off_type

    def rank(self, visual: bool):
        if visual == True:
            return self.properties['rank'][-1]
        else:
            return self.properties['rank'][0]

    def introit(self):
        if self.mass != False:
            return self.mass['int']
        else:
            return False

    def glo_cre(self):
        gloria = self.mass['glo']
        creed = self.mass['cre']
        status = []
        if gloria == True:
            status.append('G, ')
        if creed == True:
            status.append('C, ')
        return status

    def mass2latex(self):
        # todo add orations
        if self.mass != False:
            latexed_mass = '\\textbf{Ad Missam:} \\textit{' + \
                self.mass['int'] + ', } '
            for x in self.glo_cre():
                latexed_mass += x
            latexed_mass += 'Præf ' + self.mass['pre'] + ', '
        else:
            latexed_mass = ''
            for x in self.tri_mass.keys():
                latexed_tri_mass = '\\textbf{' + x + ':} \\textit{' + \
                    self.tri_mass[x]['int'] + ', } '
                gloria = self.tri_mass[x]['glo']
                creed = self.tri_mass[x]['cre']
                status = []
                if gloria == True:
                    status.append('G, ')
                if creed == True:
                    status.append('C, ')
                for i in status:
                    latexed_tri_mass += i
                latexed_tri_mass += 'Præf ' + self.tri_mass[x]['pre'] + ', '
                latexed_mass += latexed_tri_mass
        return latexed_mass

    def commemoration2latex(self):
        com_list = '\n'
        if self.com_1 != False:
            com_list += '\n[\\textit{' + self.com_1.feast() + '}]\n'
        elif self.com_2 != False:
            com_list += '\n[\\textit{' + self.com_2.feast() + '}]\n'
        elif self.com_3 != False:
            com_list += '\n[\\textit{' + self.com_3.feast() + '}]\n'
        elif self.com_4 != False:
            com_list += '\n[\\textit{' + self.com_4.feast() + '}]\n'
        elif self.com_5 != False:
            com_list += '\n[\\textit{' + self.com_5.feast() + '}]\n'
        else:
            return com_list + '\n\\textit{No Commemoration}'
        return com_list

#===-===-=== FUNCTIONS ===-===-=== #


def easter(year: int):
    x = dateutil.easter.easter(year)
    return datetime(year=int(x.strftime('%Y')), month=int(x.strftime('%m')), day=int(x.strftime('%d')))


def day(year: int, month: int, day: int):
    x = datetime(year=year, month=month, day=day)
    return x


def week(i: int):
    return timedelta(weeks=i)


def indays(numdays: int):
    return timedelta(days=numdays)


def weekday(date: datetime):
    return date.strftime("%a")


def findsunday(date):
    # todo redefine findsunday() to use %w
    x = 0
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
    """ Escape LaTeX reserved characters.

    Args:
        string (str): String to be checked for reserved characters

    Returns:
        str: Same as entered string, but with escaped characters
    """
    clean_string = re.sub('&', '\&', re.sub('_', '\_', string))
    return clean_string


def commemoration_ordering(direct: str, dictionary: int):
    """ Updates the keys in the feast dicionaries so that 
        commemorations are numerically correct.

    Args:
        direct (str): The directory of the dictionary.
        dictionary (int): The dictionary to be corrected.

    Returns:
        None: The dictionary is updated without any return.
    """
    mdl = importlib.import_module(direct + str(dictionary))
    try:
        dic = mdl.temporal
    except AttributeError:
        dic = mdl.calen
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


def dict_clean(direct: str, dictionary: int):
    """ Gets rid of all dates in calendar which are appended with . or _;
    overwrites the calendar file with the resulting dictionary.

    Args:
        direct (integer)   : the relative path to the dictionary, 
                             in format calendar/calendar_
        dict   (dictionary): year of the calendar to clean
    """
    mdl = importlib.import_module(direct + str(dictionary))
    try:
        dic = mdl.temporal
    except AttributeError:
        dic = mdl.calen
    for x in sorted(dic):
        nobility_free = True
        if len(x) >= 6:
            continue
        else:
            second_ = Feast(x, dic[x])
            if not second_.feast_date+'.' in sorted(dic):
                continue
            else:
                second_ = Feast(x, dic[x])
                first_ = Feast(second_.feast_date+'.',
                               dic[second_.feast_date+'.'])
                if second_.rank(False) > first_.rank(False):
                    first, second = first_, second_
                elif second_.rank(False) == first_.rank(False):
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
                    rank = second_.rank(False)
                    if rank <= 10:  # ! refine this to exclude all but D1 and D2
                        dic.update(
                            {more_noble.feast_date.strip(
                                '.'): more_noble.properties}
                        )
                        dic.update(
                            {less_noble.feast_date.strip(
                                '.')+' tranlsated': less_noble.properties}
                        )
                    else:
                        more_noble.com_1.update(
                            {'com_1': less_noble.properties})
                        dic.update({more_noble.feast_date.strip(
                            '.'): more_noble.properties})
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
                    if first.rank(False) <= 4 and second.rank(False) <= 10:
                        dic.update(
                            {first.feast_date.strip('.'): first.properties})
                        dic.update(
                            {second.feast_date.strip('.')+'_': second.properties})
                    # no commemoration
                    elif first.rank(False) <= 4 and second.rank(False) > 10:
                        dic.update(
                            {first.feast_date.strip('.'): first.properties})
                    # commemoration
                    # todo refine these ranges:
                    elif 19 > first.rank(False) > 4 and 19 > second.rank(False) >= 6:
                        first.com_1 = second.feast
                        dic.update(
                            {first.feast_date.strip('.'): first.properties})
                    elif second.rank(False) == 22:
                        dic.update(
                            {first.feast_date.strip('.'): first.properties})
                    # no commemoration
                    else:
                        dic.update(
                            {first.feast_date.strip('.'): first.properties})
                    if len(first.feast_date) == 6:
                        dic.pop(first.feast_date)
                    if len(second.feast_date) == 6:
                        dic.pop(second.feast_date)
    commemoration_ordering(direct, dictionary)
    with open(re.sub(r"\.", r'/', direct) + str(dictionary) + ".py", "a") as f:
        f.truncate(0)
        for i, line in enumerate(sorted(dic)):
            if i == 0:
                f.write(re.sub(r"/(temporal|calendar)", '', re.sub(r"\.", r'/', direct)+str(dictionary))
                        + ' = {\n\''+line+'\': '+str(dic[line])+',\n')
            else:
                f.write('\''+line+'\' : '+str(dic[line])+',\n')
        f.write('}')
        return 0


def stitch(year: int, s: str):
    """ Combine two calendars into a single dictionary, appending all
        doubled keys with a period.

    Args:
        year (int): year of the calendar being built
        s (str):    the sanctoral calendar being combined

    Returns:
        NoneType: None
    """
    # todo make stitch() reuseable
    mdl_temporal = importlib.import_module(
        'temporal.temporal_' + str(year)
    ).temporal
    mdl_sanctoral = importlib.import_module(
        'sanctoral.' + s
    ).sanctoral
    mdlt, mdls = sorted(mdl_temporal), sorted(mdl_sanctoral)
    calen = {}
    if leap_year(year) == False:
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
            {feast.feast_date + '.' if x in mdlt else feast.feast_date: feast.properties}
        )
    for y in mdlt:
        feast = Feast(y, mdl_temporal[y])
        calen.update({feast.feast_date: feast.properties})
    with open("calen/calendar_" + str(year) + ".py", "w") as f:
        f.truncate(0)
        for i, line in enumerate(sorted(calen)):
            if i == 0:
                f.write('calen = {\n\''+line+'\': '+str(calen[line])+',\n')
            else:
                f.write('\''+line+'\':'+str(calen[line])+',\n')
        f.write('}')
    return 0
