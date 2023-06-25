#!/usr/bin/python3
#########################################################
#                                                       #
#          (c) 2022 - GREGORY ROBERT BARNES             #
#   THIS SOFTWARE MAY NOT BE USED EXCEPT WITH THE       #
#   EXPLICIT PERMISSION OF FR. GREGORY ROBERT BARNES.   #
#    + corei8.github@gmail.com                          #
#                                                       #
#########################################################



def main(year: int, diocese: str):

    def set_global_year(year: int) -> None:
        """ Writes the global year to a file """
        with open("ordo_tools/settings.py", "w") as f:
            f.write('YEAR = ' + str(year))
        return None

    set_global_year(year)

    # from ordo_tools.outputs import build_latex_ordo
    from ordo_tools.outputs import readme_calendar
    from ordo_tools.outputs import build_test_website
    from ordo_tools.utils import LiturgicalCalendar

    data = LiturgicalCalendar(year = year, diocese=diocese).build()

    readme_calendar(year, data)
    # build_test_website(year, Temporal(year).return_temporal())
    build_test_website(year, data)

if __name__ == '__main__':
    main(year=2023, diocese='roman')
