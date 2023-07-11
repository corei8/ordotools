from ordotools import LiturgicalCalendar

data = LiturgicalCalendar(2024, "roman").build()

for feast in data:
    print(f"{feast.date.strftime('%a %d')} : {feast.name}\tFasting = {feast.fasting}")
