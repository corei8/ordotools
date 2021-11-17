#
# (c) 2021 - GREGORY ROBERT BARNES
# THIS SOFTWARE MAY NOT BE USED EXCEPT WITH THE
# PERMISSION OF GREGORY ROBERT BARNES.
#
from ordo_tools.temporal_cycle import build_temporal
from ordo_tools.ordo_tools import *
from ordo_tools.outputs import build_latex_ordo


def app(year: int, diocese: str):
    build_temporal(year)
    stitch(year, diocese)
    dict_clean("calen.calendar_", year)
    # latex_full_cal_test(year)
    # readme_calendar(year)
    build_latex_ordo(year)

 # todo use os to get a list of the diocese or regions needed to complete an ordo


# 2024 is a leap year
app(year=2022, diocese="roman")
