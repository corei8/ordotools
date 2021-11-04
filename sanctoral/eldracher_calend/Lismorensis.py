#
# ! the name of this dictionary is *diocese* -- DO NOT ALTER
# 'diocese' in this case is not strictly a diocese, but can be a country w/in a region
# All the propers of a diocese are contined here.
# Rename this file to the name of the diocese. No capitals, no spaces, only alphabet.

diocese_name = 'D. Lismoren.'  # cf. Ordo 1954; Bathurst is a diocese within the Province of Melbourne

diocese = { # ! If the feast is transferred out of Lent, then it has a common octave, otherwise not
    '03/17': {
        'feast': 'S. Patritii E.C. Patroni Hiberniae',
        # according to the accompanying charts -- only 4 digits for now, plus nominal rank
        'rank': [0, 4, 1, 1, 'DICL'],
        # commemoration
        'comm2': {#Feast is expected to always fall within Lent
            'Feast': {
                'mass': {
                    'int': '',
                    'glo': True, 'cre': True,
                    'pre': '' #could be either of Lent or of Passiontide
                }
            }
        },
        'comm3': '',  # blank if no commemoration
        'office_proper': True,  # else, false
        #'Omnia de Communi Conf. Pont. praeter sequentia.
        #Oratio ut in Brevario.
        #In I Nocturno Lectiones Fidelis sermo, de eodem Communi I loco.
        #In II et III Nocturno Lectiones ut in Breviario.
        #IX Lectio de Homilia Feriae, et fit ejus Com. ad Laudes.
        #In II Vesperis Com. sequentis et Feriae.'
        # for a proper Communicantes: 'et Communicantes de *preface*'
        'mass': {
            'int': 'Egredere', #The Gospel of this Mass is read both at Mass and Matins, with the III Nocturne Breviary Lessons altered accordingly.
            'glo': True,
            'cre': True, #Principal Patron of the Diocese
            'pre': 'Communis'
        },
        # in Vespers 'propers' is for exceptions to a common office (e.g. St Teresa's hymn)
        'vespers': {
            'proper': False,
            'admag': 'Sacerdos et Pontifex', 'Amavit eum Dominus' #How to notate different antiphons at First and Second Vespers? Both from Common in this case.
            'propers': {
                'hymn': '',
                'verse': ''
            },
            'oration': 'Deus, qui ad praedicandam'
        },
    },
}


diocese = { # ! note here if the feast has an octave, and which class of octave, otherwise remove.
    'dd/mm': {
        'feast': 'Feast',
        # according to the accompanying charts -- only 4 digits for now, plus nominal rank
        'rank': [4, 9, 6, 5, 'd'],
        # commemoration
        'comm2': {
            'Feast': {
                'mass': {
                    'int': 'Introit',
                    'glo': True, 'cre': True,
                    'pre': 'Communis'
                }
            }
        },
        'comm3': '',  # blank if no commemoration
        'office_proper': True,  # else, false
        # for a proper Communicantes: 'et Communicantes de *preface*'
        'mass': {
            'int': 'Introit',
            'glo': True,
            'cre': True,
            'pre': 'Communis'
        },
        # in Vespers 'propers' is for exceptions to a common office (e.g. St Teresa's hymn)
        'vespers': {
            'proper': False,
            'admag': 'MagnificatAnt',
            'propers': {
                'hymn': '',
                'verse': ''
            },
            'oration': 'Oration'
        },
    },
}
