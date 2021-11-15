from ordo_tools.temporal_cycle import build_temporal
from ordo_tools.ordo_tools import *
from ordo_tools.outputs import latex_full_cal_test, readme_calendar




def app(year: int, diocese: str):
    build_temporal(year)
    stitch(year, diocese)
    dict_clean("calen.calendar_", year)
    latex_full_cal_test(year)
    readme_calendar(year)


# 2024 is a leap year
app(year=2022, diocese="roman")
