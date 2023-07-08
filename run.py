from ordotools import LiturgicalCalendar

data = LiturgicalCalendar(2024, "roman").build()

for x in data:
    print(x)
