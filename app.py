#!/usr/bin/python3
#########################################################
#                                                       #
#          (c) 2022 - GREGORY ROBERT BARNES             #
#   THIS SOFTWARE MAY NOT BE USED EXCEPT WITH THE       #
#   EXPLICIT PERMISSION OF FR. GREGORY ROBERT BARNES.   #
#    + corei8.github@gmail.com                          #
#                                                       #
#########################################################

from time import perf_counter


def main(year: int, diocese: str):

    start = perf_counter()

    def set_global_year(year: int) -> None:
        """ Writes the global year to a file """
        with open("ordo_tools/settings.py", "w") as f:
            f.write("YEAR = " + str(year))
        return None

    set_global_year(year)

    # from ordo_tools.outputs import build_latex_ordo
    from ordo_tools.outputs import readme_calendar
    # from ordo_tools.outputs import build_test_website
    from ordo_tools.utils import LiturgicalCalendar
    from builders.website import WebCal

    data = LiturgicalCalendar(year=year, diocese=diocese).build()

    readme_calendar(year, data)

    # build_test_website(year, data)

    WebCal(year=year, data=data).build()

    end = perf_counter()

    print(f"[INFO] build time: {str(end-start)[:4]} s.")

    # This sorta works right now...
    # build_latex_ordo(year, data)


if __name__ == "__main__":
    main(year=2023, diocese="roman")
