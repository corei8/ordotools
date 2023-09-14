from ordotools import LiturgicalCalendar

data = LiturgicalCalendar(2024, "roman").build()

for feast in data:
    print(
        f"{feast.date.strftime('%a, %b %d')} : Fasting={feast.fasting}\t{feast.name}"
    )
