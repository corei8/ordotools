from ordotools.tools.helpers import LiturgicalYearMarks
from ordotools.tools.helpers import day
from ordotools.tools.helpers import days
from ordotools.tools.helpers import weeks

def advent_season(feast):
    return feast

def epiphany_octave_to_septuagesima(feast):
    return feast

def septuagesima_to_lent(feast):
    return feast

def lent_to_passiontide(feast):
    return feast

def easter_octave(feast):
    return feast

def easter_season(feast):
    return feast

def pentecost_season(feast):
    return feast

def seasonal_commemorations(feasts: tuple, year: int) -> tuple:
    mark = LiturgicalYearMarks(year)
    processed_feasts = ()
    month_indicator = ""
    for feast in feasts:
        # assuming that a double never takes the seasonal commemorations
        if feast.rank_n > 15:
            if mark.first_advent < feast.date < mark.christmas:
                feast.com_1["code"] = 99906
                feast.com_2["code"] = 99909
            elif mark.christmas+days(19) < feast.date < mark.lent_begins-weeks(3)-days(3):
                if feast.date > day(year, 2, 2):
                    feast.com_1["code"] = 99911
                    feast.com_2["code"] = 99913
                else:
                    feast.com_1["code"] = 99907
                    feast.com_2["code"] = 99909 # TODO: or for the pope
            elif mark.lent_begins-weeks(3)-days(3) < feast.date < mark.lent_begins:
                # TODO: special secret of BVM if before February 2nd
                feast.com_1["code"] = 99907
                feast.com_2["code"] = 99909 # or for the pope
                processed_feasts += (feast,)
                continue
            elif mark.lent_begins < feast.date <= mark.lent_ends-weeks(2):
                feast.com_1["code"] = 99911
                feast.com_2["code"] = 99914
                processed_feasts += (feast,)
                continue
            elif mark.lent_ends-weeks(2) < feast.date < mark.lent_ends:
                feast.com_1["code"] = 99909 # or for the pope
                processed_feasts += (feast,)
                continue
            elif mark.easter+days(2) < feast.date < mark.easter+days(7):
                feast.com_1["code"] = 99909 # or for the pope
                processed_feasts += (feast,)
                continue
            elif mark.easter+days(7) < feast.date < mark.easter_season_end:
                feast.com_1["code"] = 99908
                feast.com_2["code"] = 99909 # or for the pope
                processed_feasts += (feast,)
                continue
            elif mark.pentecost_season_start < feast.date < mark.first_advent:
                feast.com_1["code"] = 99911
                feast.com_2["code"] = 99913

            # FIDELIUM
            if feast.rank_n == 23: # assuming that 23 never occurs outside our range...
                # NOTE: can 23 be an impeded Sunday
                if feast.date.strftime("%w") == 1:
                    feast.com_2 = {"code": 99912}
                    processed_feasts += (feast,)
                    continue
                if month_indicator == feast.date.strftime("%B"):
                    continue
                else:
                    month_indicator = feast.date.strftime("%B")
                    if month_indicator == "November":
                        continue
                    elif mark.first_advent < feast.date < mark.christmas:
                        continue
                    else:
                        feast.com_2 = {"code": 99912}
                        processed_feasts += (feast,)
                        continue
            else:
                processed_feasts += (feast,)


        else:
            processed_feasts += (feast,)

    return processed_feasts
