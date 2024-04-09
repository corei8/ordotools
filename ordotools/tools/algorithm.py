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
        octave = {}
        day = 2
        while day < 9:
            # NOTE: since we already have the feast object,
            #       we can just make a function to set the date.
            #       We also have to empty the commemorations.
            new_feast = Feast(feast.date+days(day-1), feast.updated_properties)  #, lang=self.language)
            if day == 8:
                new_feast.day_in_octave = day
            else:
                new_feast.day_in_octave = day
            # FIX: we have an issue here if the feast falls on a Friday
            new_feast.fasting = False
            new_feast.rank_v = "feria"
            new_feast.rank_n = 18 if day < 6 else 13
            # new_feast.reset_commemorations()
            octave |= {new_feast.date: new_feast.updated_properties}
            day += 1
        return octave

    def find_octave(self, year: dict) -> dict:
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
        # FIX: I don't think we need to return anything here.
        feast.com_1 = com.feast_properties
        return feast

    def rank_by_nobility(self, feast_1: Feast, feast_2: Feast) -> dict:
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

    def transfer_feast(self, feast: Feast) -> Feast:
        return self.rank(dynamic=self.transfers, static=feast)

    def add_feasts(self, master: dict, addition: dict) -> dict:
        calendar = master.copy()
        # there is something wrong here... We should have all "feast" objects...
        for date, data in calendar.items():
            if date in addition:
                if type(data) is Feast:
                    data = data.updated_properties
                feast = self.rank(
                    dynamic=Feast(date, addition[date], lang=self.language),
                    static=Feast(date, data, lang=self.language)
                )
            else:
                if type(data) is Feast:
                    data = data.updated_properties
                feast = Feast(date, data, lang=self.language)
            if self.transfers is not None:
                result = self.transfer_feast(
                    Feast(date, feast.updated_properties, lang=self.language)
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

    def our_ladys_saturday(self, calendar: dict) -> dict:
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
                        year[feast] = Feast(feast, office, lang=self.language)
                    else:
                        continue
        return year

    def add_translation(self, compiled_cal: dict) -> list:
        year = []
        for feast in compiled_cal.values():
            feast.lang = self.language
            year.append(feast)
        return year

    def build(self) -> list:
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
        return [value for value in full_calendar.values()]
        # return self.add_translation(full_calendar)
