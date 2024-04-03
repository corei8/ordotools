from ordotools import LiturgicalCalendar
# import time


# start_time = time.time()

data = LiturgicalCalendar(2024, "roman", "la").build()

# execution = time.time() - start_time
for feast in data:
    if feast.date.strftime("%a") == "Sun":
        print("\r")
    print(
        f"{feast.date.strftime('%a, %b %d')} \t{feast.name}"
    )
# print(f"\nExecution: {execution}")
