#!/usr/bin/python3

from time import perf_counter

def main(year: int, diocese: str):

    start = perf_counter()

    # # TODO: deprecate this
    # def set_global_year(year: int) -> None:
    #     """ Writes the global year to a file """
    #     with open("tools/settings.py", "w") as f:
    #         f.write("YEAR = " + str(year))
    #     return None

    # set_global_year(year)

    from tools.algorithm import LiturgicalCalendar

    data = LiturgicalCalendar(year=year, diocese=diocese).build()

    end = perf_counter()

    # TEST:
    print(f"[INFO] build time: {str(end-start)[:4]} s.")

    # This sorta works right now...
    # build_latex_ordo(year, data)


if __name__ == "__main__":
    main(year=2023, diocese="roman")
