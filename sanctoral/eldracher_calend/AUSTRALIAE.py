#
# ! the name of this dictionary is *country* -- DO NOT ALTER
# not necessarily a country, but a region of
# All the propers of a country are contained here.
# Rename this file to the name of the country. No capitals, no spaces, only alphabet.

country_name = 'Australiae' # enter the latin name of the country as it will appear in the Ordo

country = {
    '03/17': { #This feast has a Common Octave if it is transferred outside of Lent, which happens if Easter is between March 22 and March 24.
        'feast': 'S. Patritii E.C. Patroni Hiberniae',
        # according to the accompanying charts -- only 4 digits for now, plus nominal rank
        'rank': [0, 4, 1, 1, 'DICL'],
              "com": []
              'office_proper': False,  # else, false
              # 'Omnia de Communi Conf. Pont. praeter sequentia.
              # Oratio ut in Brevario.
              # In I Nocturno Lectiones Fidelis sermo, de eodem Communi I loco.
              # In II et III Nocturno Lectiones ut in Breviario.
              # IX Lectio de Homilia Feriae, et fit ejus Com. ad Laudes.
              # In II Vesperis Com. sequentis et Feriae.'
              # for a proper Comm: 'et Comm de *preface*'
        'mass': {
            'int': 'Statuit',
            'glo': True,
            'cre': False,  # exception where St. Patrick Principal Patron of Diocese, Titular of Cathedral, or where Indult granted
            'pre': 'Communis'
        },
        # in Vespers 'propers' is for exceptions to a common office (e.g. St Teresa's hymn)
        'vespers': {
            'proper': False,
            'admag': 'Sacerdos et Pontifex', 'Amavit eum Dominus', #How to notate different antiphons at First and Second Vespers? Both from Common in this case.
            'propers': {
                'hymn': '',
                'verse': ''
            },
            'oration': 'Deus, qui ad praedicandam'
        },
    },
}
