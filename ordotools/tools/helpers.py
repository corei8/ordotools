from datetime import datetime
from datetime import timedelta

import dateutil.easter

import re

import functools


@functools.lru_cache()
class LiturgicalYearMarks:

    def __init__(self, year):
        self.year = year
        self.christmas = datetime.strptime(str(self.year) + "-12-25", "%Y-%m-%d")
        self.first_advent = self.christmas - findsunday(self.christmas) - timedelta(weeks=3)
        self.last_advent = self.christmas - timedelta(days=1)

        # FIX: there is somethig wrong here, right? Not used anywhere...
        self.easter_season_start = easter(self.year) - timedelta(weeks=6, days=4)

        # Ash Wednesday:
        self.lent_begins = easter(self.year) - timedelta(weeks=6, days=4)
        # Holy Saturday:
        self.lent_ends = easter(self.year) - timedelta(days=1)

        self.easter = easter(self.year)
        self.easter_season_end = easter(self.year) + timedelta(days=39)
        self.pentecost_season_start = easter(self.year) + timedelta(days=49)
        self.pentecost_season_end = self.first_advent - timedelta(days=1)


def findsunday(date: datetime) -> timedelta:
    """
    return the distance betweent the date and
    the previous Sunday, as timedelta.days
    """
    return timedelta(days=int(date.strftime('%w')))


@functools.lru_cache()
def easter(year: int) -> datetime:
    """ return the date of easter for this year """
    return datetime(
        year=int(dateutil.easter.easter(year).strftime('%Y')),
        month=int(dateutil.easter.easter(year).strftime('%m')),
        day=int(dateutil.easter.easter(year).strftime('%d'))
    )


ladys_office = {
    "code": "lady_saturday",
    "rank": [21, "s"],
    "color": "white",
    "mass": {
        "int": "Salve sancta parens",
        "glo": True,
        "cre": False,
        "pre": "de B Maria Virg (et te in Veneratione)"
    },
    "com_1": {"oration": "Deus qui corda"},
    "com_2": {"oration": "Ecclesiæ"},
    "com_3": {},
    "matins": {},
    "lauds": {},
    "prime": {"responsory": "Qui natus est", "preces": True},
    "little_hours": {},
    "vespers": {
        "proper": False,
        "admag": ("firstVespers", "secondVespers"),
        "propers": {},
        "oration": ""
    },
    "compline": {},
    "office_type": "ut in pr loco",
    "nobility": (8, 2, 6, 13, 3, 0,),
}


def day(year: int, month: int, day: int) -> datetime:
    return datetime(year=year, month=month, day=day)


def weeks(i: int) -> timedelta:
    """ return a timedelta week, with integers as the input """
    return timedelta(weeks=i)


def days(numdays: int) -> timedelta:
    """ return a timedelta day(s), with integers as the input """
    return timedelta(days=numdays)


def weekday(date: datetime) -> str:
    """ return the weekday, with datetime as the input """
    return date.strftime('%a')


# def advance_a_day(date: str) -> str:
#     """ return a date advanced a day, returns a string mm/dd """
#     return date + timedelta(days=1)


# def find_extra_epiphany(pents: int) -> int:
#     """ return the number of Sundays not celebrated after Epiphany """
#     if pents == 23:
#         pass
#     else:
#         return pents - 24


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
    return re.sub('&', r'\&', re.sub('_', r'\_', string))


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


def which_sunday(date: datetime) -> int:
    """
    Determine the numeric order of a Sunday within a month.
    """
    sevens = [s for s in range(0, 31, 7)]
    index = int(date.strftime("%d"))
    x = 0
    while index-x not in sevens:
        x += 1
    return sevens.index(index-x)+1


def last_sunday(date: datetime) -> bool:
    if which_sunday(date) < 4:
        return False
    elif which_sunday(date) == 4 and int(date.strftime("%d")) < 25:
        return False
    else:
        return True
