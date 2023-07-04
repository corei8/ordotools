#!/usr/bin/python3
#########################################################
#                                                       #
#          (c) 2022 - GREGORY ROBERT BARNES             #
#   THIS SOFTWARE MAY NOT BE USED EXCEPT WITH THE       #
#   EXPLICIT PERMISSION OF FR. GREGORY ROBERT BARNES.   #
#                corei8.github@gmail.com                #
#                                                       #
#########################################################

from time import perf_counter


def main(year: int, diocese: str):

    start = perf_counter()

    # TODO: deprecate this
    def set_global_year(year: int) -> None:
        """ Writes the global year to a file """
        with open("tools/settings.py", "w") as f:
            f.write("YEAR = " + str(year))
        return None

    set_global_year(year)

    from tools.algorithm import LiturgicalCalendar
    from builders.website import WebCal
    from builders.readme import Readme

    data = LiturgicalCalendar(year=year, diocese=diocese).build()

    # build_test_website(year, data)

    WebCal(year=year, data=data).build()
    Readme(year=year, data=data).build

    end = perf_counter()

    # TEST:
    print(f"[INFO] build time: {str(end-start)[:4]} s.")

    # This sorta works right now...
    # build_latex_ordo(year, data)


if __name__ == "__main__":
    main(year=2023, diocese="roman")
