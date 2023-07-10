from ordotools.tools.liturgical_dates import integer_to_roman
from ordotools.tools.parts import PENTECOST_MASSES


class TemporalData:

    def __init__(self):
        self.easy_data = {
            "Circumcision": {
                "feast": "Circumcisio DNJC et Oct. Nativitatis" ,
                "rank": [3, "d II cl"],
                "color": "white",
                "mass": {"int": "Puer natus", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },
            "8_Stephen": {
                "feast": "Octava S Stephani Protomartyris",
                "rank": [20, "s"],
                "color": "white",
                "mass": {"int": "Sederunt", "glo": True, "cre": False, "pre": "de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },
            "8_John": {
                "feast": "Octava S Joannis Ap Ev",
                "rank": [20, "s"],
                "color": "red",
                "mass": {"int": "Introit", "glo": True, "cre": True, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },
            "8_Innocents": {
                "feast": "Octava Ss Innocentium Mm.",
                "rank": [20, "s"],
                "color": "red",
                "mass": {"int": "Ex ore infantium", "glo": True, "cre": True, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },
            "SNameJesus": {
                "feast": "Ssmi Nominis Jesu",
                "rank": [10, "d II cl"],
                "color": "white",
                "mass": {"int": "In nomine Jesu", "glo": True, "cre": True, "pre": "de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },
            # FIX: test this
            "SNameJesu_8_Ste": {
                "feast": "Ssmi Nominis Jesu",
                "rank": [10, "d II cl"],
                "color": "white",
                "mass": {"int": "In nomine Jesu", "glo": True, "cre": True, "pre": "de Nativitate"},
                "com": [],
                "com": [{"feast": "S Stephani",}],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },

            # Epiphany Season
            "V_Epiphany": {
                "feast": "Vigilia Epiphaniæ",
                "rank": [12, "sd Vig privil 2 cl"],
                "color": "purple",
                "mass": {"int": "Dum medium silentium", "glo": True, "cre": True, "pre": "de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (False,),
                "fasting": False,
            },
            "Epiphany": {
                "feast": "Epiphania DNJC",
                "rank": [2, "d I cl cum Oct privil 2 ord"],
                "color": "white",
                "mass": {"int": "Ecce advenit", "glo": True, "cre": True, "pre": "de Epiphania"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },
            "8_Epiphany": {
                "feast": "Octava Epiphaniæ",
                "rank": [13, "dm"],
                "color": "white",
                "mass": {"int": "Ecce advenit", "glo": True, "cre": True, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },
            "D_Epiphany": {
                "feast": "In Octava Epiphaniæ",
                "rank": [13, "dm"],
                "color": "white",
                "mass": {"int": "Ecce advenit", "glo": True, "cre": True, "pre": "et Comm de Epiphania"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },

            # Holy Family
            "HolyFamily": {
                "feast": "S Familiæ Jesu, Mariæ, Joseph",
                "rank": [11, "dm"],
                "color": "white",
                "mass": {"int": "Exultat", "glo": True, "cre": True, "pre": "et communcantes de Epiphania"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },
            "D_HolyFamily": {
                "feast": "S Familiæ Jesu, Mariæ, Joseph; Dominica I infra Oct. Epiphaniæ",
                "rank": [11, "dm"],
                "color": "white",
                "mass": {"int": "In excelso", "glo": True, "cre": True, "pre": "et Comm de Epiphania"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },

            ##      if x == "I in Quadragesima":

            # Ash Wednesday and the follwing
            "de_AshWed": {
                "feast": "Dies Cinerum",
                "rank": [3, "s I cl"],
                "color": "purple",
                "mass": {"int": "Misereris", "glo": True, "cre": True, "pre": "de Quadragesima"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (False,),
                "fasting": True,
            },
            "AshWed_f5": {
                "feast": "Feria V post Diem Cinerum",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Dum clamarem", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (False,),
                "fasting": True,
            },
            "AshWed_f6": {
                "feast": "Feria VI post Diem Cinerum",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Audivit", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (False,),
                "fasting": True,
            },
            "AshWed_fs": {
                "feast": "Sabbatum post Diem Cinerum",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Audivit", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (False,),
                "fasting": True,
            },

            "D_Lent_1": {
                "feast": "Dominica I in Quadragesima",
                "rank": [1, "sd I cl"],
                "color": "purple",
                "mass": {"int": "Invocabit me", "glo": False, "cre": True, "pre": "de Quadragesima"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": (False,),
                "fasting": False,
            },

            # Ember days in Lent
            "Ember_Lent_4": {
                "feast": "Feria IV Quatuor Temporum Quadragesimæ",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Reminiscere", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": True,
            },
            "Ember_Lent_6": {
                "feast": "Feria VI Quatuor Temporum Quadragesimæ",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "De necessitatibus", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": True,
            },
            "Ember_Lent_s": {
                "feast": "Sabbatum Quatuor Temporum Quadragesimæ",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Intret", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": True,
            },

            "SevenSorrows": {
                "feast": "Septem Dolorum BMV",
                "rank": [14, "dm"],
                "color": "purple",
                "mass": {"int": "Stabant", "glo": False, "seq": "Stabat Mater", "cre": True, "pre": "de B. Maria Virg."},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": True,
            },

            # Holy Week Ferias:
            # TODO: check the verbose rank
            "de_Palm_f2": {
                "feast": "Feria II Majoris Hebd",
                "rank": [3, "s"],
                "color": "purple",
                "mass": {"int": "Judica, Domine", "glo": False, "cre": False, "pre": "de Cruce"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (9, 2, 6, 13, 1, 0,),
                "fasting": True,
            },
            "de_Palm_f3": {
                "feast": "Feria III Majoris Hebd",
                "rank": [3, "s"],
                "color": "purple",
                "mass": {"int": "Nos autem", "glo": False, "cre": False, "pre": "de Cruce"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (9, 2, 6, 13, 1, 0,),
                "fasting": True,
            },
            "de_Palm_f4": {
                "feast": "Feria IV Majoris Hebd",
                "rank": [3, "s"],
                "color": "purple",
                "mass": {"int": "In nomine Jesu", "glo": False, "cre": False, "pre": "de Cruce"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": True,
            },

            # Triduum:
            "de_Palm_f5": {
                "feast": "Feria V in Cœna Domini",
                "rank": [2, "d I cl"],
                "color": "white",
                "mass": {"int": "Nos autem", "glo": True, "cre": False, "pre": "de Cruce"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": True,
            },
            "de_Palm_f6": {
                "feast": "Feria VI in Parasceve",
                "rank": [2, "d I cl"],
                "color": "black",
                "mass": {"int": "Haec dicit", "glo": False, "cre": False, "pre": ""},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": True,
            },
            "de_Palm_fs": {
                "feast": "Sabbatum Sanctum",
                "rank": [2, "d I cl"],
                "color": "purple",
                "mass": {"int": "In Missa", "glo": True, "cre": False, "pre": "Te quidem"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": True,
            },

            # Easter Week TODO: Easter Vespers:
            "Easter": {
                "feast": "Dominica Resurrectionis",
                "rank": [1, "d I cl cum Oct privil I ord"],
                "color": "white",
                "mass": {"int": "Ressurexi", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "Paschalis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },
            "8Easter_f2": {
                "feast": "Feria II infra Oct. Paschæ",
                "rank": [2, "d I cl"],
                "color": "white",
                "mass": {"int": "Introduxit", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hanc Igitur, ut in die Paschae"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },
            "8Easter_f3": {
                "feast": "Feria III infra Oct. Paschæ",
                "rank": [2, "d I cl"],
                "color": "white",
                "mass": {"int": "Aqua sapientiae", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hanc Igitur, ut in die Paschae"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },
            "8Easter_f4": {
                "feast": "Feria IV infra Oct. Paschæ",
                "rank": [3, "sd"],
                "color": "white",
                "mass": {"int": "Venite", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hanc Igitur, ut in die Paschae"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },
            "8Easter_f5": {
                "feast": "Feria V infra Oct. Paschæ",
                "rank": [3, "sd"],
                "color": "white",
                "mass": {"int": "Victricem", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hang Igitur, ut in die Paschae"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },
            "8Easter_f6": {
                "feast": "Feria VI infra Oct. Paschæ",
                "rank": [3, "sd"],
                "color": "white",
                "mass": {"int": "Eduxit eos", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hanc Igitur, ut in die Paschae"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },
            "WhitSaturday": {
                "feast": "Sabbatum in Albis",
                "rank": [3, "sd"],
                "color": "white",
                "mass": {"int": "Eduxit Dominus", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hanc Igitur, ut in die Paschae"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },

            # Solemnity of St. Joseph  TODO: add the octave
            "StJoseph": {
                "feast": "Solemnitas S Joseph, Sponsi BMV", #, C. et Ecclesiæ Universalis Patroni",
                "rank": [2, "d I cl cum Oct Communi"],
                "color": "white",
                "mass": {"int": "Justus ut palma", "glo": True, "cre": True, "pre": "de S Joseph"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },
            "8_StJoseph": {
                "feast": "Octava Solemnitatis S Joseph",
                "rank": [13, "dm"],
                "color": "white",
                "mass": {"int": "Missa", "glo": True, "cre": True, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },

            # Rogation Days
            "Rogation_1": {
                "feast": "Feria II in Rogationibus",
                "rank": [19, "feria"],
                "color": "purple",
                "mass": {"int": "Exaudivit", "glo": False, "cre": True, "pre": "Paschalis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 13, 0, 0,),
                "fasting": False,
            },
            "Rogation_2": {
                "feast": "Feria III in Rogationibus",
                "rank": [23, "feria"],
                "color": "purple",
                "mass": {"int": "Exaudivit", "glo": False, "cre": True, "pre": "Paschalis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 13, 0, 0,),
                "fasting": False,
            },
            "Rogation_3": {
                "feast": "Feria IV in Rogationibus in Vigilia Ascensionis ",
                "rank": [23, "feria"],
                "color": "purple",
                "mass": {"int": "Exaudivit", "glo": False, "cre": True, "pre": "Paschalis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (9, 2, 6, 13, 3, 0,),
                "fasting": False,
            },


            # Ascension
            "Ascension": {
                "feast": "Ascensio DNJC",
                "rank": [2, "d I cl cum Oct privil 3 ord"],
                "color": "white",
                "mass": {"int": "Viri Galilæi", "glo": True, "cre": True, "pre": "et Comm de Ascensione"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },
            "8_Ascension": {
                "feast": "Oct. Ascensionis DNJC",
                "rank": [13, "dm"],
                "color": "white",
                "mass": {"int": "Viri Galilæi", "glo": True, "cre": True, "pre": "et Comm de Ascensione"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },

            "p_Ascension_f6": {  # TODO: this day has special rules
                "feast": "Oct. Ascensionis DNJC",
                "rank": [13, "dm"],
                "color": "white",
                "mass": {"int": "Viri Galilæi", "glo": True, "cre": True, "pre": "et Comm de Ascensione"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },

            ##  }
            ##      )
            ##      ascension_day = easter(year) + week(i) + indays(5)
            ##      if x == "Dominica infra Octavam Ascensionis":
            ##      for j, y in enumerate(ROMANS[1: 6], start=1):
            ##      if ascension_day + indays(j) == easter(year) + week(i):
            ##      continue
            ##      elif (ascension_day + indays(j)).strftime("%A") == "Saturday":

            # TODO: see if this is right
            "D_Ascension": {
                "feast": "Dominica infra Oct. Ascensionis",
                "rank": [16, "sd"], # FIX: check the rank and the Introit
                "color": "white",
                "mass": {"int": "Exaudi, Domine", "glo": True, "cre": False, "pre": "de Ascensione"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (5, 1, 6, 13, 3, 0,),
                "fasting": False,
            },

            "S_8_Ascension": {
                "feast": "Sabbatum infra Oct. Ascensionis",
                "rank": [17, "sd"],
                "color": "white",
                "mass": {"int": "Exaudi, Domine", "glo": True, "cre": False, "pre": "de Ascensione"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },

            "WhitSunday": {
                "feast": "Dominica in Albis",
                "rank": [1, "dm I cl"],
                "color": "white",
                "mass": {"int": "Quasi modo", "glo": True, "cre": True, "pre": "Paschalis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": (False,),
                "fasting": False,

            },

            "V_Pentecost": {
                "feast": "Sabbatum Vigilia Pentecostes",
                "rank": [3, "d I cl Vig privil I cl"],
                "color": "red",
                "mass": {"int": "Cum sanctificatus", "glo": True, "cre": False, "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": True,
            },

            # Pentecost Week
            "Pentecost": {
                "feast": "Dominica Pentecostes",
                "rank": [1, "d I cl cum Oct privil I ord"],
                "color": "red",
                "mass": {"int": "Spiritus Domini", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },
            # TODO: see if the first two ferias are 2 or 3
            "8Pent_f2": {
                "feast": "Feria II infra Oct. Pentecostes",
                "rank": [3, "d I cl"],
                "color": "red",
                "mass": {"int": "Cibavit eos", "glo": True, "cre": True, "seq": "Veni, Sancte Spiritus", "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (False,),
                "fasting": False,
            },
            "8Pent_f3": {
                "feast": "Feria III infra Oct. Pentecostes",
                "rank": [3, "d I cl"],
                "color": "red",
                "mass": {"int": "Cibavit eos", "glo": True, "cre": True, "seq": "Veni, Sancte Spiritus", "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (False,),
                "fasting": False,
            },
            "8Pent_f5": {
                "feast": "Feria V infra Oct. Pentecostes",
                "rank": [3, "d I cl"],
                "color": "red",
                "mass": {"int": "Accepite jucunditatem", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (False,),
                "fasting": False,
            },

            # TODO: see how these are listed in the missal:
            ##  {
            ##      str(pent_date + indays(j + 1)): {
            ##          "feast": "Feria " + y + " infra Oct. Pentecostes",
            ##          "rank": [3, "d I cl"],
            ##          "color": "red",
            ##          "mass": {"int": "Accepite jucunditatem", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "et Comm et Hanc Igitur de Pentecoste"},
            ##          "com": [],
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": "feria",
            ##          "nobility": False
            ##      }
            ##  }
            ##  )
            ##  cycle.update(
            ##  {
            ##      str(pent_date + indays(j + 2)): {
            ##          "feast": "Sabbatum infra Oct. Pentecostes",
            ##          "rank": [3, "sd"],
            ##          "color": "red",
            ##          "mass": {"int": "Missa", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "Communis"},
            ##          "com": [],
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": "feria",
            ##          "nobility": False
            ##      },


            # Ember Days after Pentecost
            "Ember_Pent_4": {
                "feast": "Feria IV Quatuor Temporum infra Oct. Pentecostes",
                "rank": [3, "sd"],
                "color": "red",
                "mass": {"int": "Deus, dum egredereris", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (False,),
                "fasting": True,
            },
            "Ember_Pent_6": {
                "feast": "Feria VI Quatuor Temporum infra Oct. Pentecostes",
                "rank": [3, "sd"],
                "color": "red",
                "mass": {"int": "Repleatur os meum", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (False,),
                "fasting": True,
            },
            "Ember_Pent_s": {
                "feast": "Sabbatum Quatuor Temporum infra Oct. Pentecostes",
                "rank": [3, "sd"],
                "color": "red",
                "mass": {"int": "Caritas Dei", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (False,),
                "fasting": True,
            },

            # First three post-Pentecost Sundays
            "Trinity": {
                "feast": "Festum Sanctissimæ Trinitatis",
                "rank": [2, "d I cl"],
                "color": "white",
                "mass": {"int": "Benedicta sit", "glo": True, "cre": True, "pre": "de Ssma Trinitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },
            "D_Pent_2": {
                "feast": "Dominica infra Oct. Ssmi Corporis Christi", #Christi (Dominica II post Pentecosten)",
                "rank": [12, "sd"],
                "color": "green",
                "mass": {"int": "Factus est", "glo": True, "seq": "Lauda, Sion, Salvatorem", "cre": True, "pre": "de Nativitate, vel de Ssma Trinitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": (False,),
                "fasting": False,
            },
            "D_Pent_3": {
                "feast": "Dominica infra Oct. Ssmi Cordis DNJC",  # (Dominica III post Pentecosten)",
                "rank": [12, "sd"],
                "color": "green",
                "mass": {"int": "Respice in me", "glo": True, "cre": True, "pre": "de sacratissimo Code Jesu"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": (False,),
                "fasting": False,
            },


            # TODO: update the ferias with the below information
            ##  {
            ##      str(corpus_christi + indays(j + 1)): {
            ##          "feast": fer_num+" infra Oct. Ssmi Corporis Christi",
            ##          "rank": [9, "sd"],
            ##          "color": "white",
            ##          "mass": {"int": "Factus est", "glo": True, "seq": "Lauda, Sion, Salvatorem", "cre": True, "pre": "de Nativitate"},
            # "com": [],
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": "feria",
            ##          "nobility": False
            ##      }
            ##  }
            ##  )
            ##  cycle.update(
            ##  {

            # Corpus Christi
            "CorpusChristi": {
                "feast": "Sanctissimi Corporis Christi",
                "rank": [2, "d I cl cum Oct privil 2 ord"],
                "color": "white",
                "mass": {"int": "Cibavit eos", "glo": True, "seq": "Lauda, Sion", "cre": True, "pre": "de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },
            "8_CorpusChristi": {
                "feast": "Octava Ssmi Corporis Christi",
                "rank": [4, "dm"],
                "color": "white",
                "mass": {"int": "Cibavit eos", "glo": True, "seq": "Lauda, Sion", "cre": True, "pre": "de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },

            ##  {
            ##      str(ssmi_cordis + indays(j + 1)): {
            ##          "feast": fer_num+" infra Oct. Ssmi Cordis DNJC",
            ##          # ? is this supposed to be within a common octave?
            ##          "rank": [18, "sd"],
            ##          "color": "white",
            ##          "mass": {"int": "Respice in me", "glo": True, "cre": True, "pre": "de Ssmo Corde Iesu vel de Ssma Trinitate"},
            #"com": [],
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": "dominica",
            ##          "nobility": False
            ##      },
            ##  }

            # Sacred Heart
            "SacredHeart": {
                "feast": "Sacratissimi Cordis Jesu",
                "rank": [2, "d I cl cum Oct privil 3 ord"],
                "color": "white",
                "mass": {"int": "Cogitationes", "glo": True, "cre": True, "pre": "de Ssmo Corde Iesu"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (1, 0, 3, 1, 1, 0),
                "fasting": False,
            },
            "8_SacredHeart": {
                "feast": "Octava Sacratissimi Cordis Jesu",
                "rank": [13, "dm"],
                "color": "white",
                "mass": {"int": "Cogitationes", "glo": True, "cre": True, "pre": "de Ssmo Corde Iesu"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (False,),
                "fasting": False,
            },

            ##                                                                                                                                                                      }
            ##  )
            ##  for t in range(6):
            ##  cycle.update(
            ##  {
            ##      str(post_pent_count + week(p) + indays(t+1)): {
            ##          "feast": "De ea",
            ##          "rank": [23, "s"],
            ##          "color": "green",
            ##          "mass": {"int": PENTECOST_MASSES[p], "note": "de Dom præc", "glo": True, "cre": False, "pre": "Communis"},
            ##          "com": [{"oration": "A cunctis"}, {"oration": "ad libitum"}],
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": "feria",
            ##          "nobility": (8, 2, 6, 13, 3, 0,),
            ##      },
            ##  }
            ##      )
            ##  elif count == 20 and post_pent_sundays == 23:
            ##  cycle.update(  # todo anticipate the 23rd sunday and celebrate the 24th
            ##  {

            # "D_UltPent_23": {
            #     "feast": "Dominica XXIII et ultima post Pentecosten",
            #     "rank": [12, "sd"],
            #     "color": "green",
            #     "mass": {"int": PENTECOST_MASSES[-1], "glo": True, "cre": True, "pre": "de Trinitate"},
            #     "com": [{"oration": "A cunctis"}, {"oration": "ad libitum"}],
            #     "matins": {},
            #     "lauds": {},
            #     "prime": {},
            #     "little_hours": {},
            #     "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
            #     "compline": {},
            #     "office_type": False,
            #     "nobility": (False,),
            #     "fasting": False,
            # },

            ##                                                                                                                                                                              }
            ##  )
            ##  for t in range(6):
            ##  cycle.update(
            ##  {
            ##      str(post_pent_count + week(p) + indays(t+1)): {
            ##          "feast": "De ea",
            ##          "rank": [23, "s"],
            ##          "color": "green",
            ##          "mass": {"int": PENTECOST_MASSES[-1], "note": "de Dom præc", "glo": True, "cre": False, "pre": "Communis"},
            ##          "com": [{"oration": "A cunctis"}, {"oration": "ad libitum"}],
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": "feria",
            ##          "nobility": (8, 2, 6, 13, 3, 0,),
            ##      },
            ##  }
            ##  )
            ##      break
            ##      elif count == post_pent_sundays-3:
            ##      cycle.update(
            ##      {

            ##  }
            ##      )
            ##      for t in range(6):
            ##      cycle.update(
            ##      {
            ##          str(post_pent_count + week(p) + indays(t+1)): {
            ##              "feast": "De ea",
            ##              "rank": [23, "s"],
            ##              "color": "green",
            ##              "mass": {"int": PENTECOST_MASSES[-1], "note": "de Dom præc", "glo": True, "cre": False, "pre": "Communis"},
            ##              "com": [{"oration": "A cunctis"}, {"oration": "ad libitum"}],
            ##              "matins": {},
            ##              "lauds": {},
            ##              "prime": {},
            ##              "little_hours": {},
            ##              "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
            ##              "compline": {},
            ##              "office_type": "feria",
            ##              "nobility": (8, 2, 6, 13, 3, 0,),
            ##          },
            ##      }
            ##          )
            ##          break
            ##          else:
            ##          for y, x in enumerate(epiph_sunday_overflow, start=1):
            ##          cycle.update(
            ##          {


            ##      }
            ##          )
            ##          for t in range(6):
            ##          cycle.update(
            ##          {
            ##              str(post_pent_count + week(p+y) + indays(t+1)): {
            ##                  "feast": "De ea",
            ##                  "rank": [23, "s"],
            ##                  "color": "green",
            ##                  "mass": {"int": "Dicit Dominus", "note": "de Dom præc", "glo": True, "cre": False, "pre": "Communis"},
            ##                  "com": [{"oration": "A cunctis"}, {"oration": "ad libitum"}],
            ##                  "matins": {},
            ##                  "lauds": {},
            ##                  "prime": {},
            ##                  "little_hours": {},
            ##                  "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
            ##              "compline": {},
            ##              "office_type": "feria",
            ##              "nobility": (8, 2, 6, 13, 3, 0,),
            ##          },
            ##      }

            # Ember Days in September
            "Ember_Sept_4": {
                "feast": "Feria IV Quatuor Temporum Septembris",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Exsultate Deo", "glo": False, "cre": False, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (False,),
                "fasting": True,
            },
            "Ember_Sept_6": {
                "feast": "Feria VI Quatuor Temporum Septembris",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Laetetur cor", "glo": False, "cre": False, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (False,),
                "fasting": True,
            },
            "Ember_Sept_s": {
                "feast": "Sabbatum Quatuor Temporum Septembris",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Venite, adoremus", "glo": False, "cre": False, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (False,),
                "fasting": True,
            },

            # Christ the King
            "ChristKing": {
                "feast": "In Festo DNJC Regis",
                "rank": [2, "d I cl"],
                "color": "white",
                "mass": {"int": "Dignus est", "glo": True, "cre": True, "pre": "de DNJC Rege"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },

            # Ember Days of Advent
            "Ember_Advent_4": {
                "feast": "Feria IV Quatuor Temporum in Adventus",
                "rank": [19, "feria"], # TODO: check the rank for this
                "color": "purple",
                "mass": {"int": "Rorate cæli", "glo": False, "cre": False, "pre": "Communis"},
                "com": [{"oration": "Deus qui de beate"}, {"oration": "Ecclesiæ"}],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (9, 2, 6, 13, 3, 0),
                "fasting": True,
            },
            "Ember_Advent_6": {
                "feast": "Feria VI Quatuor Temporum in Adventus",
                "rank": [19, "feria"], # TODO: check the rank for this
                "color": "purple",
                "mass": {"int": "Prope es tu", "glo": False, "cre": False, "pre": "Communis"},
                "com": [{"oration": "Deus qui de beate"}, {"oration": "Ecclesiæ"}],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (9, 2, 6, 13, 3, 0),
                "fasting": True,
            },
            "Ember_Advent_s": {
                "feast": "Sabbatum Quatuor Temporum in Adventus",
                "rank": [19, "feria"],  # TODO: check the rank for this
                "color": "purple",
                "mass": {"int": "Veni, et ostende", "glo": False, "cre": False, "pre": "Communis"},
                "com": [{"oration": "Deus qui de beate"}, {"oration": "Ecclesiæ"}],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (9, 2, 6, 13, 3, 0),
                "fasting": True,
            },


            # Christmastide
            "V_Christmas": {
                "feast": "Vigilia Nativitas DNJC",
                "rank": [3, "d I cl Vig privil I cl"],
                "color": "purple",
                "mass": {"int": "Hodie scietis", "glo": False, "cre": False, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (False,),
                "fasting": True,
            },
            "DV_Christmas": {
                "feast": "Vigilia Nativitas DNJC",
                "rank": [3, "d I cl Vig privil I cl"],
                "color": "purple",
                # TODO: add commemoration of the fourth Sunday of Advent
                "mass": {"int": "Hodie scietis", "glo": False, "cre": True, "pre": "de Trinitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (False,),
                "fasting": False,
            },
            "Christmas": {
                "feast": "Nativitas DNJC",
                "rank": [2, "d I cl cum Oct privil 3 ord"],
                "color": "white",
                "mass": {
                    "Ad Primam Missam": {"int": "Domine dixit", "glo": True, "cre": True, "pre": r"et Comm (in hac Missa tantum dicitur \textit{noctem}) de Nativitate"},
                    "Ad Secundam Missam": {"int": "Lux fulgebit", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                    "Ad Tertiam Missam": {"int": "Puer natus", "glo": True, "cre": True, "pre": "et Comm de Nativitate", "proper_last_gospel": "Epiph"},
                },
                "matins": {},
                "lauds": {"psalms": "sunday"},
                "prime": {"v_r": "Qui natus es"},
                "little_hours": {"psalms": "sunday"},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {"sunday": True,},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },
            "D_Christmas_r": {
                "feast": "Dominica Infra Octavam Nativitatis reposita",
                "rank": [12, "sd"],
                "color": "white",
                "mass": {"int": "Dum medium silentium", "glo": True, "cre": True, "pre": "de Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": (False,),
                "fasting": False,
            },
            "D_Christmas": {
                "feast": "Dominica Infra Octavam Nativitatis",
                "rank": [12, "sd"],
                "color": "white",
                "mass": {"int": "Dum medium", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": (False,),
                "fasting": False,
            },
            "8_Chritmas_f6": {
                "feast": "Feria VI infra Octavam Nativitatis",
                "rank": [16, "sd"],
                "color": "white",
                "mass": {"int": "Puer natus est nobis", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""}, "office_type": "feria",
                "compline": {},
                "nobility": (False,),
                "fasting": False,
            },
            "StStephan": {
                "feast": "S Stephani Protomartyris",
                "rank": [10, "d II cl cum Oct simplici"],
                "color": "red",
                "mass": {"int": "Sederunt", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },
            "StJohn": {
                "feast": "S Joannis Ap Ev",
                "rank": [10, "d II cl cum Oct simplici"],
                "color": "white",
                "mass": {"int": "In medio ecclesiæ", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },
            "StsInnocents": {
                "feast": "Ss Innocentium Mm",
                "rank": [10, "d II cl cum Oct simplici"],
                "color": "red",
                "mass": {"int": "Ex ore infantium", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },
            "StThomas": {
                "feast": "S Thomæ EM",
                "rank": [15, "d"],
                "color": "red",
                "mass": {"int": "Gaudeamus omnes", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },
            "StSylvester": {
                "feast": "S Silvestri I PC",
                "rank": [15, "d"],
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": False, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },

            # TEST:
            "D_StThomas": {
                "feast": "S Thomæ EM",
                "rank": [15, "d"],
                "color": "red",
                "mass": {"int": "Gaudeamus omnes", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },
            "D_StSylvester": {
                "feast": "S Silvestri I PC",
                "rank": [15, "d"],
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": False, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (False,),
                "fasting": False,
            },
            # TODO: add the Sundays if the fall on St. Thomas or St. Sylvester
        }

        self.data = self.easy_data |\
            self.epiphany_time() |\
            self.epiphany_octave() |\
            self.septuagesima_time() |\
            self.lent_sundays() |\
            self.paschaltime() |\
            self.ascension_ferias() |\
            self.corpus_ferias() |\
            self.sacredheart_ferias() |\
            self.solemnity_st_joseph() |\
            self.pentecost_sundays() |\
            self.pentecost_epiphany_sundays() |\
            self.last_pentecost() |\
            self.advents() |\
            self.three_weeks_after_pentecost()

    def lent_sundays(self) -> dict:
        the_days = {}
        normal_lents = [f"D_Lent_{l+1}" for l in range(4)]
        later_lents = ["D_Passion_5", "D_Palm_6"]
        lents = [*normal_lents, *later_lents]
        rank = 8
        for x, date in enumerate(lents):
            if x in [0, 1, 3]:
                rank = 1
            else:
                rank = 8
            for feria in range(7):
                if feria == 0:
                    the_days |= {
                        date: {
                            "feast": f"""Dominica {f'''infra Hebd {integer_to_roman(x+1)} in Quadragesima{' (Lætare)' if x+1 == 4 else ''}''' if x < 4 else '''Passione''' if x == 4 else '''Palmis''' }""",
                            "rank": [rank, "sd I cl"],  # FIX: check this
                            "color": f"{'purple' if x+1 != 4 else 'pink'}",
                            "mass": {
                                "int": "",  # TODO: add all of the Introits
                                "glo": False,
                                "cre": False,
                                "pre": "de Quadragesima" if x < 6 else "de Cruce",
                            },
                            "matins": {},
                            "lauds": {},
                            "prime": {},
                            "little_hours": {},
                            "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                            "compline": {},
                            "office_type": False,
                            "nobility": (False,),
                            "fasting": False,
                        }
                    }
                else:
                    the_days |= {
                        f"de_{'Lent' if x < 4 else 'Passion'}_f{feria+1 if feria != 6 else 's'}": {
                            # "feast": f"Feria {integer_to_roman(feria+1)} infra Hebd {integer_to_roman(x+1)} in Quadragesima",
                            "feast": "De ea",
                            "rank": [19, "feria"],
                            "color": "purple",
                            "mass": {
                                "int": "", # TODO: add all of the Lent feria Introits
                                "glo": False,
                                "cre": False,
                                "pre": "de Quadragesima" if x < 6 else "de Cruce",
                            },
                            "matins": {},
                            "lauds": {},
                            "prime": {},
                            "little_hours": {},
                            "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                            "compline": {},
                            "office_type": False,
                            "nobility": (9, 2, 6, 13, 3, 0), # FIX: Lent has higher ranking ferias?
                            "fasting": True,
                        }
                    }
        return the_days

    def ascension_ferias(self) -> dict:
        return { # NOTE: there are duplicates, but does it matter?
            f"in_8_Ascension_{date}": {
                "feast": f"De {integer_to_roman(date)} die infra Oct. Ascensionis",
                "rank": [16, "sd"],
                "color": "white",
                "mass": {"int": "Viri galilæi", "glo": True, "cre": False, "pre": "de Ascensione"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (9, 2, 6, 13, 3, 0),
                "fasting": False,
            } for date in range(1,8)
        }

    def corpus_ferias(self) -> dict:
        return {
            f"{date+1}_in_8_CorpusChristi": {
                "feast": f"De {integer_to_roman(date+1)} die infra Oct. Ssmi Corporis Christi",
                "rank": [9, "feria"],
                "color": "white",
                "mass": {"int": "Cibavit eos", "glo": True, "seq": "Lauda, Sion", "cre": True, "pre": "de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (9, 2, 6, 13, 3, 0),
                "fasting": False,
            } for date in range(1,8)
        }

    def sacredheart_ferias(self) -> dict:
        return {
            f"{date+1}_in_8_SacredHeart": {
                "feast": f"De {integer_to_roman(date+1)} die infra Oct. Sacratissimi Cordis Jesu",
                "rank": [18, "sd"], # TODO: verify this rank
                "color": "white",
                "mass": {"int": "Cogitationes", "glo": True, "cre": True, "pre": "de Ssmo Corde Iesu"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (1, 0, 3, 1, 1, 0),
                "fasting": False,
            } for date in range(1,8)
        }


    def pentecost_sundays(self) -> dict:
        # TODO: add the first 4 Sundays after Pentecost (excluding Trinity)
        pentecost_season = {}
        for date in range(4, 29):
            pentecost_season |= {
                f"D_Pent_{date}": {
                    "feast": f"Dominica {integer_to_roman(date)} post Pentecosten",
                    "rank": [12, "sd"],
                    "color": "green",
                    "mass": {"int": f"{PENTECOST_MASSES[date-5] if date >= 4 else ''}", "glo": True, "cre": True, "pre": "de Trinitate"},
                    "com": [{"oration": "A cunctis", }, {"oration": "ad libitum", },],
                    "matins": {},
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                    "compline": {},
                    "office_type": "dominica",
                    "nobility": (False,),
                    "fasting": False,
                }
            }
            for feria in range(6):
                pentecost_season |= {
                    f"de_Pent_{date}_f{feria+2 if feria != 5 else 's'}": {
                        "feast": "De ea",
                        "rank": [23, "sd"],
                        "color": "green",
                        "mass": {"int": f"{PENTECOST_MASSES[date-5] if date >= 4 else ''}", "glo": True, "cre": False, "pre": "Communi"},
                    "com": [{"oration": "A cunctis", }, {"oration": "ad libitum", },],
                        "matins": {},
                        "lauds": {},
                        "prime": {},
                        "little_hours": {},
                        "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                        "compline": {},
                        "office_type": "dominica",
                        "nobility": (9, 2, 6, 13, 3, 0),
                        "fasting": False,
                    }
                }
        return pentecost_season

    def pentecost_epiphany_sundays(self) -> dict:
        """
        This is really rough and might not be too efficient, but 
        it works for now.
        """
        epiphany_pents = {}
        for pent in range(22,29):
            for epiph in range(3,7):
                epiphany_pents |= {
                    f"D_Epiph_{epiph}_{pent}": {
                        "feast": f"Dominica {integer_to_roman(pent)} post Pentecosten, {integer_to_roman(epiph)} Epiphania",
                        "rank": [12, "sd"],
                        "color": "green",
                        "mass": {"int": "Dicit Dominus", "glo": True, "cre": True, "pre": "de Trinitate"},
                    "com": [{"oration": "A cunctis", }, {"oration": "ad libitum", },],
                        "matins": {},
                        "lauds": {},
                        "prime": {},
                        "little_hours": {},
                        "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                        "compline": {},
                        "office_type": "dominica",
                        "nobility": (False,),
                        "fasting": False,
                    }
                }
                for feria in range(6):
                    epiphany_pents |= {
                        f"de_Epiph_{epiph}_{pent}_f{feria+2 if feria != 5 else 's'}": {
                            "feast": "De ea",
                            "rank": [23, "feria"],
                            "color": "green",
                            "mass": {"int": "Dicit Dominus", "glo": True, "cre": False, "pre": "Communi"},
                    "com": [{"oration": "A cunctis", }, {"oration": "ad libitum", },],
                            "matins": {},
                            "lauds": {},
                            "prime": {},
                            "little_hours": {},
                            "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                            "compline": {},
                            "office_type": "dominica",
                            "nobility": (9, 2, 6, 13, 3, 0),
                            "fasting": False,
                        }
                    }
        return epiphany_pents

    def last_pentecost(self) -> dict:
        last_pents = {}
        for pent in range(23, 29):
            last_pents |= {
                f"D_UltPent_{pent}": {
                    "feast": f"Dominica {integer_to_roman(pent)} et ultima post Pentecosten",
                    "rank": [12, "sd"],
                    "color": "green",
                    "mass": {"int": PENTECOST_MASSES[-1], "glo": True, "cre": True, "pre": "de Trinitate"},
                    "com": [{"oration": "A cunctis", }, {"oration": "ad libitum", },],
                    "matins": {},
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                    "compline": {},
                    "office_type": "dominica",
                    "nobility": (False,),
                    "fasting": False,
                }
            }
            for feria in range(6):
                last_pents |= {
                    f"de_UltPent_{pent}_f{feria+2 if feria != 5 else 's'}": {
                        "feast": "De ea",
                        "rank": [12, "sd"], # FIX: fix the rank
                        "color": "green",
                        "mass": {"int": PENTECOST_MASSES[-1], "glo": True, "cre": False, "pre": "Communi"},
                    "com": [{"oration": "A cunctis", }, {"oration": "ad libitum", },],
                        "matins": {},
                        "lauds": {},
                        "prime": {},
                        "little_hours": {},
                        "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                        "compline": {},
                        "office_type": "dominica",
                        "nobility": (9, 2, 6, 13, 3, 0),
                        "fasting": False,
                    }
                }
        return last_pents

    def advents(self) -> dict:
        advent_season = {}
        advent_sundays = [
            "Ad te levavi",
            "Populus Sion",
            "Gaudete",
            "Rorate cæli",
        ]
        for x, introit in enumerate(advent_sundays):
            advent_season |= {
                f"D_Advent_{x+1}": { # TODO: verify that 2-4 advents are minor sundays
                                    "feast": f"Dominica {integer_to_roman(x+1)} Adventus",
                                    "rank": [1 if x == 0 else 12, f"{'sd I cl' if x == 0 else 'sd II cl'}"],
                                    "color": f"{'purple' if x+1 != 3 else 'pink'}",
                                    "mass": {"int": f"{introit}", "glo": False, "cre": True, "pre": "de Trinitate"},
                                    "com": [{"oration": "Deus qui de beate"},{"oration": "Ecclesiæ"}],
                                    "matins": {},
                                    "lauds": {},
                                    "prime": {},
                                    "little_hours": {},
                                    "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                                    "compline": {},
                                    "office_type": "dominica",
                                    "nobility": (False,),
                                    "fasting": False,
                                    }
            }
            for feria in range(6):
                advent_season |= {
                    f"Advent_{x+1}_f{feria+2 if feria != 5 else 's'}": {
                        "feast": "De ea",
                        "rank": [23, "feria"], # FIX: change the rank
                        "color": "purple",
                        "mass": {"int": f"{introit}", "glo": False, "cre": True, "pre": "de Trinitate"},
                        "com": [{"oration": "Deus qui de beate"},{"oration": "Ecclesiæ"}],
                        "matins": {},
                        "lauds": {},
                        "prime": {},
                        "little_hours": {},
                        "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                        "compline": {},
                        "office_type": "feria",
                        "nobility": (9, 2, 6, 13, 3, 0),
                        "fasting": False,
                    }
                }
        return advent_season

    def three_weeks_after_pentecost(self) -> dict:
        # NOTE: this is overkill, but it works, and is probably faster than a fix
        weeks = {}
        introits = [
            "Benedicta sit",
            "Factus est",
            "Respice in me",
        ]
        for x, introit in enumerate(introits):
            for feria in range(6):
                weeks |= {
                    f"de_Pent_{x+1}_f{feria+2 if feria != 5 else 's'}": {
                        "feast": "De ea",
                        "rank": [23, "feria"], # FIX: change the ranking
                        "color": "green", # TODO: check if this is right of the Trinity
                        "mass": {"int": introit, "glo": True, "seq": "Lauda, Sion, Salvatorem", "cre": False, "pre": "de Trinitate"},
                        "com": [],
                        "matins": {},
                        "lauds": {},
                        "prime": {},
                        "little_hours": {},
                        "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                        "compline": {},
                        "office_type": "ferial",
                        "nobility": (9, 2, 6, 13, 3, 0),
                        "fasting": False,
                    },
                }
        return weeks

    def paschaltime(self) -> dict:
        paschaltime = {}
        for week in range(6):
            paschaltime |= {
                f"D_Easter_{week+1}": {
                    "feast": f"Dominica {integer_to_roman(week+1)} post Resurrectionis",
                    "rank": [12, "sd"],
                    "color": "white",
                    "mass": {"int": "Missa", "glo": True, "cre": True, "pre": "Communis"},
                    "com": [], # FIX: easter preface?
                    "matins": {},
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                    "compline": {},
                    "office_type": "dominica",
                    "nobility": (False,),
                    "fasting": False,
                }
            }
            for feria in range(6):
                pass
                paschaltime |= {
                    f"de_Easter_{week+1}_f{feria+2 if feria != 5 else 's'}": {
                        "feast": "De ea",
                        "rank": [23, "feria"], # FIX: check the ranking
                        "color": "white",
                        "mass": {"int": "Missa", "glo": True, "cre": False, "pre": "Communis"},
                        "com": [], # FIX: easter preface?
                        "matins": {},
                        "lauds": {},
                        "prime": {},
                        "little_hours": {},
                        "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                        "compline": {},
                        "office_type": "feria",
                        "nobility": (9, 2, 6, 13, 3, 0),
                        "fasting": False,
                    }
                }
        return paschaltime

    def solemnity_st_joseph(self) -> dict:
        solemnity_ferias = {}
        for feria in range(6):
            solemnity_ferias |= {
                f"{feria+2}_in_8_StJoseph": {
                    "feast": f"De {integer_to_roman(feria+2)} die infra Solemnitas S Joseph",
                    "rank": [18, "feria"], # FIX: check the verbose rank
                    "color": "white",
                    "mass": {"int": "Justus ut palma", "glo": True, "cre": True, "pre": "de S Joseph"},
                    "com": [],
                    "matins": {},
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                    "compline": {},
                    "office_type": False,
                    "nobility": (9, 2, 6, 13, 3, 0),
                    "fasting": False,
                }
            }
        return solemnity_ferias

    def septuagesima_time(self) -> dict:
        septuagesima = {}
        for x, sunday in enumerate(["Septuagesima", "Sexagesima", "Quinquagesima"]):
            septuagesima |= {
                sunday: {
                    "feast": f"Dominica in {sunday}",
                    "rank": [8, "sd II cl"],
                    "color": "purple",
                    "mass": {"int": "", "glo": False, "cre": True, "pre": "Communis"},
                    "com": [], # FIX: preface
                    "matins": {},
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                    "compline": {},
                    "office_type": "dominica",
                    "nobility": (False,),
                    "fasting": False,
                }
            }
            for feria in range(6):
                septuagesima |= {
                    f"de_{sunday[:4]}_f{feria+2 if feria != 5 else 's'}": {
                        "feast": "De ea",
                        "rank": [23, "feria"],
                        "color": "purple",
                        "mass": {"int": "", "glo": False, "cre": True, "pre": "Communis"},
                        "com": [], # FIX: preface
                        "matins": {},
                        "lauds": {},
                        "prime": {},
                        "little_hours": {},
                        "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                        "compline": {},
                        "office_type": "dominica",
                        "nobility": (9, 2, 6, 13, 3, 0),
                        "fasting": False,
                    }
                }
        return septuagesima

    def epiphany_time(self) -> dict:
        epiphany = {}
        for sunday in range(6):
            epiphany |= {
                f"D_Epiph_{sunday+1}": {
                    "feast": f"Dominica {integer_to_roman(sunday+1)} post Epiphaniam",
                    "rank": [12, "sd"],
                    "color": "green",
                    "mass": {"int": "Omnis terra", "glo": True, "cre": True, "pre": "de Ssma Trinitate"},
                    "com": [],  # FIX: introit
                    "matins": {},
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                    "compline": {},
                    "office_type": "dominica",
                    "nobility": (False,),
                    "fasting": False,
                }
            }
            for feria in range(6):
                epiphany |= {
                    f"de_Epiph_{sunday+1}_{feria+2 if feria != 5 else 's'}": {
                        "feast": "De ea",
                        "rank": [23, "feria"],
                        "color": "white",
                        "mass": {"int": "Omnis terra", "glo": True, "cre": False, "pre": "Communis"},
                        "com": [],
                        "matins": {},
                        "lauds": {},
                        "prime": {},
                        "little_hours": {},
                        "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                        "compline": {},
                        "office_type": "feria",
                        "nobility": (8, 2, 6, 13, 3, 0,),
                        "fasting": False,
                    }
                }
        return epiphany

    def epiphany_octave(self) -> dict:
        octave = {
            "8_Epiph_fs": {
                "feast": "Sabbato infra Oct. Epiphaniæ",
                "rank": [9, "feria"],
                "color": "white",
                "mass": {"int": "Ecce advenit", "glo": True, "cre": True, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (8, 2, 6, 13, 3, 0,), # FIX: check this rank
                "fasting": False,
            },
        }
        for feria in range(6):
            octave |= {
                f"8_Epiph_f{feria+2}": {
                    "feast": f"De {integer_to_roman(feria+2)} die infra Oct. Epiphaniæ",
                    "rank": [9, "feria"],
                    "color": "white",
                    "mass": {"int": "Ecce advenit", "glo": True, "cre": True, "pre": "Communis"},
                    "com": [],
                    "matins": {},
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                    "compline": {},
                    "office_type": "feria",
                    "nobility": (8, 2, 6, 13, 3, 0,), # FIX: check this rank
                    "fasting": False,
                }
            }
        return octave
