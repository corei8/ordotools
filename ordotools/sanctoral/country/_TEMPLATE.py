from ordotools.tools.helpers import day


class Country:

    def __init__(self, year):
        self.name = "<Country>"  # in latin, genitive
        self.year = year
        self.data = {
            day(year=self.year, month=0, day=0): {
                "code": 000,
                "rank": [0, ""],  # check the ranking
                "nobility": (False,),
                "com": [],
                "office_type": False,
                "color": "white",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": { "hymn": "", "verse": ""}, "oration": "Deus, qui ad praedicandam"},
                "compline": {},
            }
        }
