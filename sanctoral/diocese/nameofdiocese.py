#
# ! the name of this dictionary is *diocese* -- DO NOT ALTER
# 'diocese' in this case is not strictly a diocese, but can be a country w/in a region
# All the propers of a diocese are contined here.
# Rename this file to the name of the diocese. No capitals, no spaces, only alphabet.

diocese_name = ''  # enter the latin name of the diocese as it will appear in the Ordo

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
        # for a proper Comm: 'et Comm de *preface*'
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
