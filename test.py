from ordotools import LiturgicalCalendar
from datetime import datetime

year = 1950

data = LiturgicalCalendar(year, "Roman", "la").build()


with open("test_files/current.txt", "w") as f:
    f.truncate(0)
    for feast in data:
        f.write(f"{feast.date.strftime('%m-%d')} {feast.name}\n")


with open("test_files/current.txt", "r") as current, open(f"test_files/{year}.txt", "r") as testfile:
    errors = 0
    for line, (day_current, day_testfile) in enumerate(zip(current, testfile)):
        if day_current != day_testfile:
            errors += 1
            print(f"\t⚠️ error on line {line+1} of current.txt")
    if errors:
        print(f"Test complete with {errors} error{'s' if errors > 1 else ''}.")
    else:
        print("Test completed with no errors.")
