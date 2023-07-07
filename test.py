from ordotools import LiturgicalCalendar

data = LiturgicalCalendar(2023, "roman").build()

for x in data:
    print(x)
