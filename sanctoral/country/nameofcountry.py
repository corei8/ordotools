#
# ! the name of this dictionary is *country* -- DO NOT ALTER
# not necessarily a country, but a region of
# All the propers of a country are contined here.
# Rename this file to the name of the country. No capitals, no spaces, only alphabet.

country_name = '' # enter the latin name of the country as it will appear in the Ordo

country = {
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
