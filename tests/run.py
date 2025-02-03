from ordotools import LiturgicalCalendar
import logging
# import time
from datetime import date, datetime, timedelta

logging.basicConfig(level=logging.DEBUG)

# 5,700,000 is the number of permutations the liturgical year in the Gregorian Calendar

x = datetime.now().year

while x < 10000:  # our algorithm for easter maxes out at 10,000...

    data = LiturgicalCalendar(x, "roman", "la").build()

    if len(data) < 365:
        for feast in data:
            if feast.date.strftime("%a") == "Sun":
                print("\r")
            print(
                f"{feast.date.strftime('%a, %b %d %Y')} \t{feast.name}"
            )
        logging.error(f"Day dropped in year {2024+x}, only {len(data)} days.")
        generated_dates = [feast.date.strftime('%a, %b %d %Y') for feast in data]

        def get_dates_in_year(year):
            year = year + 2024
            start_date = date(year, 1, 1)
            end_date = date(year, 12, 31)
            delta = end_date - start_date
            dates = []
            for i in range(delta.days + 1):
                day = start_date + timedelta(days=i)
                dates.append(day.strftime('%a, %b %d %Y'))

            return dates

        for d in get_dates_in_year(x):
            if d not in generated_dates:
                logging.error(f"\t-> missing {d}")

        break

    else:
        for feast in data:
            if feast.date.strftime("%a") == "Sun":
                print("\r")
            print(
                f"{feast.date.strftime('%a, %b %d %Y')} \t{feast.name}"
            )
    x += 1
