from ordotools import LiturgicalCalendar

# TODO: we need to add the language
data = LiturgicalCalendar(2024, "roman", "la").build()

for feast in data:
    if feast.date.strftime("%a") == "Sun":
        print("\r")
    # print(feast.feast_properties)
    print(
        f"{feast.date.strftime('%b %d')}\t{feast.name: <49} {feast.rank_v: <28} {feast.com_1['name']}"
    )

# for x in data: print(x)
