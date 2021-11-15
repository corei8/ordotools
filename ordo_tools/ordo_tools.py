from datetime import timedelta, datetime
import dateutil.easter
import importlib
import re


ROMANS = ["I", "II", "III", "IV", "V", "VI", "VII",
          "VIII", "IX", "X", "XI", "XII", "XIII",
          "XIV", "XV", "XVI", "XVII", "XVIII", "XIX",
          "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV",
          "XXVI", "XXVII", "XXVIII", ]


class Feast:
    def __init__(self, feast_date: str, properties: dict):
        self.date = feast_date
        self.properties = properties
        self.mass = properties['mass']
        self.vespers = properties['vespers'] if 'vespers' in properties.keys(
        ) else False
        self.nobility = properties['nobility'] if 'nobility' in properties.keys(
        ) else False
        # maximum of five commemorations per feast
        for x in ('com_1', 'com_2', 'com_3', 'com_4', 'com_5', ):
            if 'com_'+str(x) in properties.keys():
                self.comms = self.Commemoration(properties['com_'+str(x)])

    class Commemoration:
        def __init__(self, details: dict):
            self.details = details
            self.mass = details['mass']

        def feast(self):
            return self.details['feast']

        def mass(self):
            return self.mass

    def date(self):
        return datetime.strptime('%m%d', self.feast_date)

    def feast(self):
        return self.properties['feast']

    def rank(self, visual: bool):
        if visual == True:
            return self.properties['rank'][-1]
        else:
            return self.properties['rank'][0]

    def to_dictionary(self):
        return self.properties


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


def weekday(date: int):
    return date.strftime("%a")


def findsunday(date):
    # todo redefine findsunday() to use %w
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
            if not second_.date+'.' in sorted(dic):
                continue
            else:
                second_ = Feast(x, dic[x])
                first_ = Feast(second_.date+'.', dic[second_.date+'.'])
                if second_.rank(False) > first_.rank(False):
                    first, second = first_, second_
                elif second_.rank(False) == first_.rank(False):
                    # just to prevent errors for now...
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
                            {more_noble.date.strip('.'): more_noble.properties}
                        )
                        dic.update(
                            {less_noble.date.strip(
                                '.')+' tranlsated': less_noble.properties}
                        )
                    else:
                        more_noble.com_1.update(
                            {'com_1': less_noble.properties})
                        dic.update({more_noble.date.strip(
                            '.'): more_noble.properties})
                    if len(more_noble.date) == 6:
                        dic.pop(more_noble.date)
                    if len(less_noble.date) == 6:
                        dic.pop(less_noble.date)
                    nobility_free = False
                    pass
                else:
                    first, second = second_, first_
                if nobility_free == False:
                    pass
                else:
                    # * continue adding the objects here:
                    # translation
                    if first.rank(False) <= 4 and second.rank(False) <= 10:
                        dic.update({first.date.strip('.'): first.properties})
                        dic.update(
                            {second.date.strip('.')+'_': second.properties})
                    # no commemoration
                    elif first.rank(False) <= 4 and second.rank(False) > 10:
                        dic.update({first.date.strip('.'): first.properties})
                    # commemoration
                    # todo refine these ranges:
                    elif 19 > first.rank(False) > 4 and 19 > second.rank(False) >= 6:
                        first.com_1 = second.feast
                        dic.update({first.date.strip('.'): first.properties})
                    elif second.rank(False) == 22:
                        dic.update({first.date.strip('.'): first.properties})
                    # no commemoration
                    else:
                        dic.update({first.date.strip('.'): first.properties})
                    if len(first.date) == 6:
                        dic.pop(first.date)
                    if len(second.date) == 6:
                        dic.pop(second.date)
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
        'temporal.temporal_' + str(year)).temporal
    mdl_sanctoral = importlib.import_module('sanctoral.' + s).sanctoral
    mdlt, mdls = sorted(mdl_temporal), sorted(mdl_sanctoral)
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
    calen = {}
    for x in mdls:
        feast = Feast(x, mdl_sanctoral[x])
        calen.update(
            {feast.date + '.' if x in mdlt else feast.date: feast.properties}
        )
    for y in mdlt:
        feast = Feast(y, mdl_temporal[y])
        calen.update({feast.date: feast.properties})
    with open("calen/calendar_" + str(year) + ".py", "w") as f:
        f.truncate(0)
        for i, line in enumerate(sorted(calen)):
            if i == 0:
                f.write('calen = {\n\''+line+'\': '+str(calen[line])+',\n')
            else:
                f.write('\''+line+'\':'+str(calen[line])+',\n')
        f.write('}')
    return 0
