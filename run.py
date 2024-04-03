from ordotools import LiturgicalCalendar

# TODO: we need to add the language
data = LiturgicalCalendar(2024, "roman", "la").build()

for feast in data:
    if feast.date.strftime("%a") == "Sun":
        print("\r")
    print(
        f"{feast.date.strftime('%a, %b %d')} \t{feast.name}"
    )

# for x in data: print(x)
