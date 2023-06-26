from datetime import datetime

from ordo_tools.helpers import days
from ordo_tools.helpers import advance_a_day
from ordo_tools.helpers import leap_year

from ordo_tools.feast import Feast
from ordo_tools.temporal import Temporal
from sanctoral.diocese.roman import Sanctoral

import importlib

from ordo_tools.parts import ROMANS


class LiturgicalCalendar:

    def __init__(self, year, diocese, country=''):
        self.year = year
        self.diocese = diocese
        self.transfers = {}

    def update_calendar(self, data: dict) -> dict:
        """
        Updates the calendar file
        """
        cal = {}
        for x, y in data.items():
            cal.update({x: y})
        with open('calen/calendar_' + str(self.year) + '.py', 'a') as f:
            f.truncate(0)
            f.write('from ordo_tools.helpers import day\n\n')
            f.write("class LiturgicalCalendar:\n\n")
            f.write("\tdef __init__(self):\n")
            f.write('\t\tself.data = {\n')
            for i, line in enumerate(sorted(cal)):
                date = f"""\t\t\tday(year={self.year},\
                month={line.strftime('%m').lstrip('0')},\
                day={line.strftime('%d').lstrip('0')})"""
                if i != 0:
                    f.write(f"{date}: {cal[line]},\n")
                else:
                    f.write(f"{date}: {cal[line]},\n")
            f.write('\t\t}\n\n')
            f.write('\t\tdef data(self) -> dict:\n')
            f.write('\t\t\treturn self.data')
        return None

    def commit_to_dictionary(self, target_file: str, dic: dict) -> None:
        """
        Takes a dictionary and writes it to a file.
        """

        self.update_calendar(data=dic)
        return dic

    def explode_octaves(self, region_diocese: str) -> dict:
        # TODO: reimplement this to have a seperate dictionary for these
        """ Takes the Octaves in the Sanctoral cycle and explodes them into
        their days within the octave."""
        mdl = importlib.import_module(
            'sanctoral.diocese.' + region_diocese).sanctoral
        return_dict = {}
        for x in sorted(mdl):
            feast = Feast(x, mdl[x])
            if 'Oct' in feast.rank_v:
                if feast.nobility[2] == 4:  # common octave
                    # todo update this to handle every octave type
                    # * this is an ok use of ROMANS
                    for k, y in enumerate(ROMANS[3:6], start=1):
                        feast.name = 'De ' + y + ' die infra '
                        + feast.infra_octave_name
                        feast.rank_v = 'feria'
                        feast.rank_n = 18
                        return_dict.update(
                            {
                                str((datetime.strptime(
                                    feast.feast_date, '%m/%d'
                                ) + days(k)).strftime('%m/%d')) + '_':
                                feast.updated_properties
                            }
                        )
            else:
                return_dict.update({feast.feast_date: feast.feast_properties})
        return return_dict

    def add_commemoration(self, feast: Feast, commemoration: Feast) -> dict:
        """
        Adds one feast as the commemoration of another feast.
        Accepts feast properties.
        """
        feast.com.insert(0, commemoration.feast_properties)
        return feast.updated_properties

    def rank_by_nobility(self, feast_1: Feast, feast_2: Feast) -> dict:
        """
        Takes two feasts and returns the one with the higher rank.
        """
        alpha, bravo = feast_1.nobility, feast_2.nobility
        for x in range(6):
            if alpha[x] < bravo[x]:
                return {'higher': feast_1, 'lower': feast_2}
            elif alpha[x] > bravo[x]:
                return {'higher': feast_2, 'lower': feast_1}
            else:
                pass
        return {'higher': feast_1, 'lower': feast_2}

    def rank(
        self, date: str, sanctoral_feast: dict, temporal_feast: dict
    ) -> dict:
        """
        Ranks feasts that occur on the same date. Send feasts that can be
        transferred to the transfer dictionary.
        """
        ranked_feasts = {}
        transfers = {}
        sanct = Feast(date, sanctoral_feast)
        tempo = Feast(date, temporal_feast)
        # TODO: refactor
        if sanct.rank_n == tempo.rank_n:
            ranked_feasts |= {
                date:
                self.rank_by_nobility(sanct, tempo)['higher'].feast_properties,
            }
        else:
            candidates = {
                sanct.rank_n: sanct,
                tempo.rank_n: tempo,
            }
            higher = candidates[sorted(candidates)[0]]
            lower = candidates[sorted(candidates)[1]]
            if lower == 22:         # take care of simple feasts
                pass
            if higher.rank_n <= 4:  # feasts that exclude commemorations
                if lower.rank_n <= 10:
                    ranked_feasts.update({date: higher.feast_properties})
                    transfers |= {date: lower.feast_properties}
                else:
                    ranked_feasts.update({date: higher.feast_properties})
            elif 14 <= lower.rank_n <= 16:     # impeded dm, d and sd
                if higher.rank_n == 12 or 19:  # see p. 309 Matters Liturgical
                    ranked_feasts |= {
                        date: self.add_commemoration(
                            feast=higher,
                            commemoration=lower
                        )
                    }
                else:
                    ranked_feasts |= {
                        date: self.add_commemoration(
                            feast=higher,
                            commemoration=lower
                        )
                    }
            else:
                ranked_feasts |= {
                    date: self.add_commemoration(
                        feast=higher,
                        commemoration=lower
                    )
                }
        return ranked_feasts

    def add_sanctoral_feasts(self, temporal: dict, sanctoral: dict) -> dict:
        """
        Adds the sanctoral feasts to the temporal feast dictionary;
        Sends the feasts that confilict to the ranking function.
        """
        calendar = temporal.copy()
        for the_date in sanctoral.keys():
            if the_date in calendar.keys():
                ranked_feast = self.rank(
                    date=the_date,
                    sanctoral_feast=sanctoral[the_date],
                    temporal_feast=calendar[the_date]
                )
                calendar |= ranked_feast
            else:
                calendar |= {the_date: sanctoral[the_date]}
        return calendar

    def transfer_feasts(self, dic: dict) -> dict:
        """ Solves the transfer feast problem. """
        for x in self.transfers.keys():
            trans_feast = Feast(x, self.transfers[x])
            target_date = advance_a_day(trans_feast.date)
            if target_date not in dic.keys():
                dic.update(target_date, trans_feast.feast_properties)
            else:
                pass
        return dic

    def build(self) -> None:
        """ Stitches the temporal and sanctoral calendars together. """
        temporal = Temporal(self.year).return_temporal()
        saints = Sanctoral(self.year)
        if self.diocese == 'roman':
            sanctoral = saints.data \
                if leap_year(self.year) is False else saints.leapyear()
        else:
            pass  # TODO: add dioceses
        full_calendar = self.add_sanctoral_feasts(temporal, sanctoral).copy()
        self.commit_to_dictionary(target_file='calendar', dic=full_calendar)
        return full_calendar
