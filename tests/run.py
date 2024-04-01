from ordotools import LiturgicalCalendar

data = LiturgicalCalendar(2024, "roman").build()

for feast in data:
    if feast.date.strftime("%a") == "Sun":
        print("\r")
    print(
        # f"{feast.date.strftime('%a, %b %d')} : Fasting={feast.fasting}\t{feast.name}"
        f"{feast.date.strftime('%a, %b %d')} \t{feast.name}"
    )
