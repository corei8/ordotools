from datetime import datetime
from ordo_tools.settings import YEAR


class Feast:
    def __init__(self, feast_date: str, properties: dict):
        self.feast_date = feast_date
        try:
            self.feast_date_datetime = datetime.strptime(
                feast_date.strip('.'), '%m/%d')
        except ValueError:
            self.feast_date_datetime = datetime.strptime(
                feast_date.strip('.'), '%m%d')
        self.feast_properties = properties
        self.name = properties['feast']
        if 'infra_octave_name' in properties.keys():
            self.infra_octave_name = properties['infra_octave_name']
        self.rank_v = properties['rank'][-1]  # verbose rank
        self.rank_n = properties['rank'][0]   # numeric rank
        self.color = properties['color']
        self.mass = {}
        if 'int' in properties['mass'].keys():
            self.mass = {'Ad Missam': properties['mass']}
        else:
            for x, y in properties['mass'].items():
                self.mass.update({x: y})
        self.nobility = properties['nobility'] if 'nobility' in properties.keys(
        ) else ('0', '0', '0', '0', '0', '0', )
        self.office_type = properties['office_type']
        self.coms = {
            'com_1': properties['com_1'] if 'com_1' in properties.keys() else '',
            'com_2': properties['com_2'] if 'com_2' in properties.keys() else '',
            'com_3': properties['com_3'] if 'com_3' in properties.keys() else '',
            'com_4': properties['com_4'] if 'com_4' in properties.keys() else '',
            'com_5': properties['com_5'] if 'com_5' in properties.keys() else '',
        }
        # parts of the office:
        self.matins = properties['matins'] if 'matins' in properties.keys() else {
        }
        self.lauds = properties['lauds'] if 'lauds' in properties.keys() else {
        }
        self.prime = properties['prime'] if 'prime' in properties.keys() else {
        }
        self.little_hours = properties['little_hours'] if 'little_hours' in properties.keys() else {
        }
        self.vespers = properties['vespers'] if 'vespers' in properties.keys() else {
        }
        self.compline = properties['compline'] if 'compline' in properties.keys() else {
        }

    @ property
    def feast_date_display(self) -> str:
        """ Displays the feast date for the ordo """
        return datetime.strptime(self.feast_date.strip('tranlsated ._')+'/'+str(YEAR), '%m/%d/%Y').strftime('%d')

    def date(self):
        # ? is this used?
        return datetime.strptime('%m%d', self.feast_date)

    @ property
    # todo #9 expand Preces method to provide for 1. Preces Feriales 2. Compline 3. Little Hours
    def preces(self) -> str:
        if self.rank_n <= 16:
            return ''
        else:
            return 'Preces'

    @ property
    def feast(self) -> str:
        return self.feast_properties['feast']

    @ property
    def updated_properties(self) -> dict:
        """ Updates all values of the feast's dictionary """
        dic = {
            'feast': self.name,
            'rank': [self.rank_n, self.rank_v],
            'color': self.color,
            'mass': self.mass,
            'matins': {},
            'lauds': {},
            'prime': {},
            'little_hours': {},
            'vespers': self.vespers,
            'compline': {},
            'nobility': self.nobility,
            'office_type': self.office_type,
            'com_1': self.coms['com_1'],
            'com_2': self.coms['com_2'],
            'com_3': self.coms['com_3'],
            'com_4': self.coms['com_4'],
            'com_5': self.coms['com_5'],
        }
        return dic

    @ property
    def office_type2latex(self) -> str:
        """ returns formatted office type based on office_type key """
        # todo write all office types in english
        if self.office_type == False:
            off_type = 'Ord, '
        elif self.office_type == 'feria':
            off_type = 'Fer, '
        elif self.office_type == 'festiva':
            off_type = 'Festiv, '
        elif self.office_type == 'dominica':
            off_type = 'Dom, '
        elif self.office_type == 'ut in pr loco':
            off_type = 'ut in pr loco, '
        else:
            return 'ERROR!'
        return 'Off ' + off_type

    @ property
    def com_in_title(self) -> str:
        """ returns formatted commemorations in title """
        results = ''
        for x in self.coms.values():
            if type(x) == dict:
                if 'feast' in x.keys():
                    results += r'\textit{['+x['feast'] + r']} \\ '
                else:
                    results += ''
            else:
                results += ''
        return results

    def introit(self) -> list:
        """ Finds the Introit text for the feast """
        # todo add a methed to determine if it is a three Mass Introit or not.
        introit_list = []
        if len(self.mass.items()) == 1:
            if 'Ad Missam' in self.mass.keys():
                if type(self.mass['Ad Missam']['int']) == str:
                    introit_list.append(self.mass['Ad Missam']['int'])
                else:
                    # todo add a method to determine whether it is still pascahltime or not
                    # ! just for testing purposes
                    introit_list.append(self.mass['Ad Missam']['int'][0])
            else:
                pass
        else:
            for y in self.mass.keys():
                introit_list.append(self.mass[y]['int'])
        return introit_list

    @ property
    def translate_color(self) -> str:
        """ translate the color from english to latin """
        translations = {
            'white': 'albus',
            'green': 'viridis',
            'red': 'ruber',
            'violet': 'violaceus',
            'black': 'niger',
            'color': 'void',
        }
        latin_color = translations[self.color]
        return latin_color

    @ property
    def translate_weekday(self) -> str:
        """ translate the weekday from english to latin """
        translations = {
            'Sunday': 'Dom',
            'Monday': 'Fer II',
            'Tuesday': 'Fer III',
            'Wednesday': 'Fer IV',
            'Thursday': 'Fer V',
            'Friday': 'Fer VI',
            'Saturday': 'Sabb',
        }
        latin_weekday = translations[datetime.strptime(self.feast_date.strip(
            'tranlsated ._')+'/'+str(YEAR), '%m/%d/%Y').strftime('%A')]
        return latin_weekday

    def mass_commemorations(self) -> str:
        """ returns formatted and ordered mass commemorations in title """
        results = ''
        i = 2
        for x in self.coms.keys():
            if type(self.coms[x]) == dict:
                if 'feast' in self.coms[x].keys():
                    results += str(i) + r' or ' + self.coms[x]['feast'] + r', '
                    i += 1
                elif 'oration' in self.coms[x].keys():
                    if self.coms[x]['oration'] == 'ad libitum':
                        results += str(i) + r' or ' + \
                            self.coms[x]['oration'] + r', '
                    else:
                        results += str(i) + \
                            r' or \textit{' + self.coms[x]['oration'] + r',} '
                    i += 1
                else:
                    pass
            else:
                pass
        return results

    def display_mass_as_latex(self) -> str:
        """ return the Mass as LaTeX code """
        # todo add orations
        latexed_mass = ''
        pprlast = ''
        status = []
        for y in self.mass.values():
            gloria = y['glo']
            creed = y['cre']
            if gloria == True and creed == True:
                status.append('G, C, ')
            elif gloria == True and creed == False:
                status.append('G, ')
            elif gloria == False and creed == True:
                status.append('C, ')
            else:
                status.append('')
        i = 0
        #! refine this to work only for its proper Mass:
        if 'proper_last_gospel' in y.keys():
            pprlast = 'ult Evgl ' + y['proper_last_gospel'] + ', '
        else:
            pprlast = ''
        for x, y in self.mass.items():
            # todo use the second in the string if it is Paschaltime.
            latexed_mass += '\\textbf{'+x+'}: \\textit{' + \
                self.introit()[i] + ',} ' + \
                status[i]+'Pre '+y['pre'] + ', ' + \
                self.mass_commemorations() + ' ' + pprlast + ' '
            i += 1
        return latexed_mass

    @ property
    def display_matins_as_latex(self) -> str:
        """ return Matins as LaTeX code """
        if len(self.matins) == 0:
            return ''
        else:
            latexed_matins = r'\textbf{Ad Mat}: '
            return ''

    @ property
    def display_lauds_as_latex(self) -> str:
        """ return Laudes as LaTeX code """
        if len(self.lauds) == 0:
            return ''
        else:
            latexed_lauds = r'\textbf{Ad Lau}: '
            for k in self.lauds.keys():
                if k == 'psalms':
                    # * make this a bit easier to work with
                    if self.lauds[k] == 'sunday':
                        latexed_lauds += 'Pss de Dom, '
                    else:
                        pass
            return latexed_lauds

    @ property
    def display_little_hours_as_latex(self) -> str:
        """ return the little hours as LaTeX code """
        if len(self.little_hours) == 0:
            return ''
        else:
            latexed_little_hours = r'\textbf{Ad Horas}: '
            for k in self.little_hours.keys():
                if k == 'preces_feriales':
                    if self.prime[k] == True:
                        latexed_little_hours += 'Preces feriales, '
                    else:
                        pass
                elif k == 'psalms':
                    if self.little_hours[k] == 'sunday':
                        latexed_little_hours += 'Pss de Dom, '
                else:
                    pass
            return latexed_little_hours

    @ property
    def display_prime_as_latex(self) -> str:
        """ return Prime as LaTeX code """
        if len(self.prime) == 0:
            return ''
        else:
            latexed_prime = r'\textbf{Ad Primam}: '
            for k in self.prime.keys():
                if k == 'four_psalms':
                    if self.prime[k] == True:
                        latexed_prime += r'4 Pss, '
                    else:
                        pass
                elif k == 'cap':
                    latexed_prime += r'\textit{' + f'{self.prime[k]},' + '} '
                elif k == 'v_r':
                    latexed_prime += r'\Vbar\ in \Rbar\ brev: ' + \
                        r'\textit{' + f'{self.prime[k]},' + '} '
                elif k == 'preces_feriales':
                    if self.prime[k] == True:
                        latexed_prime += 'Preces feriales, '
                    else:
                        pass
                else:
                    pass
            return latexed_prime

    @ property
    def display_vespers_as_latex(self) -> str:
        """ return vespers as LaTeX code """
        if len(self.vespers) == 0:
            return ''
        else:
            latexed_vespers = r'\textbf{In Vesp}: '
            return ''

    @ property
    def display_compline_as_latex(self) -> str:
        """ return compline as LaTeX code """
        if len(self.compline) == 0:
            return ''
        else:
            latexed_compline = r'\textbf{Ad Compl}: '
            for k in self.compline.keys():
                if k == 'sunday':
                    if self.compline[k] == True:
                        # * do something fancy with the period -- no trailing commas!!
                        latexed_compline += 'Pss de Dom. '
                    else:
                        pass
                else:
                    pass
            return latexed_compline
