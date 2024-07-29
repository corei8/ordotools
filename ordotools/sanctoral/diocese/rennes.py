from ordotools.tools.helpers import day
from importlib import import_module


class Diocese:

    def __init__(self, year):
        self.year = year

        self.name = "D. Rennes"
        self.country = "france"

        self.sanctoral = import_module(f".country.{self.country}", "sanctoral")
        self.country_data = self.sanctoral.Country(self.year).data
        self.roman = import_module(".diocese.roman", "sanctoral")
        self.roman_data = self.roman.Sanctoral(self.year).data

        self.data = {

            day(year=self.year, month=1, day=3): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=0, day=00): {
                "code": 900,
                "rank": [00, ""],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

































        }

    def calendar(self) -> dict:
        y = {}
        for local in self.data:
            # HACK: just to get things started
            if local in self.country_data:
                y |= {local: self.data[local]}
            else:
                y |= {local: self.data[local]}
        for date in self.roman_data:
            if date in y:
                # HACK: just to get things started
                pass
            else:
                y |= {date: self.roman_data[date]}
        return y
