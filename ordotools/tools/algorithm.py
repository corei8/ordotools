from copy import deepcopy

from importlib import import_module

from ordotools.tools.feast import Feast

from ordotools.tools.helpers import LiturgicalYearMarks
from ordotools.tools.helpers import days
from ordotools.tools.helpers import ladys_office
from ordotools.tools.helpers import leap_year

from ordotools.tools.temporal import Temporal

from ordotools.sanctoral.diocese.roman import Sanctoral

import logging

logging.basicConfig(level=logging.DEBUG)


class LiturgicalCalendar:

    def __init__(self, year, diocese, language, country=""):
        self.year = year
        self.diocese = diocese
        self.language = language

        # TODO: theoretically we could have more than one...
        self.transfers = None
        self.temporal = Temporal(self.year).return_temporal()
        self.FIRST_ADVENT = LiturgicalYearMarks(self.year).first_advent
        self.LAST_ADVENT = LiturgicalYearMarks(self.year).last_advent
        self.LENT_BEGINS = LiturgicalYearMarks(self.year).lent_begins
        self.LENT_ENDS = LiturgicalYearMarks(self.year).lent_ends

    def expand_octaves(self, feast: Feast) -> dict:
        """
        Generates (or expands) the octave for a feast.
        """
        octave = {}
        day = 2
        while day < 9:
            new_feast = Feast(feast.date+days(day-1), feast.updated_properties)
            # WARN: this is a hack for now!!
            if day == 8:
                new_feast.day_in_octave = day
                # new_feast.name = feast.infra_octave_name
            else:
                # intro = f"De {integer_to_roman(day)} die"
                # new_feast.name = f"{intro} infra {feast.infra_octave_name}"
                new_feast.day_in_octave = day
            # FIX: we have an issue here if the feast falls on a Friday
            new_feast.fasting = False
            new_feast.rank_v = "feria"
            new_feast.rank_n = 18 if day < 6 else 13 # for common octaves
            octave |= {new_feast.date: new_feast.updated_properties}
            day += 1
        return octave

    def find_octave(self, year: dict) -> dict:
        """
        Finds the octaves of the sanctoral cycle and adds them to the year.
        """
        calendar = year.copy()
        temporals = [feast["code"] for feast in self.temporal.values()]
        for candidate in calendar.values():
            if candidate.code in temporals:
                continue
            elif candidate.octave is True:
                octave = self.expand_octaves(deepcopy(candidate))
                calendar |= self.add_feasts(master=calendar, addition=octave)
        return calendar

    def commemoration(self, feast: Feast, com: Feast) -> Feast:
        if "com" in com.feast_properties.keys():
            com.feast_properties.pop("com")
        feast.com.insert(0, com.feast_properties)
        return feast

    def rank_by_nobility(self, feast_1: Feast, feast_2: Feast) -> dict:
        """
        Those feasts that are of the same rank need to be ranked according to
        the nobility of the feast (e.g., a feast of Our Lord is of a higher
        nobility than a feast of Our Lady).
        """
        for x in range(6):
            if feast_1.nobility[x] < feast_2.nobility[x]:
                return {'higher': feast_1, 'lower': feast_2}
            elif feast_1.nobility[x] > feast_2.nobility[x]:
                return {'higher': feast_2, 'lower': feast_1}
            else:
                pass
        return {'higher': feast_1, 'lower': feast_2}

    def rank(self, dynamic: Feast, static: Feast) -> Feast:
        if dynamic.rank_n == static.rank_n:
            return self.rank_by_nobility(dynamic, static)['higher']
        else:
            candidates = {dynamic.rank_n: dynamic, static.rank_n: static}
            higher = candidates[sorted(candidates)[0]]
            lower = candidates[sorted(candidates)[1]]
            if lower.rank_n == 22:
                pass
            if lower.rank_n == 19:
                return self.commemoration(feast=higher, com=lower)
            if higher.rank_n <= 4:
                if lower.rank_n == 3:
                    self.transfers = higher
                    return lower
                if lower.rank_n <= 10:
                    if lower.fasting is True:
                        higher.fasting = True
                    if lower != self.transfers:
                        self.transfers = lower
                    return higher
                else:
                    if lower.fasting is True:
                        higher.fasting = True
                    return higher
            elif 14 <= lower.rank_n <= 16:
                return self.commemoration(feast=higher, com=lower)
            else:
                return self.commemoration(feast=higher, com=lower)

    def transfer_feast(self, feast: Feast) -> None:
        """
        Checks for feasts in the transfer dictionary.
        """
        return self.rank(dynamic=self.transfers, static=feast)

    def add_feasts(self, master: dict, addition: dict) -> dict:
        """
        Adds additional feasts to the master feast dictionary;
        Sends the feasts that confilict to the ranking algorithm.
        """
        calendar = master.copy()
        for date, data in calendar.items():
            if date in addition:
                if type(data) is Feast:
                    data = data.updated_properties
                feast = self.rank(
                    dynamic=Feast(date, addition[date]),
                    static=Feast(date, data)
                )
            else:
                if type(data) is Feast:
                    data = data.updated_properties
                feast = Feast(date, data)
            if self.transfers is not None:
                print(f"we are transferring {self.transfers.code}")
                result = self.transfer_feast(
                    Feast(date, feast.updated_properties)
                )
                if result.code == feast.code:
                    pass
                else:
                    self.transfers = None
                    feast = result
            try:
                calendar |= {date: feast}
            except TypeError:
                pass
        return calendar

    def our_ladys_saturday(self, calendar: dict) -> None:
        """
        Adds Office of the Blessed Virgin Mary on Saturdays.
        """
        year = calendar.copy()
        office = ladys_office
        for feast in year.keys():
            if feast.strftime("%w") == str(6):
                if self.LENT_BEGINS.date() <= feast.date() <= self.LENT_ENDS.date():
                    continue
                elif self.FIRST_ADVENT.date() <= feast.date() <= self.LAST_ADVENT.date():
                    continue
                else:
                    if year[feast].rank_n > 16:
                        year[feast] = Feast(feast, office)
                    else:
                        continue
        return year

    def add_translation(self, compiled_cal: dict) -> dict:
        year = []
        for date, feast in compiled_cal.items():
            feast.lang = self.language
            year.append(feast)
        return year

    def build(self) -> None:
        print("Starting the Calendar...")
        print("Gathering Sanctoral Cycle...")
        saints = Sanctoral(self.year)
        if self.diocese == 'roman':
            sanctoral = saints.data if leap_year(self.year) is False else saints.leapyear()
        else:
            diocese = import_module(
                f"sanctoral.diocese.{self.diocese}",
            )
            sanctoral = diocese.Diocese(self.year).calendar()

        print("Adding Feasts...")
        full_calendar = self.add_feasts(self.temporal, sanctoral).copy()
        print("Checking for Our Lady's Saturday...")
        full_calendar |= self.our_ladys_saturday(full_calendar)
        print("Looking for Octaves...")
        full_calendar |= self.find_octave(year=full_calendar)
        print("Adding Translations...")
        return self.add_translation(full_calendar)
