from importlib import import_module

from ordo_tools.feast import Feast

from ordo_tools.helpers import FIRST_ADVENT
from ordo_tools.helpers import LAST_ADVENT
from ordo_tools.helpers import LENT_BEGINS
from ordo_tools.helpers import LENT_ENDS
from ordo_tools.helpers import advance_a_day
from ordo_tools.helpers import days
from ordo_tools.helpers import ladys_office
from ordo_tools.helpers import leap_year

from ordo_tools.liturgical_dates import integer_to_roman

from ordo_tools.temporal import Temporal

from sanctoral.diocese.roman import Sanctoral


class LiturgicalCalendar:

    def __init__(self, year, diocese, country=''):
        self.year = year
        self.diocese = diocese
        self.transfers = {}
        self.temporal = Temporal(self.year).return_temporal()

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

    def explode_octaves(self, feast: Feast) -> dict:
        """
        Generates "explodes" the octave for a feast.
        """
        octave = {}
        for x in range(7):
            intro = f"De {integer_to_roman(x+2)} die"
            if x != 6:
                feast.name = f"{intro} infra {feast.infra_octave_name}"
            else:
                feast.name = feast.infra_octave_name
            feast.rank_v = "feria"
            feast.rank_n = 18 if x < 6 else 13  # common octave
            octave |= {feast.date+days(x+1): feast.updated_properties}
        return octave

    def find_octave(self, year: dict) -> dict:
        """
        Finds the octaves of the sanctoral cycle and adds
        them to the year.
        """
        y = year.copy()
        temporals = []
        for feast in self.temporal.values():
            temporals.append(feast["feast"])
        for date, feast in y.items():
            candidate = Feast(feast_date=date, properties=feast)
            if candidate.name in temporals:
                continue
            elif candidate.octave is True:
                octave = self.explode_octaves(candidate)
                y |= self.add_feasts(master=y, addition=octave)
        return y

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
        print(f"[INFO] Comparing {feast_1.name} to {feast_2.name}...")
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

    def add_feasts(self, master: dict, addition: dict) -> dict:
        """
        Adds additional feasts to the master feast dictionary;
        Sends the feasts that confilict to the ranking function.
        """
        calendar = master.copy()
        for the_date in addition.keys():
            if the_date in calendar.keys():
                ranked_feast = self.rank(
                    date=the_date,
                    sanctoral_feast=addition[the_date],
                    temporal_feast=calendar[the_date]
                )
                calendar |= ranked_feast
            else:
                calendar |= {the_date: addition[the_date]}
        return calendar

    def transfer_feasts(self, dic: dict) -> dict:
        """
        Adds a feast that has to be transfered to a queue that
        is checked against every subsequent day.
        """
        for x in self.transfers.keys():
            trans_feast = Feast(x, self.transfers[x])
            target_date = advance_a_day(trans_feast.date)
            if target_date not in dic.keys():
                dic.update(target_date, trans_feast.feast_properties)
            else:
                pass
        return dic

    def our_ladys_saturday(self, calendar: dict) -> None:
        """
        Adds all the Saturday Offices of the Blessed Virgin
        to the temporal calendar.
        """
        # TODO: add mass number according to season
        year = calendar.copy()
        office = ladys_office
        for feast in year.keys():
            if feast.strftime("%w") == str(6):
                if LENT_BEGINS.date() <= feast.date() <= LENT_ENDS.date():
                    continue
                elif FIRST_ADVENT.date() <= feast.date() <= LAST_ADVENT.date():
                    continue
                else:
                    if year[feast]["rank"][0] > 16:  # not a double
                        year[feast] = office  # TODO: add commemorations
                    else:
                        continue
        return year

    def build(self) -> None:
        """ Stitches the temporal and sanctoral calendars together. """
        saints = Sanctoral(self.year)
        if self.diocese == 'roman':
            sanctoral = saints.data \
                if leap_year(self.year) is False else saints.leapyear()
        else:
            diocese = import_module(
                f"sanctoral.diocese.{self.diocese}",
            )
            sanctoral = diocese.Diocese(self.year).calendar()
        full_calendar = self.add_feasts(self.temporal, sanctoral).copy()
        full_calendar |= self.our_ladys_saturday(full_calendar)
        full_calendar |= self.find_octave(year=full_calendar)
        return full_calendar
