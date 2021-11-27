from datetime import datetime
from ordo_tools.settings import YEAR

class Feast:
    def __init__(self, feast_date: str, properties: dict):
        self.feast_date = feast_date
        self.feast_date_display = datetime.strptime(self.feast_date.strip(
            'tranlsated ._')+'/'+str(YEAR), '%m/%d/%Y').strftime('%d')
        self.feast_properties = properties
        self.name = properties['feast']
        print(self.name)
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
        self.vespers = properties['vespers'] if 'vespers' in properties.keys(
        ) else {'proper': False, 'admag': '', 'propers': {}, 'oration': ''}
        self.nobility = properties['nobility'] if 'nobility' in properties.keys(
        ) else ('0', '0', '0', '0', '0', '0', )
        self.office_type = properties['office_type']
        self.com_1 = {'oration': ''}
        self.com_2 = {'oration': ''}
        self.com_3 = {'oration': ''}
        self.com_4 = {'oration': ''}
        self.com_5 = {'oration': ''}
        self_coms = [self.com_1, self.com_2,
                     self.com_3, self.com_4, self.com_5]
        coms = ('com_1', 'com_2', 'com_3', 'com_4', 'com_5')
        for i, com in enumerate(coms):
            try:
                if properties[com]:
                    self_coms[i] = self.Commemoration(
                        properties[com]) if com in properties.keys() else None
                    print('assigning ' + com + ' to ' + str(self_coms[i]))
            except KeyError:
                pass

    class Commemoration:
        def __init__(self, detail: dict):
            self.details = detail
            self.com_mass = detail['mass'] if 'mass' in detail.keys() else None
            self.com_name = detail['feast'] if 'feast' in detail.keys(
            ) else detail['oration']

        def com_feast_inline(self) -> str:
            """ display the commemoration as an oration """
            # todo write a method that lables the commemorations with numbers
            try:
                if 'feast' in self.details.keys():
                    return r'\normaltext{' + self.details['feast'] + '}'
                else:
                    return r'\textit{' + self.details['oration'] + '}'
            except KeyError:
                return ''

    def date(self):
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
        dic = {
            'feast': self.name,
            'rank': [self.rank_n, self.rank_v],
            'color': self.color,
            'mass': self.mass,
            'vespers': self.vespers,
            'nobility': self.nobility,
            'office_type': self.office_type,
            'com_1': self.com_1.details if self.com_1 else '',
            'com_2': self.com_2.details if self.com_2 else '',
            'com_3': self.com_3.details if self.com_3 else '',
            'com_4': self.com_4.details if self.com_4 else '',
            'com_5': self.com_5.details if self.com_5 else '',
        }
        return dic

    @ property
    def office_type2latex(self) -> str:
        """ returns formatted office type based on office_type key """
        if self.office_type == False:
            off_type = 'Ord'
        elif self.office_type == 'feria':
            off_type = 'Fer'
        elif self.office_type == 'festiva':
            off_type = 'Festiv'
        elif self.office_type == 'dominica':
            off_type = 'Dom'
        else:
            return 'ERROR!'
        return 'Off ' + off_type

    def introit(self) -> list:
        """Find the introit text for the feast

        Returns:
            str: Introit text
        """
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
            'color': '????',
        }
        latin_color = translations[self.color]
        return latin_color

    # add the commemorations to display_mass_as_latex
    def commemorations_as_latex(self) -> str:
        """ returns the commemorations as latex """
        coms = (self.com_1, self.com_2, self.com_3, self.com_4, self.com_5)
        oration = ''
        for i, com in enumerate(coms):
            try:
                oration += str(i)+' or '+com.com_name + ', '
            except KeyError:
                pass
        return oration

    def display_mass_as_latex(self) -> str:
        """ return the Mass as LaTeX code """
        # todo add orations
        latexed_mass = ''
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
        for x, y in self.mass.items():
            # todo use the second in the string if it is Paschaltime.
            latexed_mass += '\\textbf{'+x+'}: \\textit{' + \
                self.introit()[i] + ',} ' + \
                status[i]+'Pre '+y['pre'] + ', ' + \
                self.commemorations_as_latex()
            i += 1
        return latexed_mass

    def commemoration2latex(self):
        """ return the commemorations as LaTeX code """
        com_list = '\n'
        if self.com_1 != False:
            com_list += self.com_1
        elif self.com_2 != False:
            com_list += self.com_2
        elif self.com_3 != False:
            com_list += self.com_3
        elif self.com_4 != False:
            com_list += self.com_4
        elif self.com_5 != False:
            com_list += self.com_5
        else:
            return com_list + '\n\\textit{No Commemoration}'
        return com_list
