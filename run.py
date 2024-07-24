from ordotools import LiturgicalCalendar

# TODO: we need to add the language
data = LiturgicalCalendar(2024, "roman", "la").build()

for feast in data:
    if feast.date.strftime("%a") == "Sun":
        print("\r")
    # print(
    #     f"{feast.date.strftime('%b %d')}\t{feast.name: <49} {feast.rank_v: <28} com: {feast.com_1['name']}, 2 com: {feast.com_2['name']}, 3 com: {feast.com_3['name']}"
    # )
    print(
        f"{feast.date.strftime('%b %d')}\t{feast.name: <49} {feast.abstinence: <28}"
    )

# for x in data: print(x)
