from importlib import import_module

from ordo_tools.feast import Feast

from ordo_tools.helpers import FIRST_ADVENT
from ordo_tools.helpers import LAST_ADVENT
from ordo_tools.helpers import LENT_BEGINS
from ordo_tools.helpers import LENT_ENDS
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
        self.transfers = None
        self.temporal = Temporal(self.year).return_temporal()

    def fasting(self, feast: Feast) -> Feast:
        """
        Return the feast with updated fasting rules.
        The commemoration will always have the fasting rules,
        even on a second pass e.g., for a transferred feast.
        """
        # TODO: check the higher date against the holydays of obligation
        if feast.com[0]["fasting"] is True:
            feast.fasting = True
        return feast

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

    def commemoration(self, feast: Feast, com: Feast) -> dict:
        """
        Adds one feast as the commemoration of another feast.
        """
        feast.com.insert(0, com.feast_properties)
        return self.fasting(feast).updated_properties

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

    def rank(self, dynamic: Feast, static: Feast) -> dict:
        # TODO: this should return a Feast object.
        """
        Ranks feasts that occur on the same date. Send feasts that can be
        transferred to the transfer dictionary. "Dynamic" is from the
        sanctoral cycle, and "static" is from the temporal cycle.
        """
        date = static.date
        print(f'[INFO] ranking "{dynamic.feast}" against "{static.feast}".')

        # if the feasts are the same rank:
        if dynamic.rank_n == static.rank_n:
            print('      ...same rank')
            return {
                date:
                self.rank_by_nobility(
                    dynamic,
                    static
                )['higher'].feast_properties,
            }
        else:
            candidates = {
                dynamic.rank_n: dynamic,
                static.rank_n: static,
            }
            higher = candidates[sorted(candidates)[0]]
            lower = candidates[sorted(candidates)[1]]

            # FIXME: not sure what is going on here...
            if lower.rank_n == 22:
                pass

                # FIX: just a hack for now
            if lower.rank_n == 19:  # lent
                return {
                    date: self.commemoration(
                        feast=higher,
                        com=lower
                    )
                }
            # TODO: this has to be a separate function:

            # feasts that do not take a commemoration
            if higher.rank_n <= 4:
                print('      ...higher does not take a commemoration')
                # lower feast is transferred
                if lower.rank_n <= 10:
                    if lower.fasting is True:
                        higher.fasting = True
                        return {date: higher.feast_properties}
                    if lower != self.transfers:
                        self.transfers = lower
                else:
                    # lower feast is ignored
                    if lower.fasting is True:
                        higher.fasting = True
                    return {date: higher.feast_properties}
                # HACK: allows transfers to occur on ferias, etc.

            # impeded DM, D and SD
            elif 14 <= lower.rank_n <= 16:
                print('      ...impeded DM, D or SD')
                # if higher.rank_n == 12:
                #     return {
                #         date: self.commemoration(
                #             feast=higher,
                #             com=lower
                #         )
                #     }
                # else:  # FIX: why are these the same
                return {
                    date: self.commemoration(
                        feast=higher,
                        com=lower
                    )
                }
            else:
                print(f'      ..."{higher.feast}" commemorates "{lower.feast}"')
                return {
                    date: self.commemoration(
                        feast=higher,
                        com=lower
                    )
                }
        # return ranked_feasts

    def transfer_feast(self, feast: Feast) -> None:
        """
        Checks for feasts in the transfer dictionary.
        """
        if self.transfers:
            for t in self.transfers:
                # t.date = advance_a_day(t.date)
                return self.rank(dynamic=t, static=feast)

    def add_feasts(self, master: dict, addition: dict) -> dict:
        """
        Adds additional feasts to the master feast dictionary;
        Sends the feasts that confilict to the ranking function.
        """
        calendar = master.copy()
        for the_date in addition.keys():
            if the_date in calendar.keys():
                feast = self.rank(
                    dynamic=Feast(the_date, addition[the_date],),
                    static=Feast(the_date, calendar[the_date])
                )
            else:
                feast = {the_date: addition[the_date]}
            if self.transfers and self.transfers.date == the_date-days(1):
                # TODO: rank the overlapping transfers
                result = self.transfer_feast(
                    Feast(the_date, addition[the_date])
                )
                if result == feast:
                    feast = feast
                else:
                    # WARN: this assumes that there is no transfer overlap
                    self.transfers = None
                    feast = result
            calendar |= feast
        return calendar

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

    # def update_calendar(self, data: dict) -> dict:
    #     """
    #     Updates the calendar file
    #     """
    #     cal = {}
    #     # FIX: this is deprecated now.
    #     for x, y in data.items():
    #         cal.update({x: y})
    #     with open('calen/calendar_' + str(self.year) + '.py', 'a') as f:
    #         f.truncate(0)
    #         f.write('from ordo_tools.helpers import day\n\n')
    #         f.write("class LiturgicalCalendar:\n\n")
    #         f.write("\tdef __init__(self):\n")
    #         f.write('\t\tself.data = {\n')
    #         for i, line in enumerate(sorted(cal)):
    #             date = f"""\t\t\tday(year={self.year},\
    #                         month={line.strftime('%m').lstrip('0')},\
    #                         day={line.strftime('%d').lstrip('0')})"""
    #             if i != 0:
    #                 f.write(f"{date}: {cal[line]},\n")
    #             else:
    #                 f.write(f"{date}: {cal[line]},\n")
    #                 f.write('\t\t}\n\n')
    #         f.write('\t\tdef data(self) -> dict:\n')
    #         f.write('\t\t\treturn self.data')
    #     return None

    # def commit_to_dictionary(self, target_file: str, dic: dict) -> None:
    #     """
    #     Takes a dictionary and writes it to a file.
    #     """
    #     # FIXME: this is deprecated now.
    #     self.update_calendar(data=dic)
    #     return dic
