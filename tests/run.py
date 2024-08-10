from ordotools import LiturgicalCalendar
import logging
# import time

logging.basicConfig(level=logging.DEBUG)

# 5,700,000 is the number of permutations the liturgical year in the Gregorian Calendar

for x in range(5_700_000): # our algorithm for easter maxes out at 10,000...

    data = LiturgicalCalendar(2024+x, "roman", "la").build()

    if len(data) < 365:
        for feast in data:
            if feast.date.strftime("%a") == "Sun":
                print("\r")
            print(
                f"{feast.date.strftime('%a, %b %d %Y')} \t{feast.name}"
            )
        logging.error(f"Day dropped in year {2024+x}, only {len(data)} days.")
        break

    else:
        for feast in data:
            if feast.date.strftime("%a") == "Sun":
                print("\r")
            print(
                f"{feast.date.strftime('%a, %b %d %Y')} \t{feast.name}"
            )
