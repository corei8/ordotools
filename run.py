from ordotools import LiturgicalCalendar
# from rich import print  ## this "pretty prints" the exiting print statements
from rich.console import Console
from rich.table import Table
# from rich import box
import subprocess

# from rich.live import Live

# with Live(table, refresh_per_second=4):
#     ...

subprocess.run(["clear"], check=True)

# TODO: turn the entire run into a class and we can choose the output

console = Console()

data = LiturgicalCalendar(2027, "Roman", "la").build()

truncate = lambda s: s if len(s) <= 20 else s[:17] + "..."


def num_coms(feast):
    if feast.com_1["name"] is None:
        return "0"
    elif feast.com_2["name"] is None:
        return "1"
    elif feast.com_3["name"] is None:
        return "2"
    else:
        return "3"


table = Table(
    show_header=True,
    header_style="bold red",
    expand=True,
    row_styles=['dim', 'none']
)

# Feasts and number of commemoratins
table.add_column("Date", width=12)  # style="dim", width=12)
table.add_column("Feast Name")
table.add_column("Commemorations", justify="left")
# table.add_column("2 Com", justify="left")
# table.add_column("3 Com", justify="left")

for feast in data:

    if feast.date.strftime("%a") == "Sun":
        table.add_section()

    first_com = ""

    try:
        first_com = feast.commemorations[0].name
    except IndexError:
        first_com = ""
    try:
        second_com = feast.commemorations[1].name
    except IndexError:
        second_com = ""
    try:
        third_com = feast.commemorations[2].name
    except IndexError:
        third_com = ""
    try:
        fourth_com = feast.commemorations[3].name
    except IndexError:
        fourth_com = ""

    # feasts and number of commemorations
    table.add_row(
        feast.date.strftime('%b %d'),
        feast.name + ", [italic]" + feast.rank_verbose + "[/italic]",
        first_com + " | " + second_com + " | " + third_com + " | " + fourth_com
    )

with console.pager(styles=True):
    console.print(table)
