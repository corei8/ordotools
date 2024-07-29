from ordotools.tools.helpers import day


class Country:
    """
    Proper days of a country, which are called by the diocese.
    """

    def __init__(self, year):
        self.name = "Australiae"
        self.year = year
        self.data = {
            day(year=self.year, month=7, day=31): {
                "feast": "",
                "rank": [14, "dm"],
                "nobility": (False,),
                "com": [],
                "office_type": False,
                "color": "white",
                "mass": {"int": "", "glo": False, "cre": False, "pre": ""},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },
            day(year=self.year, month=7, day=31): {
                "feast": "",
                "rank": [14, "dm"],
                "nobility": (False,),
                "com": [],
                "office_type": False,
                "color": "white",
                "mass": {"int": "", "glo": False, "cre": False, "pre": ""},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            }
        }
