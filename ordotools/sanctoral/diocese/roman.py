from ordotools.tools.helpers import day


class Sanctoral:
    """
    The Roman Sanctoral Cycle, which is called at every compilation.
    | self.sanctoral is the only return, containing a dictionary of
    | the feasts.
    """

    def __init__(self, year):
        self.year = year
        self.data = {

            # what is the best way to determine if the third lessons are proper?

            # TODO: We need to have a method for events on any day. Greater Litanies, for example.

            # January
            day(year=self.year, month=1, day=5): {
                # S Telesphori PM
                "code": 100000,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                # TODO: get the correct antiphons
                "vespers": {"proper": False, "admag": ("O Doctor", "O Doctor"), "oration": "Deus, qui populo"},
                "compline": {},
            },

            day(year=self.year, month=1, day=14): {
                # S Hilarii Episcopi ECD
                "code": 100,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    "code": 27400,
                    "mass": {"int": "Lætabitur", "glo": True, "cre": False, "pre": "Communis"},
                    "matins": {
                        "lessons": 9,
                    },
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("O Doctor", "O Doctor"), "oration": "Deus, qui populo"},
                "compline": {},
            },

            day(year=self.year, month=1, day=15): {
                # S Pauli Primi Eremitæ C
                "code": 200,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus ut palma", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "code": 27500,
                    "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=1, day=16): {
                # S Marcelli PM
                "code": 300,
                "rank": [16, "sd"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis", "glo": True, "cre": False, "pre": "de Apostolis"},
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

            day(year=self.year, month=1, day=17): {
                # S Antonii Abb
                "code": 400,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=1, day=18): {
                # Cathedræ S Petri Ap Romæ
                "code": 500,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit ei", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {
                    "code": 27600,
                    "mass": False
                },
                "com_2": {
                    "code": 27700,
                    "mass": {"int": "Me expectaverunt", "glo": True, "cre": True, "pre": "Communis"}
                },
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

            day(year=self.year, month=1, day=19): {
                # Ss Marii, Marthæ, Audifacis et Abachum Mm
                "code": 600,
                "rank": [22, "s"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Justi epulentur", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "code": 27800,
                    "mass": {"int": "In virtute", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=1, day=20): {
                # Ss Fabiani P et Sebastiani Mm
                "code": 700,
                "rank": [15, "d"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Intret in conspectu", "glo": True, "cre": False, "pre": "de Apostolis"},
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

            day(year=self.year, month=1, day=21): {
                # S Agnetis VM
                "code": 800,
                "rank": [15, "d"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Me expectaverunt", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=1, day=22): {
                # Ss Vincentii & Anastasii Mm
                "code": 900,
                "rank": [16, "sd"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Intret", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=1, day=23): {
                # S Raymundi de Peñafort C
                "code": 1000,
                "rank": [16, "sd, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "code": 27900,
                    "mass": {"int": "Me expectaverunt", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=1, day=24): {
                # S Timothei EM
                "code": 1100,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=1, day=25): {
                # Conversio S Pauli Ap
                "code": 1200,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Scio, cui credidi", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {
                    "code": 28000,
                    "mass": False
                },
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

            day(year=self.year, month=1, day=26): {
                # S Polycarpi EM
                "code": 1300,
                "rank": [15, "d"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Sacerdotes Dei", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=1, day=27): {
                # S Joannis Chrysostomi ECD
                "code": 1400,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=1, day=28): {
                # S Petri Nolasci C
                "code": 1500,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "code": 28100,
                    "mass": {"int": "Vultum tuum", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=1, day=29): {
                # S Francisci Salesii ECD
                "code": 1600,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=1, day=30): {
                # S Martinæ VM
                "code": 1700,
                "rank": [16, "sd"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=1, day=31): {
                # S Joannis Bosco C
                "code": 1800,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dedit illi", "glo": True, "cre": False, "pre": "Communis"},
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

            # February
            day(year=self.year, month=2, day=1): {
                # S Ignatii EM
                "code": 1900,
                "rank": [15, "d"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=2, day=2): {
                # In Purificatione BMV
                "code": 2000,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Suscepisimus", "glo": True, "cre": True, "pre": "de Nativitate"},
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

            day(year=self.year, month=2, day=3): {
                # S Blasii EM
                "code": 2100,
                "rank": [22, "s"],
                "nobility": (8, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Sacerdotes Dei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=4): {
                # S Andreæ Corsini EC
                "code": 2200,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=2, day=5): {
                # S Agathæ VM
                "code": 2300,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Gaudeamus", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=2, day=6): {
                # S Titi EC
                "code": 2400,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit ei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "code": 28200,
                    "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=2, day=7): {
                # S Romualdi Abb
                "code": 2500,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=2, day=8): {
                # S Joannis de Matha C
                "code": 2600,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=2, day=9): {
                # S Cyrilli Alexandrini ECD
                "code": 2700,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    "code": 28300,
                    "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=2, day=10): {
                # S Scholasticæ V
                "code": 2800,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=2, day=11): {
                # In Apparitione BMV Immaculatæ
                "code": 2900,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Vidi civitatem", "glo": True, "cre": True, "pre": "de B Maria Virg"},
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

            day(year=self.year, month=2, day=12): {
                # Ss Septem Fundatores Ordinis Servorum BMV C
                "code": 3000,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justi decantaverunt", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=2, day=14): {
                # S Valentini PM
                "code": 3100,
                "rank": [22, "s"],
                "nobility": (8, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "In virtute", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=15): {
                # Ss Faustini & Jovitæ Mm
                "code": 3200,
                "rank": [22, "s"],
                "nobility": (8, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=18): {
                # S Simeonis EM
                "code": 3300,
                "rank": [22, "s"],
                "nobility": (8, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=2, day=22): {
                # In Cathedra S Petri Ap
                "code": 3400,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit ei Dominus", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=2, day=23): {
                # S Petri Damiani ECD
                "code": 3500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    "code": 27300,
                },
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

            day(year=self.year, month=2, day=24): {
                # S Matthiæ Ap
                "code": 3600,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostolis"},
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

            day(year=self.year, month=2, day=27): {
                # S Gabrielis a Virgine Perdolente C
                "code": 3700,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Oculus Dei", "glo": True, "cre": False, "pre": "Communis"},
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

            # March
            day(year=self.year, month=3, day=4): {
                # S Casimiri C
                "code": 3800,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os iusti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "code": 28400,
                    "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
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

            day(year=self.year, month=3, day=6): {
                # Ss Perpetuae et Felicitatiis Mm
                "code": 3900,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Me expectaverunt", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=3, day=7): {
                # S Thomæ de Aquino CD
                "code": 4000,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio ecclesiae", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=3, day=8): {
                # S Joannis a Deo C
                "code": 4100,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os iusti", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=3, day=9): {
                # S Franciscae Romanae V
                "code": 4200,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Cognovi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=3, day=10): {
                # Ss Quadragintarum Mm
                "code": 4300,
                "rank": [16, "sd"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Clamaverunt iusti", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=3, day=12): {
                # S Gregorii I PCD
                "code": 4400,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": True, "cre": True, "pre": "de Apostolis"},
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

            day(year=self.year, month=3, day=17): {
                # S Patricii EC
                "code": 4500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=3, day=18): {
                # S Cyrilli Hierosolymitani ECD
                "code": 4600,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio ecclesiae", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=3, day=19): {
                # S Josephi Sponsi BMV C
                "code": 4700,
                "rank": [2, "d I cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus ut palma", "glo": True, "cre": True, "pre": "De Sancto Ioseph"},
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

            day(year=self.year, month=3, day=21): {
                # S Benedicti Abb
                "code": 4800,
                "rank": [14, "dm"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os iusti", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=3, day=24): {
                # S Gabrielis Arch
                "code": 4900,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Benedicite Dominum", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=3, day=25): {
                # In Annuntiatione BMV
                "code": 5000,
                "rank": [2, "d I cl"],
                "nobility": (1, 2, 6, 2, 1, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Vultum tuum", "glo": True, "cre": True, "pre": "De B Maria Virg"},
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

            day(year=self.year, month=3, day=27): {
                # S Joannis Damasceni CD
                "code": 5100,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Tenuisti manum", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=3, day=28): {
                # S Joannis a Capistrano C
                "code": 5200,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Ego autem", "glo": True, "cre": False, "pre": "Communis"},
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

            # April
            day(year=self.year, month=4, day=2): {
                # S Francisci de Paula C
                "code": 5300,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus ut palma", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=4, day=4): {
                # S Isidori ECD
                "code": 5400,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio ecclesiae", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=4, day=5): {
                # S Vincentii Ferrerii C
                "code": 5500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os iusti", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=4, day=11): {
                # S Leonis PCD
                "code": 5600,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": True, "cre": True, "pre": "de Apostolis"},
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

            day(year=self.year, month=4, day=13): {
                # S Hermenegildi M
                "code": 5700,
                "rank": [16, "sd"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": ["In virtute", "Protexisti"], "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=4, day=14): {
                # S Justini M
                "code": 5800,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Narraverunt mihi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "code": 28500,
                    "mass": {"int": ["Sapientiam", "Sancti tui"], "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=4, day=17): {
                # S Aniceti PM
                "code": 5900,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=4, day=21): {
                # S Anselmi ECD
                "code": 6000,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio ecclesiae", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=4, day=22): {
                # Ss Soteris et Caii PpMm
                "code": 6100,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=4, day=23): {
                # S Georgii M
                "code": 6200,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Protexisti me", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=4, day=24): {
                # S Fidelis a Sigmaringa M
                "code": 6300,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Protexisti me", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=4, day=25): {
                # S Marci Ev
                "code": 6400,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Protexisti me", "glo": True, "cre": True, "pre": "de Apostolis"},
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

            day(year=self.year, month=4, day=26): {
                # Ss Cleti et Marcellini PpMm
                "code": 6500,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
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

            day(year=self.year, month=4, day=27): {
                # S Petri Canisii CD
                "code": 6600,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio ecclesiae", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=4, day=28): {
                # S Pauli a Cruce C
                "code": 6700,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Christo confixus sum", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "code": 28600,
                    "mass": {"int": ["Protexisti", "In virtute"], "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=4, day=29): {
                # S Petri M
                "code": 6800,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Protexisti", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=4, day=30): {
                # S Catharinae Senensis V
                "code": 6900,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
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

            # May
            day(year=self.year, month=5, day=1): {
                # Ss Philippi et Iacobi App
                "code": 7000,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Clamaverunt ad te", "glo": True, "cre": True, "pre": "De Apostolis"},
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

            day(year=self.year, month=5, day=2): {
                # S Athanasii ECD
                "code": 7100,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio ecclesiae", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=5, day=3): {
                # In Inventione S Crucis
                "code": 7200,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Nos autem gloriari", "glo": True, "cre": True, "pre": "De Cruce"},
                "com_1": {
                    "code": 28700,
                    "mass": {"int": "Sancti tui", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
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

            day(year=self.year, month=5, day=4): {
                # S Monicae V
                "code": 7300,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Cognovi, Domine", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=5, day=5): {
                # S Pii V PC
                "code": 7400,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
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

            day(year=self.year, month=5, day=6): {
                # S Joannis ApEv ante Portam Latinam
                "code": 7500,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Protexisti me", "glo": True, "cre": True, "pre": "De Apostolis"},
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

            day(year=self.year, month=5, day=7): {
                # S Stanislai EM
                "code": 7600,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Protexisti me", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=5, day=8): {
                # In Apparitione S Michaelis Arch
                "code": 7700,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Benedicite Dominum", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=5, day=9): {
                # S Gregorii Nanzanzeni ECD
                "code": 7800,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In media", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=5, day=10): {
                # S Antonini EC
                "code": 7900,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit ei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "code": 28800,
                    "mass": {"int": "Sancti tui", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=5, day=12): {
                # Ss Nerei, Achillei at Domitillae V atq Pancratii Mm
                "code": 8000,
                "rank": [16, "sd"],
                "nobility": (5, 2, 6, 7, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Ecce, oculi Domini", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=5, day=13): {
                # S Roberti Bellarmino ECD
                "code": 8100,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=5, day=14): {
                # S Bonifatii M
                "code": 8200,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Protexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=15): {
                # S Joannis Baptistae de la Salle C
                "code": 8300,
                "rank": [15, "d, mtv"],  # TODO: check this mtv
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os iusti", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=5, day=16): {
                # S Ubaldi EC
                "code": 8400,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=5, day=17): {
                # S Paschalis Baylon C
                "code": 8500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=5, day=18): {
                # S Venantii M
                "code": 8600,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": ["Protexisti", "In virtute"], "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=5, day=19): {
                # S Petri Caelestini PC
                "code": 8700,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {
                    "code": 28900,
                    "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=5, day=20): {
                # S Bernardini Senensis C
                "code": 8800,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=5, day=25): {
                # S Gregorii VII PC
                "code": 8900,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {
                    "code": 29000,
                    "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
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

            day(year=self.year, month=5, day=26): {
                # S Philippi Nerii C
                "code": 9000,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Caritas Dei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    "code": 29100,
                    "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
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

            day(year=self.year, month=5, day=27): {
                # S Bedæ Venerabilis CD
                "code": 9100,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    "code": 29200,
                    "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
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

            day(year=self.year, month=5, day=28): {
                # S Augustini EC
                "code": 9200,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Sacerdotes", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=5, day=29): {
                # S Mariæ Magdalenæ de Pazzis V
                "code": 9300,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=5, day=30): {
                # S Felix I PM
                "code": 9400,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=5, day=31): {
                # B Mariae Virginis Reginae
                "code": 9500,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Gaudeamus", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {
                    # S Petronillae V
                    "code": 29300,
                    "mass": {"int": "Vultum tuum", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            # June
            day(year=self.year, month=6, day=1): {
                # S Angelæ Mericiæ V
                "code": 9600,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=6, day=2): {
                # Ss Marcellini, Petri atq Erasmi E Mm
                "code": 9700,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Clamaverunt", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=6, day=4): {
                # S Francisci Caracciolo C
                "code": 9800,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Factum est", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=6, day=5): {
                # S Bonifatii EM
                "code": 9900,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Exsultabo", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=6, day=6): {
                # S Norberti EC
                "code": 10000,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=6, day=9): {
                # Ss Primi et Feliciani Mm
                "code": 10100,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": ["Sapientiam", "Sancti tui"], "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=10): {
                # S Margaritæ R V
                "code": 10200,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Cognovi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=6, day=11): {
                # S Barnabæ Ap
                "code": 10300,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostlis"},
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

            day(year=self.year, month=6, day=12): {
                # S Joannis a S Facundo C
                "code": 10400,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Basilidi, Cyrini, Nabori atq Nazarii Mm
                    "code": 29400,
                    "mass": {"int": ["Intret in conspectu", "Sancti tui"], "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=6, day=13): {
                # S Antonii de Padua CD
                "code": 10500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=6, day=14): {
                # S Basilii Magni ECD
                "code": 10600,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=6, day=15): {
                # Ss Viti, Modesti atq Crescentiæ Mm
                "code": 10700,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Multæ tribulationes", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 0,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=18): {
                # S Ephræm Syri Diaconi CD
                "code": 10800,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    # Ss Marci et Marcelliani Mm
                    "code": 29500,
                    "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 0,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=19): {
                # S Julianæ de Falconeriis V
                "code": 10900,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Gervasii et Protasii Mm", "mass": {"int": "Loquetur Dominus "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 0,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=20): {
                # S Silverii PM
                "code": 11000,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=6, day=21): {
                # S Aloisii Gonzagæ C
                "code": 11100,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Minuisti", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=6, day=22): {
                # S Paulini EC
                "code": 11200,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Sacerdotes tui", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=6, day=23): {
                # In Vigilia Nativitatis S Joannis Baptistæ
                "code": 11300,
                "rank": [19, "v"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Ne timeas", "glo": False, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=6, day=24): {
                # In Nativitate S Joannis Baptistæ
                "code": 11400,
                "rank": [2, "d I cl cum Oct communi"],
                "nobility": (1, 0, 4, 4, 1, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "De ventre", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=6, day=25): {
                # S Gulielmi Abb
                "code": 11500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=6, day=26): {
                # S Joannis et Pauli Mm
                "code": 11600,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Multæ tribulationes", "glo": True, "cre": False, "pre": "Communis"},
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

            # todo Add "123/27 De IV die infra OCtava Nativitatis S Joannis Baptistae feria
            day(year=self.year, month=6, day=28): {
                # S Irinæi EM
                "code": 11800,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Lex veritatis", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # In Vigilia Ss Petri et Pauli App
                    "code": 29600,
                    "mass": {"int": "Dicit Dominus", "glo": False, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=6, day=29): {
                # Ss Petri et Pauli App
                "code": 11900,
                "rank": [2, "d I cl cum Oct communi"],
                "nobility": (1, 2, 4, 5, 1, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Nunc scio", "glo": True, "cre": True, "pre": "de Apostolis"},
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

            day(year=self.year, month=6, day=30): {
                # In Commemoratione S Pauli Apostoli
                "code": 12000,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Scio, cui credidi", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {
                    # S Petri Ap
                    "code": 29700,
                    "mass": {"int": "", "glo": True, "cre": True, "pre": "de Apostolis"}
                },
                "com_2": {
                    # "feast": "In Octava S Joannis Baptistae"
                },
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

            # July
            day(year=self.year, month=7, day=1): {
                # In Festo Pretiosissimi Sanguinis DNJC
                "code": 12100,
                "rank": [2, "d I cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Redemisti nos", "glo": True, "cre": True, "pre": "de Cruce"},
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

            day(year=self.year, month=7, day=2): {
                # In Visitatione BMV
                "code": 12200,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Salve, sancta Parens", "glo": True, "cre": True, "pre": "de BMV"},
                "com_1": {
                    # Ss Processi et Martiniani Mm
                    "code": 29800,
                    "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=7, day=3): {
                # S Leonis II PC
                "code": 12300,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": True, "cre": True, "pre": "de Apostolis"},
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
            # todo add "131/4 De VI die infra Octava Ss Petri et Pauli App feria
            day(year=self.year, month=7, day=5): {
                # S Antonii Mariæ Zaccaria C
                "code": 12500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Sermo meus", "glo": True, "cre": True, "pre": "de Apostolis"},
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
            # todo add "133/6 Octava Ss Petri et Pauli App dm
            day(year=self.year, month=7, day=7): {
                # Ss Cyrilli et Methodii EeCc
                "code": 12700,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Sacerdotes tui", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=7, day=8): {
                # S Elisabeth R Vid
                "code": 12800,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Cognovi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=7, day=10): {
                # Ss Septem Fratrum Mm ac Rufinæ et Secundæ VvMm
                "code": 12900,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Laudate, pueri", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=7, day=11): {
                # S Pii I PM
                "code": 13000,
                "rank": [22, "s"],
                "nobility": (8, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=12): {
                # S Joannis Gualberti Abb
                "code": 13100,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Naboris et Felicis Mm
                    "code": 29900,
                    "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=7, day=13): {
                # S Anacleti PM
                "code": 13200,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
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

            day(year=self.year, month=7, day=14): {
                # S Bonaventuræ ECD
                "code": 13300,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=7, day=15): {
                # S Henrici Imp C
                "code": 13400,
                "rank": [16, "sd, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=7, day=16): {
                # In Commemoratione BMV de Monte Carmelo
                "code": 13500,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Gaudeamus", "glo": True, "cre": True, "pre": " de B Maria Virg"},
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

            day(year=self.year, month=7, day=17): {
                # S Alexii C
                "code": 13600,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=7, day=18): {
                # S Camilli de Lellis C
                "code": 13700,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Majorem hac", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Symphorosae et Septem Filiis ejus Mm
                    "code": 30000,
                    "mass": {"int": "Clamaverunt", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=7, day=19): {
                # S Vincentii a Paulo C
                "code": 13800,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus ut palma", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=7, day=20): {
                # S Hieronymi Æmiliani C
                "code": 13900,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Effusum est", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Margaritae VM
                    "code": 30100,
                    "mass": {"int": "Me expectaverunt", "glo": True, "cre": False, "pre": "Communis"},
                },
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

            day(year=self.year, month=7, day=21): {
                # S Praxedis V
                "code": 14000,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=22): {
                # S Mariæ Magdalenæ Pænitentis
                "code": 14100,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Me expectaverunt", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=7, day=23): {
                # S Apollinaris EM
                "code": 14200,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Sacerdotes Dei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Liborii EC
                    "code": 30200,
                    "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=7, day=24): {
                # In Vigilia S Jacobi Ap
                "code": 14300,
                "rank": [19, "v"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "purple",
                "mass": {"int": "Ego autem", "glo": False, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Christinae VM
                    "code": 30300,
                    "mass": {"int": "Me expectaverunt", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=7, day=25): {
                # S Jacobi Ap
                "code": 14400,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {
                    # S Christophori M
                    "code": 30400,
                    "mass": {"int": "In virtute", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=7, day=26): {
                # S Annæ Matris BMV
                "code": 14500,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Gaudeamus", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=7, day=27): {
                # S Pantaleonis M
                "code": 14600,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Lætabitur", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=28): {
                # Ss Nazarii et Celsi Mm, Victoris I PM, ac Innocentii I PC
                "code": 14700,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Intret in conspectu", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=7, day=29): {
                # S Marthæ V
                "code": 14800,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Felicis II P, Simplicis, Faustinis atq Beatricae Mm
                    "code": 30500,
                    "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=7, day=30): {
                # Ss Abdon et Sennen Mm
                "code": 14900,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Intret in conspectu", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=7, day=31): {
                # S Ignatii C
                "code": 15000,
                "rank": [14, "dm"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In nomine Jesu", "glo": True, "cre": False, "pre": "Communis"},
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

            # August
            day(year=self.year, month=8, day=1): {
                # S Petri Ap ad Vincula
                "code": 15100,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Nunc scio vere", "glo": True, "cre": True, "pre": "de Apostolis"},
                "com_1": {
                    # S Pauli Ap
                    "code": 30600,
                    "mass": {"int": "", "glo": True, "cre": True, "pre": "de Apostolis"}
                },
                "com_2": {
                    # Ss Machabæis Mm
                    "code": 34700,
                    "mass": {"int": "Clamaverunt", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=8, day=2): {
                # S Alphonsi Mariæ de Ligorio ECD
                "code": 15200,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Spiritus Domini", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    # S Stephani PM
                    "code": 30700,
                    "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
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

            day(year=self.year, month=8, day=3): {
                # In Inventione S Stephani Protomartyris
                "code": 15300,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Sederunt", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=8, day=4): {
                # S Dominici C
                "code": 15400,
                "rank": [14, "dm, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=8, day=5): {
                # In Dedicatione S Mariæ ad Nives
                "code": 15500,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Salve, sancta parens", "glo": True, "cre": True, "pre": "De B Mariae Virginis"},
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

            day(year=self.year, month=8, day=6): {
                # In Transfiguratione DNJC
                "code": 15600,
                "rank": [11, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Illuxerunt", "glo": True, "cre": True, "pre": "de Nativitate"},
                "com_1": {
                    # Ss Xysti P, Felicissimi atq Agapiti Mm
                    "code": 30800,
                    "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
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

            day(year=self.year, month=8, day=7): {
                # S Cajetani C
                "code": 15700,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Donati EM
                    "code": 30900,
                    "mass": {"int": "Sacerdotes Dei", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=8, day=8): {
                # Ss Cyriaci, Largi atq Smaragdi Mm
                "code": 15800,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Timete Dominum", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=8, day=9): {
                # S Joannis Mariæ Vianney C
                "code": 15900,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Vigilia S Laurentii M
                    "code": 31000,
                    "mass": {"int": "Dispersit", "glo": False, "cre": False, "pre": "Communis"}
                },
                "com_2": {
                    # S Romani M
                    "code": 34800,
                    "mass": {"int": "Lætabitur", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=8, day=10): {
                # S Laurentii M
                "code": 16000,
                "rank": [10, "d II cl"],
                "office_type": False,
                "color": "red",
                "mass": {"int": "Confessio", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=8, day=11): {
                # Ss Tiburtii et Susannæ V, Mm
                "code": 16100,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=12): {
                # S Claræ V
                "code": 16200,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=8, day=13): {
                # Ss Hippolyti et Cassiani Mm
                "code": 16300,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=8, day=14): {
                # In Vigilia Assumptionis BMV
                "code": 16400,
                "rank": [19, "v"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "purple",
                "mass": {"int": "Vultum tuum", "glo": False, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Eusebii C
                    "code": 31100,
                    "mass": {"int": "Justus", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {
                    "oration": "Spiritus Sancti",
                },
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

            day(year=self.year, month=8, day=15): {
                # In Assumptione BMV
                "code": 16500,
                "rank": [2, "d I cl cum Oct communi"],
                "nobility": (1, 1, 4, 2, 1, 0),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Signum magnum", "glo": True, "cre": True, "pre": "de B Maria Virg"},
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

            day(year=self.year, month=8, day=16): {
                # S Joachim C, Patris BMV,
                "code": 16600,
                "rank": [10, "d II cl, mtv"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dispersit", "glo": True, "cre": True, "pre": "de B Maria Virg"},
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

            day(year=self.year, month=8, day=17): {
                # S Hyacinthi C
                "code": 16700,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {
                    # Octava S Laurentii M
                    "code": 31200,
                    "mass": {"int": "Probasti", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=8, day=18): {
                # S Agapiti M
                "code": 16800,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Lætabitur", "glo": True, "cre": True, "pre": "de B Maria Virg"},
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

            day(year=self.year, month=8, day=19): {
                # S Joannis Eudes C
                "code": 16900,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": True, "pre": "de B Maria Virg"},
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

            day(year=self.year, month=8, day=20): {
                # S Bernardi AbbD
                "code": 17000,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "de B Maria Virg"},
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

            day(year=self.year, month=8, day=21): {
                # S Joannæ Franciscæ Fremiot de Chantal V
                "code": 17100,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Cognovi", "glo": True, "cre": True, "pre": "de B Maria Virg"},
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

            day(year=self.year, month=8, day=22): {
                # In Festo Immaculati Cordis BMV
                "code": 17200,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Adeamus", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {
                    # Ss Timothei, Hippolyti atq Symphoriani Mm
                    "code": 31300,
                    "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=8, day=23): {
                # S Philippi Benitii C
                "code": 17300,
                "rank": [19, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # In Vigilia S Bartholomæi Ap
                    "code": 31400,
                    "mass": {"int": "Ego autem", "glo": False, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=8, day=24): {
                # S Bartholomæi Ap
                "code": 17400,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostolis"},
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

            day(year=self.year, month=8, day=25): {
                # S Ludovici RC
                "code": 17500,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=8, day=26): {
                # S Zephrini PM
                "code": 17600,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
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

            day(year=self.year, month=8, day=27): {
                # S Josephi Calasanctii C
                "code": 17700,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Venite, filii", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=8, day=28): {
                # S Augustini ECD
                "code": 17800,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    # S Hermetis M
                    "code": 31500,
                    "mass": {"int": "Lætabitur", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=8, day=29): {
                # In Decollatione S Joannis Baptistæ
                "code": 17900,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Sabinae M
                    "code": 31600,
                    "mass": {"int": "Me expectaverunt", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=8, day=30): {
                # S Rosæ a S Maria Limanae V
                "code": 18000,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Felicis et Adaucti Mm
                    "code": 31700,
                    "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=8, day=31): {
                # S Raymundi Nonnati C
                "code": 18100,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
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

            # September
            day(year=self.year, month=9, day=1): {
                # S Ægidii Abb
                "code": 18200,
                "rank": [22, "s"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Duodecim Fratribus
                    "code": 31800,
                    "mass": {"int": "Clamaverunt", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=2): {
                # S Stephani R C
                "code": 18300,
                "rank": [16, "sd, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=9, day=3): {
                # S Pii X PC
                "code": 18400,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Extuli", "glo": True, "cre": False, "pre": "de Apostolis"},
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

            day(year=self.year, month=9, day=5): {
                # S Laurentii Justiniani EC
                "code": 18500,
                "rank": [16, "sd, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit ei", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=9, day=8): {
                # In Nativitate BMV
                "code": 18600,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Salve, sancta Parens", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {
                    # S Hadriani M
                    "code": 31900,
                    "mass": {"int": "In virtute", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=9, day=9): {
                # S Gorgonii M
                "code": 18700,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Lætabitur", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=10): {
                # S Nicolai de Tolentino C
                "code": 18800,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=9, day=11): {
                # Ss Proti et Hycinthi Mm
                "code": 18900,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=12): {
                # Ssmi Nominis BMV
                "code": 19000,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Vultum tuum", "glo": True, "cre": True, "pre": "de B Maria Virg"},
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

            day(year=self.year, month=9, day=14): {
                # In Exaltatione S Crucis
                "code": 19100,
                "rank": [14, "dm"],
                "office_type": False,
                "color": "red",
                "mass": {"int": "Nos autem", "glo": True, "cre": True, "pre": "de Cruce"},
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

            day(year=self.year, month=9, day=15): {
                # Septem Dolorum BMV
                "code": 19200,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Stabant", "glo": True, "seq": "Stabat Mater", "cre": True, "pre": "de B Maria Virg"},
                "com_1": {
                    # S Nicomedis M
                    "code": 32000,
                    "mass": {"int": "In virtute", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=9, day=16): {
                # Ss Cornelii P et Cypriani E Mm
                "code": 19300,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Intret", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {
                    # Ss Euphemiae V, Luciae atq Geminiani Mm
                    "code": 32100,
                    "mass": {"int": "Intret", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=9, day=17): {
                # In Impressione Ss Stigmatum S Francisci C
                "code": 19400,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Mihi autem", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=9, day=18): {
                # S Josephi a Cupertino C
                "code": 19500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilectio", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=9, day=19): {
                # Ss Januarii E et Sociorum Mm
                "code": 19600,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=9, day=20): {
                # Ss Eustachii et Sociorum Mm
                "code": 19700,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # In Vigilia S Matthæi ApEv
                    "code": 32200,
                    "mass": {"int": "Ego autem", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=9, day=21): {
                # S Matthæi ApEv
                "code": 19800,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Os justi", "glo": True, "cre": True, "pre": "de Apostolis"},
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

            day(year=self.year, month=9, day=22): {
                # S Thomæ de Villanova EC
                "code": 19900,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Mauritii et Sociorum Mm
                    "code": 32300,
                    "mass": {"int": "Intret", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=9, day=23): {
                # S Lini PM
                "code": 20000,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Theclae VM
                    "code": 32400,
                    "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=9, day=24): {
                # BMV de Merdece
                "code": 20100,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Salve", "glo": True, "cre": True, "pre": "de B Maria Virg"},
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

            day(year=self.year, month=9, day=26): {
                # Ss Cypriani et Justinæ Mm
                "code": 20200,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=9, day=27): {
                # Ss Cosmæ et Damiani Mm
                "code": 20300,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=9, day=28): {
                # S Wenceslai Ducis M
                "code": 20400,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "In virtute", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=9, day=29): {
                # In Dedicatione S Michaelis Arch
                "code": 20500,
                "rank": [2, "d I cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Benedicite", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=9, day=30): {
                # S Hieronymi SCD
                "code": 20600,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
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

            # October
            day(year=self.year, month=10, day=1): {
                # S Remigii EC
                "code": 20700,
                "rank": [22, "s"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=2): {
                # Ss Angelorum Custodum
                "code": 20800,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Benedicite", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=10, day=3): {
                # S Teresiæ a Jesu Infante V
                "code": 20900,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Veni de Libano", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=10, day=4): {
                # S Francisci C
                "code": 21000,
                "rank": [14, "dm"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Mihi autem", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=10, day=5): {
                # Ss Placidi et Sociorum Mm
                "code": 21100,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Salus autem", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=6): {
                # S Brunonis C
                "code": 21200,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=10, day=7): {
                # Sacratissimi Rosarii BMV
                "code": 21300,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Gaudeamus", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {
                    # S Marci PC
                    "code": 32500,
                    "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
                "com_2": {
                    # Ss Sergii, Bacchi, Marcelli atq Apuleji MM
                    "code": 34900,
                    "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=10, day=8): {
                # S Birgittæ V
                "code": 21400,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Cognovi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=10, day=9): {
                # S Joannis Leonardi C
                "code": 21500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In sermonibus", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Dionysii E, Rustici atq Eleutherii Mm
                    "code": 32600,
                    "mass": {"int": "Sapientiam", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=10, day=10): {
                # S Francisci Borgiæ C
                "code": 21600,
                "rank": [16, "sd, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=10, day=11): {
                # In Maternitate BMV
                "code": 21700,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Ecce Virgo", "glo": True, "cre": True, "pre": "de B Maria Virg"},
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

            day(year=self.year, month=10, day=13): {
                # S Eduardi R C
                "code": 21800,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=10, day=14): {
                # S Callisti I PM
                "code": 21900,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=10, day=15): {
                # S Teresiæ V
                "code": 22000,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=10, day=16): {
                # S Hedwigis V
                "code": 22100,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Cognovi", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=10, day=17): {
                # S Margaritæ Mariæ Alacoque V
                "code": 22200,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Sub umbra", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=10, day=18): {
                # S Lucæ Ev
                "code": 22300,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostolis"},
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

            day(year=self.year, month=10, day=19): {
                # S Petri de Alcantara C
                "code": 22400,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus ut palma", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=10, day=20): {
                # S Joannis Cantii C
                "code": 22500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Miseratio hominis", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=10, day=21): {
                # S Hilarionis Abb
                "code": 22600,
                "rank": [22, "s"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Ursulae et Sociarum VM
                    "code": 32700,
                    "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"}
                },
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=24): {
                # S Raphaelis Arch
                "code": 22700,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Benedicite", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=10, day=25): {
                # Ss Chrysanthi et Dariæ Mm
                "code": 22800,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Intret", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=26): {
                # S Evaristi PM
                "code": 22900,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=10, day=27): {
                # In Vigilia Ss Simonis et Judæ App
                "code": 23000,
                "rank": [19, "v"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "purple",
                "mass": {"int": "Intret", "glo": False, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=10, day=28): {
                # Ss Simonis et Judæ App
                "code": 23100,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostolis"},
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

            day(year=self.year, month=10, day=31): {
                # In Vigilia Omnium Sanctorum
                "code": 23200,
                "rank": [19, "v"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "purple",
                "mass": {"int": "Judicant", "glo": False, "cre": False, "pre": "Communis"},
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

            # November
            day(year=self.year, month=11, day=1): {
                # In Festo Omnium Sanctorum
                "code": 23300,
                "rank": [2, "d I cl cum Oct communi"],
                "nobility": (1, 1, 4, 3, 1, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Gaudeamus", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=11, day=2): {
                # In Commemoratione Omnium Fidelium Defunctorum
                "code": 23400,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "color": "black",
                "mass": {
                    "Ad Primam Missam": {"int": "Requiem", "glo": False, "seq": "Dies Iræ", "cre": False, "pre": "Defunctorum"},
                    "Ad Secundam Missam": {"int": "Requiem", "glo": False, "seq": "Dies Iræ", "cre": False, "pre": "Defunctorum"},
                    "Ad Tertiam Missam": {"int": "Requiem", "glo": False, "seq": "Dies Iræ", "cre": False, "pre": "Defunctorum"},
                },
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "office_type": False,
                "matins": {
                    "lessons": 9,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=11, day=4): {
                # S Caroli EC
                "code": 23500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit ei", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    # Octavae Omnium Sanctorum
                    "code": 32800,
                    "mass": {"int": "", "glo": True, "cre": True, "pre": "Communis"}
                },
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
            # todo add "2371/5-7 Infra Octava Omnium Sanctorum feria
            # day(year=self.year, month=11, day=8): {
            #     # In Octava Omnium Sanctorum
            #     "rank": [16, "sd"],
            #     "nobility": (0, 0, 0, 0, 0, 0,),
            #     "office_type": False,
            #     "com": [{# Ss Quatuor Coronatis Mm", "mass": {"int": "Intret "glo": True, "cre": False, "pre": "Communis"}},],
            #     "color": "white",
            #     "mass": {"int": "Gaudeamus", "glo": True, "cre": True, "pre": "Communis"},
            #     "matins": {
            #     "lessons": 9,
            # },
            #     "lauds": {},
            #     "prime": {},
            #     "little_hours": {},
            #     "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
            #     "compline": {},
            # },

            day(year=self.year, month=11, day=9): {
                # In Dedicatione Archibasilicæ Ssmi Salvatoris
                "code": 23700,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Terribilis", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    # S Theodori M
                    "code": 32900,
                    "mass": {"int": "Laetabitur", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=11, day=10): {
                # S Andreæ Avellini C
                "code": 23800,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # Ss Tryphonis, Respicii atq Nymphae V Mm
                    "code": 33000,
                    "mass": {"int": "Clamaverunt", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=11, day=11): {
                # S Martini EC
                "code": 23900,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit ei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Mennae M
                    "code": 33100,
                    "mass": {"int": "Laetabitur", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=11, day=12): {
                # S Martini I PM
                "code": 24000,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"},
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

            day(year=self.year, month=11, day=13): {
                # S Didaci C
                "code": 24100,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=11, day=14): {
                # S Josaphat EM
                "code": 24200,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Gaudeamus", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=11, day=15): {
                # S Alberti Magni ECD
                "code": 24300,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=11, day=16): {
                # S Gertrudis V
                "code": 24400,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Dilexisti", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=11, day=17): {
                # S Gregorii Thaumaturgi EC
                "code": 24500,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=11, day=18): {
                # In Dedicatione Basilicarum Ss Petri et Pauli App
                "code": 24600,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Terribilis", "glo": True, "cre": True, "pre": "de Apostolis"},
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

            day(year=self.year, month=11, day=19): {
                # S Elisabeth V
                "code": 24700,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Cognovi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Pontiani PM
                    "code": 33200,
                    "mass": {"int": "Si diligis me", "glo": True, "cre": False, "pre": "de Apostolis"}
                },
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

            day(year=self.year, month=11, day=20): {
                # S Felicis de Valois C
                "code": 24800,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Justus", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=11, day=21): {
                # In Præsentatione BMV
                "code": 24900,
                "rank": [14, "dm"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Salve", "glo": True, "cre": True, "pre": "de B Maria Virg"},
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

            day(year=self.year, month=11, day=22): {
                # S Cæciliæ VM
                "code": 25000,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=11, day=23): {
                # S Clementis I PM
                "code": 25100,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Dicit Dóminus", "glo": True, "cre": False, "pre": "de Apostolis"},
                "com_1": {
                    # S Felicitatis M
                    "code": 33300,
                    "mass": {"int": "Me exspectaverunt", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=11, day=24): {
                # S Joannis a Cruce CD
                "code": 25200,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    # S Chrysogoni M
                    "code": 33400,
                    "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=11, day=25): {
                # S Catharinæ VM
                "code": 25300,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=11, day=26): {
                # S Sylvestri Abb
                "code": 25400,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Petri Alexandrini EM
                    "code": 33500,
                    "mass": {"int": "", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=11, day=29): {
                # In Vigilia S Andreæ Ap
                "code": 25500,
                "rank": [22, "v"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "purple",
                "mass": {"int": "Dominus secus", "glo": False, "cre": False, "pre": "Communis"},
                "com_1": {
                    # S Saturnini M
                    "code": 33600,
                    "mass": {"int": "Laetabitur", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=11, day=30): {
                # S Andreæ Ap
                "code": 25600,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostolis"},
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
            # todo add 1259/1 feria

            # December
            day(year=self.year, month=12, day=2): {
                # S Bibianæ VM
                "code": 25800,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Me expectaverunt", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=12, day=3): {
                # S Francisci Xaverii C
                "code": 25900,
                "rank": [14, "dm, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=12, day=4): {
                # S Petri Chrysologi ECD
                "code": 26000,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
                "com_1": {
                    # S Barbarae VM
                    "code": 33700,
                    "mass": {"int": "Loquebar", "glo": True, "cre": False, "pre": "Communis"}
                },
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

            day(year=self.year, month=12, day=5): {
                # S Sabbae Abb
                "code": 26100,
                "rank": [22, "s"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Os justi", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=12, day=6): {
                # S Nicolai EC
                "code": 26200,
                "rank": [15, "d"],  # FIX: vigil of IC?
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit ei", "glo": True, "cre": False, "pre": "Communis"},
                "com_1": {
                    # In Vigilia Conceptionis Immaculatæ BMV
                    "code": 33800,
                    "rank": [19, "v"],
                    "nobility": (0, 0, 0, 0, 0, 0,),
                    "office_type": False,
                    "color": "purple",
                    "mass": {"int": "Venite, audite", "glo": False, "cre": False, "pre": "Communis"},
                    "matins": {
                        "lessons": 9,
                    },
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                    "compline": {}
                },
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

            day(year=self.year, month=12, day=7): {
                # S Ambrosii ECD
                "code": 26300,
                "rank": [15, "d, mtv"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=12, day=8): {
                # In Conceptione Immaculata BMV
                "code": 26400,
                "rank": [2, "d I cl cum Oct communi"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "octave": 4,
                "office_type": False,
                "color": "white",
                "mass": {"int": "Gaudens gaudebo", "glo": True, "cre": True, "pre": "de B Maria Virg"},
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
            # todo add "2662/9 De II die infra Octava Concept. Immac. BMV feria
            day(year=self.year, month=12, day=10): {
                # S Melchidi PM
                "code": 26600,
                "rank": [22, "s"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Si diligis me", "glo": True, "cre": True, "pre": "de B Maria Virg"},
                "com_1": {},
                "com_2": {},
                "com_3": {},
                "matins": {
                    "lessons": 3,
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("firstVespers", "secondVespers"), "propers": {}, "oration": ""},
                "compline": {},
            },

            day(year=self.year, month=12, day=11): {
                # S Damasi I PC
                "code": 26700,
                "rank": [16, "sd"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": True, "cre": True, "pre": "de B Maria Virg"},
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

            day(year=self.year, month=12, day=13): {
                # S Luciæ VM
                "code": 26900,
                "rank": [15, "d"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Dilexisti", "glo": True, "cre": True, "pre": "de B Maria Virg"},
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

            day(year=self.year, month=12, day=16): {
                # S Eusebii EM
                "code": 27000,
                "rank": [16, "sd"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Sacerdotes Dei", "glo": True, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=12, day=20): {
                # In Vigilia S Thomæ Ap
                "code": 27100,
                "rank": [22, "v"], # TODO: check the ranking of a vigil
                "nobility": (8, 2, 6, 5, 3, 0,),
                "office_type": False,
                "color": "purple",
                "mass": {"int": "Ego autem", "glo": False, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=12, day=21): {
                # S Thomæ Ap
                "code": 27200,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostolis"},
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

        self.data_leapyear = {
            day(year=self.year, month=2, day=23): {
                # S Petri Damiani ECD
                "code": 3500,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "In medio", "glo": True, "cre": True, "pre": "Communis"},
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

            day(year=self.year, month=2, day=24): {
                # In Vigilia S Matthiæ
                "code": 27300,
                "rank": [20, "v"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Ego autem", "glo": False, "cre": False, "pre": "Communis"},
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

            day(year=self.year, month=2, day=25): {
                # S Matthiæ Ap
                "code": 3600,
                "rank": [10, "d II cl"],
                "nobility": (0, 0, 0, 0, 0, 0,),
                "office_type": False,
                "color": "red",
                "mass": {"int": "Mihi autem", "glo": True, "cre": True, "pre": "de Apostolis"},
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

            day(year=self.year, month=2, day=27): {
                "code": False,
                # "code": 27600,
            },

            day(year=self.year, month=2, day=28): {
                # S Gabrielis a Virgine Perdolente C
                "code": 3700,
                "rank": [15, "d"],
                "nobility": (4, 2, 6, 8, 3, 0,),
                "office_type": False,
                "color": "white",
                "mass": {"int": "Oculus Dei", "glo": True, "cre": False, "pre": "Communis"},
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

    def leapyear(self) -> dict:
        for feast, data in self.data_leapyear.items():
            # del self.data[day(year=self.year, month=2, day=27)]
            if feast in self.data:
                if data["code"] is False:
                    del self.data[feast]
            else:
                self.data |= {feast: data}
        return self.data
