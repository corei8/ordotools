from ordotools import LiturgicalCalendar
# from rich import print  ## this "pretty prints" the exiting print statements
from rich.console import Console
from rich.table import Table
from rich import box

# TODO: turn the entire run into a class and we can choose the output

console = Console()

# TODO: we need to add the language
data = LiturgicalCalendar(2025, "roman", "la").build()

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


table = Table(show_header=True, header_style="bold red", box=box.DOUBLE)

table.add_column("Date", style="dim", width=12)
table.add_column("Feast Name")
table.add_column("Rank", justify="center")
table.add_column("Verbose Rank", justify="left")
table.add_column("Com", justify="center")

for feast in data:

    # print(
    #     f"{feast.date.strftime('%b %d')}\t{feast.name: <49} {feast.rank_v: <28} com: {feast.com_1['name']}, 2 com: {feast.com_2['name']}, 3 com: {feast.com_3['name']}"
    # )

    # print(
    #     f"{feast.date.strftime('%b %d')}\
    #     \t{truncate(feast.name): <21} \
    #     \t{feast.rank_n: <3} \
    #     \t{feast.abstinence: <2} \
    #     \t{feast.fasting: <2} \
    #     ".expandtabs(3)
    # )

    # NOTE: feasts and number of commemorations
    table.add_row(
        feast.date.strftime('%b %d, %Y'),
        truncate(feast.name),
        str(feast.rank_n),
        feast.rank_v,
        num_coms(feast)
    )

    if feast.date.strftime("%a") == "Sun":
        table.add_section()

console.print(table)
# for x in data: print(x)
