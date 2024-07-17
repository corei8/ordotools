from ordotools.tools.helpers import LiturgicalYearMarks
from ordotools.tools.helpers import day
from ordotools.tools.helpers import days
from ordotools.tools.helpers import weeks


"""
Commemorations are a bit tricky to implement. Everything
in this file is for determing the "seasonal commemorations"
for each feast, as well as the Fidélium prayer. The non-seasonal
commemorations are then added on top of these and ordering 
the commemorations is handled by the Feast class.
"""


def advent_season(feast):
    feast.com_1["code"] = 99906
    feast.com_2["code"] = 99909
    return feast

def epiphany_octave_to_septuagesima(year: int, feast):
    if feast.date > day(year, 2, 2):
        feast.com_1["code"] = 99911
        feast.com_2["code"] = 99913
    else:
        feast.com_1["code"] = 99907
        feast.com_2["code"] = 99909 # TODO: or for the pope
    return feast

def septuagesima_to_lent(feast):
    # TODO: special secret of BVM if before February 2nd
    feast.com_1["code"] = 99907
    feast.com_2["code"] = 99909 # or for the pope
    return feast

def lent_to_passiontide(feast):
    feast.com_1["code"] = 99911
    feast.com_2["code"] = 99914
    return feast

def passiontide(feast):
    feast.com_1["code"] = 99909 # or for the pope
    return feast

def easter_octave(feast):
    feast.com_1["code"] = 99909 # or for the pope
    return feast

def easter_season(feast):
    feast.com_1["code"] = 99908
    feast.com_2["code"] = 99909 # or for the pope
    return feast

def pentecost_season(feast):
    feast.com_1["code"] = 99911
    feast.com_2["code"] = 99913
    return feast

def seasonal_commemorations(feasts: tuple, year: int) -> tuple:
    mark = LiturgicalYearMarks(year)
    processed_feasts = ()
    month_indicator = ""

    for feast in feasts:
        if feast.rank_n > 15:

            if mark.first_advent < feast.date < mark.christmas:
                feast = advent_season(feast)

            elif mark.christmas+days(19) < feast.date < mark.lent_begins-weeks(3)-days(3):
                feast = epiphany_octave_to_septuagesima(year, feast)

            elif mark.lent_begins-weeks(3)-days(3) < feast.date < mark.lent_begins:
                feast = septuagesima_to_lent(feast)

            elif mark.lent_begins < feast.date <= mark.lent_ends-weeks(2):
                feast = lent_to_passiontide(feast)

            elif mark.lent_ends-weeks(2) < feast.date < mark.lent_ends:
                feast = passiontide(feast)

            elif mark.easter+days(2) < feast.date < mark.easter+days(7):
                feast = easter_octave(feast)

            elif mark.easter+days(7) < feast.date < mark.easter_season_end:
                feast = easter_season(feast)

            elif mark.pentecost_season_start < feast.date < mark.first_advent:
                feast = pentecost_season(feast)

            else:
                pass

            # FIDELIUM
            if feast.rank_n == 23:  # NOTE: can 23 be an impeded Sunday
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
