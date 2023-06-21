from ordo_tools.liturgical_dates import integer_to_roman


class TemporalData:

    def __init__(self):
        self.easy_data = {
            "Circumcision": {
                "feast": "Circumcisio DNJC et Oct. Nativitatis" ,
                "rank": [3, "d II cl"],
                "color": "white",
                "mass": {"int": "Puer natus", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": False,
                "fasting": False,
            },
            "8_Stephen": {
                "feast": "Octava S. Stephani Protomartyris",
                "rank": [20, "s"],
                "color": "white",
                "mass": {"int": "Sederunt", "glo": True, "cre": False, "pre": "de Nativitate"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            },
            "8_John": {
                "feast": "Octava S. Joannis Ap Ev",
                "rank": [20, "s"],
                "color": "red",
                "mass": {"int": "Introit", "glo": True, "cre": True, "pre": "Communis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            },
            "8_Innocents": {
                "feast": "Octava Ss Innocentium Mm.",
                "rank": [20, "s"],
                "color": "red",
                "mass": {"int": "Ex ore infantium", "glo": True, "cre": True, "pre": "Communis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            },
            "SNameJesus": {
                "feast": "Ssmi Nominis Jesu",
                "rank": [10, "d II cl"],
                "color": "color",
                "mass": {"int": "In nomine Jesu", "glo": True, "cre": True, "pre": "de Nativitate"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": False,
                "fasting": False,
            },
            # FIX: also the octave of St. Stephen
            "SNameJesus+8_Ste": {
                "feast": "Ssmi Nominis Jesu",
                "rank": [10, "d II cl"],
                "color": "color",
                "mass": {"int": "In nomine Jesu", "glo": True, "cre": True, "pre": "de Nativitate"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": False,
                "fasting": False,
            },
            "Septuagesima": {
                "feast": "Dominica in Septuagesima",
                "rank": [8, "sd II cl"],
                "color": "purple",
                "mass": {"int": "Missa", "glo": False, "cre": True, "pre": "Communis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": False,
                "fasting": False,
            },
            "Sexagesima": {
                "feast": "Dominica in Sexagesima",
                "rank": [8, "sd II cl"],
                "color": "purple",
                "mass": {"int": "Missa", "glo": False, "cre": True, "pre": "Communis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": False,
                "fasting": False,
            },
            "Quinquagesima": {
                "feast": "Dominica in Quinquagesima",
                "rank": [8, "sd II cl"],
                "color": "purple",
                "mass": {"int": "Missa", "glo": False, "cre": True, "pre": "Communis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": False,
                "fasting": False,
            },
            "V_Epiphany": {
                "feast": "Vigilia Epiphaniæ",
                "rank": [12, "sd Vig privil 2 cl"],
                "color": "white",
                "mass": {"int": "Dum medium silentium", "glo": True, "cre": True, "pre": "de Nativitate"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": False,
                "fasting": False,
            },
            "Epiphany": {
                "feast": "Epiphania DNJC",
                "rank": [2, "d I cl cum Oct privil 2 ord"],
                "color": "white",
                "mass": {"int": "Ecce advenit", "glo": True, "cre": True, "pre": "de Epiphania"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": False,
                "fasting": False,
            },
            "8_Epiphany": {
                "feast": "Octava Epiphaniæ",
                "rank": [13, "dm"],
                "color": "white",
                "mass": {"int": "Ecce advenit", "glo": True, "cre": True, "pre": "Communis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            },
            "8_Epiph_fs": {
                "feast": "Sabbato infra Oct. Epiphaniæ",
                "rank": [9, "feria"],
                "color": "white",
                "mass": {"int": "Ecce advenit", "glo": True, "cre": True, "pre": "Communis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": False,
                "fasting": False,
            },
            "8_Epiph_f": {
                "feast": "De # die infra Oct. Epiphaniæ",
                "rank": [9, "feria"],
                "color": "white",
                "mass": {"int": "Ecce advenit", "glo": True, "cre": True, "pre": "Communis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": False,
                "fasting": False,
            },
            "D_Epiphany": {
                "feast": "In Octava Epiphaniæ",
                "rank": [13, "dm"],
                "color": "white",
                "mass": {"int": "Ecce advenit", "glo": True, "cre": True, "pre": "et Comm de Epiphania"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            },
            "HolyFamily": {
                "feast": "S. Familiæ Jesu, Mariæ, Joseph",
                "rank": [11, "dm"],
                "color": "white",
                "mass": {"int": "Exultat", "glo": True, "cre": True, "pre": "et communcantes de Epiphania"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            },
            "D_HolyFamily": {
                "feast": "S. Familiæ Jesu, Mariæ, Joseph; Dominica I infra Oct. Epiphaniæ",
                "rank": [11, "dm"],
                "color": "white",
                "mass": {"int": "In excelso", "glo": True, "cre": True, "pre": "et Comm de Epiphania"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            },
            # FIX: add each of the sundays
            "D_Epiph_2": {
                "feast": "Dominic II post Epiphaniam",
                "rank": [12, "sd"],
                "color": "white",
                "mass": {"int": "Omnis terra", "glo": True, "cre": True, "pre": "de Ssma Trinitate"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": False,
                "fasting": False,
            },

            # TODO: see if each epiphany has a proper Mass
            ##      str(epiph_counter + indays(t+1)): {
            ##          "feast": "De ea",
            ##          "rank": [23, "s"],
            ##          "color": "white",
            ##          "mass": {"int": "Omnis terra", "glo": True, "cre": False, "pre": "Communis"},
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": "feria",
            ##          "nobility": (8, 2, 6, 13, 3, 0,),
            ##      },
            ##  }

            ##      if x == "I in Quadragesima":

            "de_AshWed": {
                "feast": "Dies Cinerum",
                "rank": [3, "s I cl"],
                "color": "purple",
                "mass": {"int": "Misereris", "glo": True, "cre": True, "pre": "de Quadragesima"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": False,
                "fasting": True,
            },
            "AshWed_f5": {
                "feast": "Feria V post Diem Cinerum",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Dum clamarem", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": False,
                "fasting": True,
            },
            "AshWed_f6": {
                "feast": "Feria VI post Diem Cinerum",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Audivit", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": False,
                "fasting": True,
            },
            "AshWed_fs": {
                "feast": "Sabbatum post Diem Cinerum",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Audivit", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": False,
                "fasting": True,
            },

            "D_Lent_1": {
                "feast": "Dominica I in Quadragesima",
                "rank": [1, "sd I cl"],
                "color": "purple",
                "mass": {"int": "Invocabit me", "glo": False, "cre": True, "pre": "de Quadragesima"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": False,
                "fasting": False,
            },


            ##  )
            ##  for j, y in enumerate(FERIA):
            ##  if x == "de Passione" and y == "Feria VI":
            ##  cycle.update(


            "de_Passion_f6": {
                "feast": "Septem Dolorum BMV",
                "rank": [14, "dm"],
                "color": "purple",
                "mass": {"int": "Stabant", "glo": False, "seq": "Stabat Mater", "cre": True, "pre": "de B. Maria Virg."},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": True,
            },
            "Ember_Lent_4": {
                "feast": "Feria IV Quatuor Temporum Quadragesimæ",
                "rank": [3, "s"],
                "color": "purple",
                "mass": {"int": "Reminiscere", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": True,
            },
            "Ember_Lent_6": {
                "feast": "Feria VI Quatuor Temporum Quadragesimæ",
                "rank": [3, "s"],
                "color": "purple",
                "mass": {"int": "De necessitatibus", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": True,
            },
            "Ember_Lent_s": {
                "feast": "Sabbatum Quatuor Temporum Quadragesimæ",
                "rank": [3, "s"],
                "color": "purple",
                "mass": {"int": "Intret", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": True,
            },

            # Holy Week Ferias:
            "de_Palm_f2": {
                "feast": "Feria II Majoris Hebd",
                "rank": [3, "s"],
                "color": "purple",
                "mass": {"int": "Judica, Domine", "glo": False, "cre": False, "pre": "de Cruce"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": True,
            },
            "de_Palm_f3": {
                "feast": "Feria III Majoris Hebd",
                "rank": [3, "s"],
                "color": "purple",
                "mass": {"int": "Nos autem", "glo": False, "cre": False, "pre": "de Cruce"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": True,
            },
            "de_Palm_f4": {
                "feast": "Feria IV Majoris Hebd",
                "rank": [3, "s"],
                "color": "purple",
                "mass": {"int": "In nomine Jesu", "glo": False, "cre": False, "pre": "de Cruce"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": True,
            },

            # Triduum:
            "de_Palm_f5": {
                "feast": "Feria V in Cœna Domini",
                "rank": [2, "d I cl"],
                "color": "white",
                "mass": {"int": "Nos autem", "glo": True, "cre": False, "pre": "de Cruce"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": True,
            },
            "de_Palm_f6": {
                "feast": "Feria VI in Parasceve",
                "rank": [2, "d I cl"],
                "color": "black",
                "mass": {"int": "Haec dicit", "glo": False, "cre": False, "pre": ""},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": True,
            },
            "de_Palm_fs": {
                "feast": "Sabbatum Sanctum",
                "rank": [2, "d I cl"],
                "color": "purple",
                "mass": {"int": "In Missa", "glo": True, "cre": False, "pre": "Te quidem"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": True,
            },


            ##  }
            ##  )
            ##  elif x == "in Palmis":
            ##  cycle.update(
            ##  }
            ##  )
            ##  else:
            ##  if x == "IV in Quadragesima (Lætare)":
            ##  new_x = re.sub("\(Lætare\)", "", x)
            ##  else:
            ##  new_x = x



            ##  )
            ##  i += 1
            ##  cycle.update(
            ##  {

            # Easter Week
            # TODO: Easter Vespers:
            "Easter": {
                "feast": "Dominica Resurrectionis",
                "rank": [1, "d I cl cum Oct privil I ord"],
                "color": "white",
                "mass": {"int": "Ressurexi", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "Paschalis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": False,
                "fasting": False,
            },
            "8Easter_f2": {
                "feast": "Feria II infra Oct. Paschæ",
                "rank": [2, "d I cl"],
                "color": "white",
                "mass": {"int": "Introduxit", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hanc Igitur, ut in die Paschae"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            },
            "8Easter_f3": {
                "feast": "Feria III infra Oct. Paschæ",
                "rank": [2, "d I cl"],
                "color": "white",
                "mass": {"int": "Aqua sapientiae", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hanc Igitur, ut in die Paschae"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            },
            "8Easter_f4": {
                "feast": "Feria IV infra Oct. Paschæ",
                "rank": [3, "sd"],
                "color": "white",
                "mass": {"int": "Venite", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hanc Igitur, ut in die Paschae"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            },
            "8Easter_f5": {
                "feast": "Feria V infra Oct. Paschæ",
                "rank": [3, "sd"],
                "color": "white",
                "mass": {"int": "Victricem", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hang Igitur, ut in die Paschae"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            },
            "8Easter_f6": {
                "feast": "Feria VI infra Oct. Paschæ",
                "rank": [3, "sd"],
                "color": "white",
                "mass": {"int": "Eduxit eos", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hanc Igitur, ut in die Paschae"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            },
            "8Easter_fs": {
                "feast": "Sabbatum in Albis",
                "rank": [3, "sd"],
                "color": "white",
                "mass": {"int": "Eduxit Dominus", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hanc Igitur, ut in die Paschae"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            },

            ##  )
            ##  post_pent = [
            ##      "Dominica in Albis",
            ##      "Dominica II post Pascha",
            ##      "Dominica III post Pascha",
            ##      "Dominica IV post Pascha",
            ##      "Dominica V post Pascha",
            ##      "Dominica infra Octavam Ascensionis",
            ##  ]
            ##      for i, x in enumerate(post_pent, start=1):
            ##      if x == "Dominica II post Pascha":
            ##      cycle.update(
            ##      {

            "StJoseph": {
                "feast": "Solemnitas S. Joseph, Sponsi BMV, C. et Ecclesiæ Universalis Patroni",
                "rank": [2, "d I cl cum Oct Communi"],
                "color": "white",
                "mass": {"int": "Justus ut palma", "glo": True, "cre": True, "pre": "de S. Joseph"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            },

            ##      # todo We need all the days within the octave

            "8_StJoseph": {
                "feast": "Octava Solemnitatis S. Joseph",
                "rank": [13, "dm"],
                "color": "white",
                "mass": {"int": "Missa", "glo": True, "cre": True, "pre": "Communis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            },

            ##                                                                                                      },
            ##                                                                                                  }
            ##  )
            ##  if x == "Dominica V post Pascha":
            ##  ROGATION_MONDAY = easter(year) + week(i) + indays(1)
            ##  cycle.update(
            ##  {

            "Rogation_1": {
                "feast": "Feria II in Rogationibus",
                "rank": [19, "feria"],
                "color": "purple",
                "mass": {"int": "Exaudivit", "glo": False, "cre": True, "pre": "Paschalis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 13, 0, 0,),
                "fasting": True, # FIX: fast days?
            },
            "Rogation_2": {
                "feast": "Feria III in Rogationibus",
                "rank": [19, "feria"],
                "color": "purple",
                "mass": {"int": "Exaudivit", "glo": False, "cre": True, "pre": "Paschalis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 13, 0, 0,),
                "fasting": True, # FIX: fast days?
            },
            "Rogation_3": {
                "feast": "Feria IV in Rogationibus in Vigilia Ascensionis ",
                "rank": [19, "feria"],
                "color": "purple",
                "mass": {"int": "Exaudivit", "glo": False, "cre": True, "pre": "Paschalis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (9, 2, 6, 13, 3, 0,),
                "fasting": True, # FIX: fast days?
            },


            # Ascension
            "Ascension": {
                "feast": "Ascensio DNJC",
                "rank": [2, "d I cl cum Oct privil 3 ord"],
                "color": "white",
                "mass": {"int": "Viri Galilæi", "glo": True, "cre": True, "pre": "et Comm de Ascensione"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": False,
                "fasting": False,
            },
            "8_Ascension": {
                "feast": "Oct. Ascensionis DNJC",
                "rank": [13, "dm"],
                "color": "white",
                "mass": {"int": "Viri Galilæi", "glo": True, "cre": True, "pre": "et Comm de Ascensione"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
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

            "S_8_Ascension": {
                "feast": "Sabbatum infra Oct. Ascensionis",
                "rank": [16, "sd"],
                "color": "white",
                "mass": {"int": "Exaudi, Domine", "glo": True, "cre": False, "pre": "de Ascensione"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            },

            ##                                                                                                          }
            ##  )
            ##  else:
            ##  cycle.update(



            ##                                                                                                              }
            ##  )
            ##  if x == "Dominica in Albis":
            ##  cycle.update(
            ##  {
            ##  str(easter(year) + week(i)): {
            ##  "feast": x,
            ##  "rank": [1, "dm I cl"],
            ##  "color": "white",
            ##  "mass": {"int": "Quasi modo", "glo": True, "cre": True, "pre": "Paschalis"},
            ##  "matins": {},
            ##  "lauds": {},
            ##  "prime": {},
            ##  "little_hours": {},
            ##  "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##  "compline": {},
            ##  "office_type": "dominica",
            ##  "nobility": False
            ##                                                                                                                      }
            ##                                                                                                                  }
            ##  )
            ##  else:
            ##  cycle.update(
            ##  {
            ##  str(easter(year) + week(i)): {
            ##  "feast": x,
            ##  "rank": [12, "sd"],
            ##  "color": "white",
            ##  "mass": {"int": "Missa", "glo": True, "cre": True, "pre": "Communis"},
            ##  "matins": {},
            ##  "lauds": {},
            ##  "prime": {},
            ##  "little_hours": {},
            ##  "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##  "compline": {},
            ##  "office_type": "dominica",
            ##  "nobility": False
            ##                                                                                                                          }
            ##                                                                                                                      }
            ##  )
            ##  pent_date = easter(year) + week(i+1)
            ##  cycle.update(
            ##  {
            ##      str(pent_date - indays(1)): {
            ##          "feast": "Sabbatum Vigilia Pentecostes",
            ##          "rank": [3, "d I cl Vig privil I cl"],
            ##          "color": "red",
            ##          "mass": {"int": "Cum sanctificatus", "glo": True, "cre": False, "pre": "et Comm et Hanc Igitur de Pentecoste"},
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": False,
            ##          "nobility": False
            ##      },
            ##      str(pent_date): {
            ##      "feast": "Dominica Pentecostes",
            ##      "rank": [1, "d I cl cum Oct privil I ord"],
            ##      "color": "red",
            ##      "mass": {"int": "Spiritus Domini", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "et Comm et Hanc Igitur de Pentecoste"},
            ##      "matins": {},
            ##      "lauds": {},
            ##      "prime": {},
            ##      "little_hours": {},
            ##      "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##      "compline": {},
            ##      "office_type": "festiva",
            ##      "nobility": False
            ##  },
            ##                                                                                                                          }
            ##  )
            ##  for j, y in enumerate(ROMANS[1: 6]):
            ##  if y == "II" or y == "III":
            ##  cycle.update(
            ##  {
            ##      str(pent_date + indays(j + 1)): {   # ! Add all days within octave of pentecost
            ##          "feast": "Feria "+y+" infra Oct. Pentecostes",
            ##          "rank": [2, "d I cl"],
            ##          "color": "red",
            ##          "mass": {"int": "Cibavit eos", "glo": True, "cre": True, "seq": "Veni, Sancte Spiritus", "pre": "et Comm et Hanc Igitur de Pentecoste"},
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": "feria",
            ##          "nobility": False
            ##      }
            ##  }
            ##  )
            ##  else:
            ##  cycle.update(
            ##  {
            ##      str(pent_date + indays(j + 1)): {
            ##          "feast": "Feria " + y + " infra Oct. Pentecostes",
            ##          "rank": [3, "d I cl"],
            ##          "color": "red",
            ##          "mass": {"int": "Accepite jucunditatem", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "et Comm et Hanc Igitur de Pentecoste"},
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
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
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": "feria",
            ##          "nobility": False
            ##      },


            # Ember Days after Pentecost
            "Ember_Pent_4": {
                "feast": "Feria IV Quatuor Temporum infra Oct. Pentecostes",
                "rank": [19, "sd"],
                "color": "red",
                "mass": {"int": "Deus, dum egredereris", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": False,
                "fasting": False,
            },
            "Ember_Pent_6": {
                "feast": "Feria VI Quatuor Temporum infra Oct. Pentecostes",
                "rank": [19, "sd"],
                "color": "red",
                "mass": {"int": "Repleatur os meum", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": False,
                "fasting": False,
            },
            "Ember_Pent_s": {
                "feast": "Sabbatum Quatuor Temporum infra Oct. Pentecostes",
                "rank": [19, "sd"],
                "color": "red",
                "mass": {"int": "Caritas Dei", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": False,
                "fasting": False,
            },

            ##  }
            ##      )
            ##      EMBER_DAYS.extend([easter(year) + week(i+1) + indays(3), easter(year) + week(i+1) + indays(5), easter(year) + week(i+1) + indays(6)])
            ##      i += 1
            ##      prelim_pents = [
            ##      {
            ##      "feast": "Festum Sanctissimæ Trinitatis",
            ##      "rank": [2, "d I cl"],
            ##      "color": "white",
            ##      "mass": {"int": "Benedicta sit", "glo": True, "cre": True, "pre": "de Ssma Trinitate"},
            ##      "matins": {},
            ##      "lauds": {},
            ##      "prime": {},
            ##      "little_hours": {},
            ##      "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##      "compline": {},
            ##      "office_type": "festiva",
            ##      "nobility": False
            ##  },
            ##  {
            ##      "feast": "Dominica infra Oct. Ssmi Corporis Christi (Dominica II post Pentecosten)",
            ##      "rank": [12, "sd"],
            ##      "color": "white",
            ##      "mass": {"int": "Factus est", "glo": True, "seq": "Lauda, Sion, Salvatorem", "cre": True, "pre": "de Nativitate, vel de Ssma Trinitate"},
            ##      "matins": {},
            ##      "lauds": {},
            ##      "prime": {},
            ##      "little_hours": {},
            ##      "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##      "compline": {},
            ##      "office_type": "dominica",
            ##      "nobility": False
            ##  },
            ##  {
            ##      "feast": "Dominica infra Oct. Ssmi Cordis DNJC (Dominica III post Pentecosten)",
            ##      "rank": [12, "sd"],
            ##      "color": "white",
            ##      "mass": {"int": "Respice in me", "glo": True, "cre": True, "pre": "de sacratissimo Code Jesu"},
            ##      "matins": {},
            ##      "lauds": {},
            ##      "prime": {},
            ##      "little_hours": {},
            ##      "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##      "compline": {},
            ##      "office_type": "dominica",
            ##      "nobility": False
            ##  },
            ##                                                                                                                                      ]
            ##  for l, x in enumerate(prelim_pents):
            ##  if x["feast"] == "Dominica infra Oct. Ssmi Corporis Christi (Dominica II post Pentecosten)":
            ##  corpus_christi = pent_date + week(2) - indays(3)
            ##  for j, y in enumerate(ROMANS[1: 7]):
            ##  if (corpus_christi + indays(j+1)) == (pent_date + week(2)):
            ##  pass  # ? necessary?
            ##  else:
            ##  feria_index = int(
            ##  (corpus_christi+indays(j+1)).strftime("%w"))-1
            ##  fer_num = FERIA[feria_index]
            ##  cycle.update(
            ##  {
            ##      str(corpus_christi + indays(j + 1)): {
            ##          "feast": fer_num+" infra Oct. Ssmi Corporis Christi",
            ##          "rank": [9, "sd"],
            ##          "color": "white",
            ##          "mass": {"int": "Factus est", "glo": True, "seq": "Lauda, Sion, Salvatorem", "cre": True, "pre": "de Nativitate"},
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": "feria",
            ##          "nobility": False
            ##      }
            ##  }
            ##  )
            ##  cycle.update(
            ##  {
            ##  str(corpus_christi): {
            ##      "feast": "Sanctissimi Corporis Christi",
            ##      "rank": [2, "d I cl cum Oct privil 2 ord"],
            ##      "color": "white",
            ##      "mass": {"int": "Cibavit eos", "glo": True, "seq": "Lauda, Sion", "cre": True, "pre": "de Nativitate"},
            ##      "matins": {},
            ##      "lauds": {},
            ##      "prime": {},
            ##      "little_hours": {},
            ##      "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##      "compline": {},
            ##      "office_type": "festiva",
            ##      "nobility": False
            ##  },
            ##  str(corpus_christi + week(1)): {
            ##      "feast": "Octava Ssmi Corporis Christi",
            ##      "rank": [4, "dm"],
            ##      "color": "white",
            ##      "mass": {"int": "Cibavit eos", "glo": True, "seq": "Lauda, Sion", "cre": True, "pre": "de Nativitate"},
            ##      "matins": {},
            ##      "lauds": {},
            ##      "prime": {},
            ##      "little_hours": {},
            ##      "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##      "compline": {},
            ##      "office_type": False,
            ##      "nobility": False
            ##  }
            ##                                                                                                                                                  }
            ##  )
            ##  if x["feast"] == "Dominica infra Oct. Ssmi Cordis DNJC (Dominica III post Pentecosten)":
            ##  ssmi_cordis = pent_date + week(3) - indays(2)
            ##  for j, y in enumerate(ROMANS[1: 7]):
            ##  if ssmi_cordis + indays(j + 1) == pent_date + week(3):
            ##  pass
            ##  else:
            ##  feria_index = int(
            ##  (ssmi_cordis + indays(j + 1)).strftime("%w")) - 1
            ##  fer_num = FERIA[feria_index]
            ##  cycle.update(
            ##  {
            ##      str(ssmi_cordis + indays(j + 1)): {
            ##          "feast": fer_num+" infra Oct. Ssmi Cordis DNJC",
            ##          # ? is this supposed to be within a common octave?
            ##          "rank": [18, "sd"],
            ##          "color": "white",
            ##          "mass": {"int": "Respice in me", "glo": True, "cre": True, "pre": "de Ssmo Corde Iesu vel de Ssma Trinitate"},
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": "dominica",
            ##          "nobility": False
            ##      },
            ##  }
            ##      )
            ##      cycle.update(
            ##      {
            ##      str(ssmi_cordis): {
            ##      "feast": "Sacratissimi Cordis Jesu",
            ##      "rank": [2, "d I cl cum Oct privil 3 ord"],
            ##      "color": "white",
            ##      "mass": {"int": "Cogitationes", "glo": True, "cre": True, "pre": "de Ssmo Corde Iesu"},
            ##      "matins": {},
            ##      "lauds": {},
            ##      "prime": {},
            ##      "little_hours": {},
            ##      "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##      "compline": {},
            ##      "office_type": "festiva",
            ##      "nobility": (1, 0, 3, 1, 1, 0),
            ##  },
            ##      str(ssmi_cordis + week(1)): {
            ##          "feast": "Octava Sacratissimi Cordis Jesu",
            ##          "rank": [13, "dm"],
            ##          "color": "white",
            ##          "mass": {"int": "Cogitationes", "glo": True, "cre": True, "pre": "de Ssmo Corde Iesu"},
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": False,
            ##          "nobility": False
            ##      },
            ##  }
            ##      )
            ##      cycle.update({str(pent_date+week(l+1)): x})
            ##      i += 1
            ##      sept_counter = 0
            ##      christmas = datetime.strptime(str(year) + "-12-25", "%Y-%m-%d")
            ##      lastadvent = christmas - findsunday(christmas)
            ##      post_pent_sundays = int((((lastadvent - week(4))-pent_date)/7).days)-1
            ##      post_pent_count = pent_date + week(4)
            ##      epiph_sunday_overflow = ROMANS[6-find_extra_epiphany(
            ##      post_pent_sundays): find_extra_epiphany(post_pent_sundays)+2]
            ##      for count, x in enumerate(ROMANS[3: post_pent_sundays+1], start=1):
            ##      p = count - 1
            ##      if count <= 20:
            ##      cycle.update(
            ##      {
            ##      str(post_pent_count + week(p)): {
            ##      "feast": "Dominica "+x+" post Pentecosten",
            ##      "rank": [12, "sd"],
            ##      "color": "green",
            ##      "mass": {"int": PENTECOST_MASSES[p], "glo": True, "cre": True, "pre": "de Trinitate"},
            ##      "com_1": {"oration": "A cunctis", },
            ##      "com_2": {"oration": "ad libitum", },
            ##      "matins": {},
            ##      "lauds": {},
            ##      "prime": {},
            ##      "little_hours": {},
            ##      "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##      "compline": {},
            ##      "office_type": "dominica",
            ##      "nobility": False
            ##  },
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
            ##          "com_1": {"oration": "A cunctis", },
            ##          "com_2": {"oration": "ad libitum", },
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": "feria",
            ##          "nobility": (8, 2, 6, 13, 3, 0,),
            ##      },
            ##  }
            ##      )
            ##  elif count == 20 and post_pent_sundays == 23:
            ##  cycle.update(  # todo anticipate the 23rd sunday and celebrate the 24th
            ##  {
            ##  str(post_pent_count + week(p)): {
            ##      "feast": "Dominica XXIII et ultima post Pentecosten",
            ##      "rank": [12, "sd"],
            ##      "color": "green",
            ##      "mass": {"int": PENTECOST_MASSES[-1], "glo": True, "cre": True, "pre": "de Trinitate"},
            ##      "com_1": {"oration": "A cunctis", },
            ##      "com_2": {"oration": "ad libitum", },
            ##      "matins": {},
            ##      "lauds": {},
            ##      "prime": {},
            ##      "little_hours": {},
            ##      "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##      "compline": {},
            ##      "office_type": False,
            ##      "nobility": False
            ##  },
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
            ##          "com_1": {"oration": "A cunctis", },
            ##          "com_2": {"oration": "ad libitum", },
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
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
            ##      str(post_pent_count + week(p)): {
            ##          "feast": "Dominica " + x + " et ultima post Pentecosten",
            ##          "rank": [12, "sd"],
            ##          "color": "green",
            ##          "mass": {"int": PENTECOST_MASSES[-1], "glo": True, "cre": True, "pre": "de Trinitate"},
            ##          "com_1": {"oration": "A cunctis", },
            ##          "com_2": {"oration": "ad libitum", },
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": "dominica",
            ##          "nobility": False
            ##      },
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
            ##              "com_1": {"oration": "A cunctis", },
            ##              "com_2": {"oration": "ad libitum", },
            ##              "matins": {},
            ##              "lauds": {},
            ##              "prime": {},
            ##              "little_hours": {},
            ##              "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
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
            ##          str(post_pent_count + week(p+y)): {
            ##              "feast": "Dominica "+ROMANS[p+y+3]+" post Pentecosten, "+x+"Epiphany",
            ##              "rank": [12, "sd"],
            ##              "color": "green",
            ##              "mass": {"int": "Dicit Dominus", "glo": True, "cre": True, "pre": "de Trinitate"},
            ##              "com_1": {"oration": "A cunctis", },
            ##              "com_2": {"oration": "ad libitum", },
            ##              "matins": {},
            ##              "lauds": {},
            ##              "prime": {},
            ##              "little_hours": {},
            ##              "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##              "compline": {},
            ##              "office_type": "dominica",
            ##              "nobility": False
            ##          },
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
            ##                  "com_1": {"oration": "A cunctis", },
            ##                  "com_2": {"oration": "ad libitum", },
            ##                  "matins": {},
            ##                  "lauds": {},
            ##                  "prime": {},
            ##                  "little_hours": {},
            ##                  "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##              "compline": {},
            ##              "office_type": "feria",
            ##              "nobility": (8, 2, 6, 13, 3, 0,),
            ##          },
            ##      }
            ##          )
            ##          if (post_pent_count + week(p)).strftime("%B") == "September":
            ##          if int((post_pent_count + week(p)).strftime("%d")) <= 3:
            ##          sept_counter += 0
            ##          else:
            ##          sept_counter += 1
            ##          if sept_counter == 3:
            ##          cycle.update(
            ##          {

            "Ember_Sept_4": {
                "feast": "Feria IV Quatuor Temporum Septembris",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Exsultate Deo", "glo": False, "cre": False, "pre": "Communis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": False,
                "fasting": True,
            },
            "Ember_Sept_6": {
                "feast": "Feria VI Quatuor Temporum Septembris",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Laetetur cor", "glo": False, "cre": False, "pre": "Communis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": False,
                "fasting": True,
            },
            "Ember_Sept_s": {
                "feast": "Sabbatum Quatuor Temporum Septembris",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Venite, adoremus", "glo": False, "cre": False, "pre": "Communis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": False,
                "fasting": True,
            },

            ##      }
            ##          )
            ##          EMBER_DAYS.extend([post_pent_count + week(p) + indays(3),post_pent_count + week(p) + indays(5), post_pent_count + week(p) + indays(6)])
            ##          if (post_pent_count + week(p)).strftime("%B") == "November" and (post_pent_count + week(p-1)).strftime("%B") == "October":
            ##          # if the current Sunday is in November and the previous Sunday is in October
            ##          christ_king = post_pent_count + week(p) - week(1)
            ##          cycle.update(
            ##          {
            ##          str(christ_king): {
            ##          "feast": "In Festo DNJC Regis",
            ##          "rank": [2, "d I cl"],
            ##          "color": "white",
            ##          "mass": {"int": "Dignus est", "glo": True, "cre": True, "pre": "de DNJC Rege"},
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {},
            ##          "little_hours": {},
            ##          "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": "festiva",
            ##          "nobility": False
            ##      },
            ##  }
            ##      )
            ##      i += 1

            # TODO: is this already taken care of?
            ##      if christmas == lastadvent:  # prevents 4th Sunday of Advent and Christmas occurance
            ##      lastadvent -= week(1)
            ##      advents = [
            ##      "Dominica IV Adventus",
            ##      "Dominica III Adventus",
            ##      "Dominica II Adventus",
            ##      "Dominica I Adventus",
            ##  ]
            ##      for i, x in enumerate(advents):
            ##      for k, y in enumerate(ROMANS[1: 6], start=1):
            ##      cycle.update(
            ##      {
            ##      str(lastadvent - week(i) + indays(k)): {
            ##          "feast": "Feria "+y+" infra Hebd"+x.strip("Dominica"),
            ##          "rank": [19, "feria"],
            ##          "color": "purple",
            ##          "mass": {"int": "Ad te levavi" if x == "Dominica I Adventus" else ("Populus Sion" if x == "Dominica II Adventus" else ("Gaudete" if x == "Dominica III Adventus" else "Rorate cæli")), "glo": False, "cre": False, "pre": "Communis"},
            ##          "com_1": {"oration": "Deus qui de beate"},
            ##          "com_2": {"oration": "Ecclesiæ"},
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {"four_psalms": True, "cap": "Pacem", "v_r": "Qui venturus est in mundum", "preces_feriales": True, },
            ##          "little_hours": {"preces_feriales": True, },
            ##          "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": "feria",
            ##          "nobility": (9, 2, 6, 13, 3, 0),
            ##      },
            ##  }
            ##      )
            ##      else:
            ##      cycle.update(
            ##      {
            ##      str(lastadvent - week(i) + indays(6)): {
            ##          "feast": "Sabbatum infra Hebd"+x.strip("Dominica"),
            ##          "rank": [19, "feria"],
            ##          "color": "purple",
            ##          "mass": {"int": "Ad te levavi" if x == "Dominica I Adventus" else ("Populus Sion" if x == "Dominica II Adventus" else ("Gaudete" if x == "Dominica III Adventus" else "Rorate cæli")), "glo": False, "cre": False, "pre": "Communis"},
            ##          "com_1": {"oration": "Deus qui de beate"},
            ##          "com_2": {"oration": "Ecclesiæ"},
            ##          "matins": {},
            ##          "lauds": {},
            ##          "prime": {"four_psalms": True, "cap": "Pacem", "v_r": "Qui venturus est in mundum", "preces_feriales": True, },
            ##          "little_hours": {"preces_feriales": True, },
            ##          "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##          "compline": {},
            ##          "office_type": "feria",
            ##          "nobility": (9, 2, 6, 13, 3, 0),
            ##      },
            ##  }
            ##      )
            ##      if x == "Dominica III Adventus":
            ##      cycle.update(
            ##      {
            ##      str(lastadvent - week(i)): {
            ##      "feast": x,
            ##      "rank": [8, "sd II cl"],
            ##      "color": "purple",
            ##      "mass": {"int": "Populus Sion" if x == "Dominica II Adventus" else ("Gaudete" if x == "Dominica III Adventus" else "Rorate cæli"), "glo": False, "cre": True, "pre": "de Trinitate"},
            ##      "com_1": {"oration": "Deus qui de beate"},
            ##      "com_2": {"oration": "Ecclesiæ"},
            ##      "matins": {},
            ##      "lauds": {},
            ##      "prime": {},
            ##      "little_hours": {},
            ##      "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
            ##      "compline": {},
            ##      "office_type": "dominica",
            ##      "nobility": False
            ##  },


            # Ember Days of Advent
            "Ember_Advent_4": {
                "feast": "Feria IV Quatuor Temporum in Adventus",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Rorate cæli", "glo": False, "cre": False, "pre": "Communis"},
                "com_1": {"oration": "Deus qui de beate"},
                "com_2": {"oration": "Ecclesiæ"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (9, 2, 6, 13, 3, 0),
                "fasting": True,
            },
            "Ember_Advent_6": {
                "feast": "Feria VI Quatuor Temporum in Adventus",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Prope es tu", "glo": False, "cre": False, "pre": "Communis"},
                "com_1": {"oration": "Deus qui de beate"},
                "com_2": {"oration": "Ecclesiæ"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (9, 2, 6, 13, 3, 0),
                "fasting": True,
            },
            "Ember_Advent_s": {
                "feast": "Sabbatum Quatuor Temporum in Adventus",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Veni, et ostende", "glo": False, "cre": False, "pre": "Communis"},
                "com_1": {"oration": "Deus qui de beate"},
                "com_2": {"oration": "Ecclesiæ"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (9, 2, 6, 13, 3, 0),
                "fasting": True,
            },

            ##  }
            ##      )
            ##      EMBER_DAYS.extend([lastadvent - week(i) + indays(4), lastadvent - week(i) + indays(5), lastadvent - week(i) + indays(6)])
            ##      elif x == "Dominica I Adventus":
            ##      cycle.update(
            ##      {


            ##                                                                                                                                                                                                                          }
            ##  )
            ##  else:
            ##  cycle.update(
            ##  {

            # Advents
            "D_Advent_1": {
                "feast": "Dominica I Adventus",
                "rank": [1, "sd"],
                "color": "purple",
                "mass": {"int": "Ad te levavi", "glo": False, "cre": True, "pre": "de Trinitate"},
                "com_1": {"oration": "Deus qui de beate"},
                "com_2": {"oration": "Ecclesiæ"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": False,
                "fasting": False,
            },
            "D_Advent_2": {
                "feast": "Dominica II Adventus",
                "rank": [8, "sd II cl"],
                "color": "purple",
                "mass": {"int": "Populus Sion", "glo": False, "cre": True, "pre": "de Trinitate"},
                "com_1": {"oration": "Deus qui de beate"},
                "com_2": {"oration": "Ecclesiæ"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": False,
                "fasting": False,
            },
            "D_Advent_3": {
                "feast": "Dominica III Adventus",
                "rank": [8, "sd II cl"],
                "color": "pink",
                "mass": {"int": "Gaudete", "glo": False, "cre": True, "pre": "de Trinitate"},
                "com_1": {"oration": "Deus qui de beate"},
                "com_2": {"oration": "Ecclesiæ"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": False,
                "fasting": False,
            },
            "D_Advent_4": {
                "feast": "Dominica IV Adventus",
                "rank": [8, "sd II cl"],
                "color": "purple",
                "mass": {"int": "Rorate cæli", "glo": False, "cre": True, "pre": "de Trinitate"},
                "com_1": {"oration": "Deus qui de beate"},
                "com_2": {"oration": "Ecclesiæ"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": False,
                "fasting": False,
            },

            "V_Christmas": {
                "feast": "Vigilia Nativitas DNJC",
                "rank": [3, "d I cl Vig privil I cl"],
                "color": "purple",
                "mass": {"int": "Hodie scietis", "glo": False, "cre": False, "pre": "Communis"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": False,
                "fasting": True,
            },
            "DV_Christmas": {
                "feast": "Vigilia Nativitas DNJC",
                "rank": [3, "d I cl Vig privil I cl"],
                "color": "purple",
                # TODO: add commemoration of the fourth Sunday of Advent
                "mass": {"int": "Hodie scietis", "glo": False, "cre": True, "pre": "de Trinitate"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": False,
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
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {"sunday": True,},
                "office_type": "festiva",
                "nobility": False,
                "fasting": False,
            },

            ##  if findsunday(christmas) == 0 or 1 or 2 or 3:
            ##  # Dominica infra respsita on 30 if Sunday falls on 25, 26, 27 or 28


            "D_Christmas_r": {
                "feast": "Dominica Infra Octavam Nativitatis reposita",
                "rank": [12, "sd"],
                "color": "white",
                "mass": {"int": "Dum medium silentium", "glo": True, "cre": True, "pre": "de Comm de Nativitate"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": False,
                "fasting": False,
            },
            "D_Christmas": {
                "feast": "Dominica Infra Octavam Nativitatis",
                "rank": [12, "sd"],
                "color": "white",
                "mass": {"int": "Dum medium", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": False,
                "fasting": False,
            },

            ##  }
            ##      )
            ##      if (
            ##      int(day(year, 12, 30).strftime("%u")) == 1
            ##      or int(day(year, 12, 30).strftime("%u")) == 7
            ##      ):

            "8_Chritmas_f6": {
                "feast": "Feria VI infra Octavam Nativitatis",
                "rank": [16, "sd"],
                "color": "white",
                "mass": {"int": "Puer natus est nobis", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""}, "office_type": "feria",
                "compline": {},
                "nobility": False,
                "fasting": False,
            },
            "StStephan": {
                "feast": "S. Stephani Protomartyris",
                "rank": [10, "d II cl cum Oct simplici"],
                "color": "red",
                "mass": {"int": "Sederunt", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": False,
                "fasting": False,
            },
            "StJohn": {
                "feast": "S. Joannis Ap Ev",
                "rank": [10, "d II cl cum Oct simplici"],
                "color": "red",
                "mass": {"int": "In medio ecclesiæ", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": False,
                "fasting": False,
            },
            "StsInnocents": {
                "feast": "Ss Innocentium Mm",
                "rank": [10, "d II cl cum Oct simplici"],
                "color": "purple",
                "mass": {"int": "Ex ore infantium", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": False,
                "fasting": False,
            },
            "StThomas": {
                "feast": "S. Thomæ EM",
                "rank": [15, "d"],
                "color": "red",
                "mass": {"int": "Gaudeamus omnes", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": False,
                "fasting": False,
            },
            "StSylvester": {
                "feast": "S. Silvestri I PC",
                "rank": [15, "d"],
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": False, "cre": True, "pre": "et Comm de Nativitate"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": False,
                "fasting": False,
            },
            # TODO: add the Sundays if the fall on St. Thomas or St. Sylvester
        }

        self.data = self.easy_data | self.lent_sundays() | self.ascension_ferias()

    def lent_sundays(self) -> dict:
        normal_lents = [f"D_Lent_{l+1}" for l in range(4)]
        later_lents = ["D_Passion_5", "D_Palm_6"]
        lents = [*normal_lents, *later_lents]
        return {
            date: {
                "feast": f"Dominica infra Hebd {integer_to_roman(x+1)} in Quadragesima",
                "rank": [19, "sd I cl"],
                "color": "purple",
                "mass": {
                    "int": "", # TODO: add all of the Lent Sunday Introits
                    "glo": False,
                    "cre": False,
                    "pre": "de Quadragesima" if x < 6 else "de Cruce",
                },
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            } for x, date in enumerate(lents)
        }

    def ascension_ferias(self) -> dict:
        ferias = []
        return { # NOTE: there are duplicates, but does it matter?
            f"in_8_Ascension_{date}": {
                "feast": f"De {integer_to_roman(date)} die infra Oct. Ascensionis",
                "rank": [16, "sd"],
                "color": "white",
                "mass": {"int": "Viri galilæi", "glo": True, "cre": False, "pre": "de Ascensione"},
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": {"firstVespers": "", "secondVespers": ""}, "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": False,
                "fasting": False,
            } for date in range(1,8)
        }
