from ordotools.tools.feast import Feast
from ordotools.tools.helpers import LiturgicalYearMarks


def friday_abstinence(feast: Feast):
    # TODO: if the feast is a holyday of obligation, there is no abstinence
    if feast.date.strftime("%w") == '5':
        feast.abstinence = True


class Fasting:

    def __init__(self, year) -> None:
        self.year = year
        self.lent_ends = LiturgicalYearMarks(self.year).lent_ends
        self.lent_begins = LiturgicalYearMarks(self.year).lent_begins
        pass

    # NOTE: all of these should be combined after they are finished
    def fasting_day_special(self, feast: Feast):
        # TODO: days that change according to the locality
        return None

    def fasting_day_lent(self, feast: Feast):
        if feast.date <= self.lent_ends and feast.date >= self.lent_begins:
            if feast.date.strftime('%w') != '0':
                feast.fasting = True

    def fasting_day_ember(self, feast: Feast):
        # NOTE: how to find all the ember days?
        return None

    def fasting_day_vigil(self, feast: Feast):
        return None
