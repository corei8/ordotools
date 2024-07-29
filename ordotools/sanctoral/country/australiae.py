from ordotools.tools.helpers import day


class Country:

    def __init__(self, year):
        self.name = "Australiae"
        self.year = year
        self.data = {
            day(year=self.year, month=3, day=17): {
                "feast": "S. Patritii E.C. Patroni Hiberniae",
                "rank": [5, "d I cl"],  # check the ranking
                "nobility": (False,),
                "com": [],
                "office_type": False,
                "color": "white",
                "mass": {"int": "Statuit", "glo": True, "cre": False, "pre": "Communis"},
                "matins": {
                    "L1": "",
                    "L2": "",
                    "L3": "",
                    "L4": "",
                    "L5": "",
                    "L6": "",
                    "L7": "",
                    "L8": "",
                    "L9": "",
                },
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ("Sacerdos et Pontifex", "Amavit eum Dominus"), "propers": { "hymn": "", "verse": "" }, "oration": "Deus, qui ad praedicandam"},
                "compline": {},
            }
        }


# NOTE:
# 'Omnia de Communi Conf. Pont. praeter sequentia.
# Oratio ut in Brevario.
# In I Nocturno Lectiones Fidelis sermo, de eodem Communi I loco.
# In II et III Nocturno Lectiones ut in Breviario.
# IX Lectio de Homilia Feriae, et fit ejus Com. ad Laudes.
# In II Vesperis Com. sequentis et Feriae.'
