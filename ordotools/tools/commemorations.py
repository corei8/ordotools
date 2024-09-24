from ordotools.tools.helpers import LiturgicalYearMarks
from ordotools.tools.helpers import day
from ordotools.tools.helpers import days
from ordotools.tools.helpers import weeks

"""
Almost Everything having to do with the ordering and assignment of
commemorations is contained in this file. The "seasonal
commemorations" are added after the commemorations of concurrance
and occurance are figured out.
"""


def existing_commemoration(feast):
    if "code" in feast.com_1.keys():
        if "code" in feast.com_2.keys():
            return 2
        else:
            return 1
    else:
        return 0


def add_commemorations(feast, first, second=None):
    # TODO: add more commemoration rules (Sundays, major ferias, etc.)
    addition_index = existing_commemoration(feast)
    if addition_index == 1:
        feast.com_2["code"] = first
    elif addition_index == 2:
        feast.com_3["code"] = first
    else:
        feast.com_1["code"] = first
        if second is not None:
            feast.com_2["code"] = second
    return feast


def seasonal_commemorations(feasts: tuple, year: int) -> tuple:
    mark = LiturgicalYearMarks(year)
    processed_feasts = ()
    month_indicator = ""

    for feast in feasts:
        if (
                feast.rank_n > 15 or
                feast.rank_n == 12 or
                feast.rank_n == 9
                ):

            if mark.first_advent < feast.date < mark.christmas:
                feast = add_commemorations(feast, 99906, 99909)

            elif feast.date < mark.lent_begins-weeks(2)-days(3):
                if feast.date > day(year, 2, 2):
                    feast = add_commemorations(feast, 99911, 99913)
                else:
                    feast = add_commemorations(feast, 99907, 99909)

            elif mark.lent_begins-weeks(2)-days(3) < feast.date < mark.lent_begins:
                feast = add_commemorations(feast, 99907, 99909)

            elif mark.lent_begins < feast.date <= mark.lent_ends-weeks(2):
                feast = add_commemorations(feast, 99911, 99914)

            elif mark.lent_ends-weeks(2) < feast.date < mark.lent_ends:
                feast = add_commemorations(feast, 99909)

            elif mark.easter+days(2) < feast.date < mark.easter+days(7):
                feast = add_commemorations(feast, 99909)

            elif mark.easter+days(7) < feast.date < mark.easter_season_end:
                feast = add_commemorations(feast, 99908, 99909)

            elif mark.pentecost_season_start < feast.date < mark.first_advent:
                feast = add_commemorations(feast, 99911, 99913)

            else:
                pass

            # FIDELIUM
            if feast.rank_n == 23:  # NOTE: can rank 23 be an impeded Sunday
                if month_indicator == feast.date.strftime("%B"):
                    pass
                else:
                    if month_indicator == "November":
                        pass
                    elif (
                            mark.first_advent < feast.date < mark.christmas or
                            mark.lent_begins < feast.date < mark.lent_ends or
                            mark.easter_season_start < feast.date < mark.easter_season_end
                            ):
                        pass
                    else:
                        feast.com_2 = {"code": 99912}
                        month_indicator = feast.date.strftime("%B")

                if feast.date.strftime("%w") == 1:
                    if mark.first_advent < feast.date < mark.christmas:
                        pass
                    elif mark.lent_begins < feast.date < mark.lent_ends:
                        pass
                    else:
                        if feast.com_2["code"] == 99912:
                            pass
                        else:
                            feast.com_2 = {"code": 99912}

        else:
            pass

        processed_feasts += (feast,)

    return processed_feasts
