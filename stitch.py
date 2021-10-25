import importlib
import sys
from datetime import timedelta
from datetime import datetime

# from temporal import roman
import temporal
from sanctoral import roman

# sys.path.append(".")
# import temporal.roman


def full_year(year):
    year_list = []
    yearstart = datetime(year=year, month=1, day=1)
    while yearstart.strftime("%Y") != str(year + 1):
        year_list.append(yearstart.strftime("%m/%d"))
        yearstart += timedelta(days=1)
    return year_list


def occur(one, two):
    occur_table = [
        [0, 1, 3, 1, 3, 3, 3, 3, 3, 3, 6, 5, 8, 6, 3, 3, 6],
        [0, 3, 3, 1, 3, 6, 3, 3, 3, 3, 6, 8, 6, 6, 3, 6, 6],
        [0, 3, 3, 3, 3, 4, 3, 3, 3, 7, 4, 4, 4, 0, 4, 4, 4],
        [0, 3, 3, 3, 3, 4, 3, 3, 7, 4, 4, 4, 4, 4, 4, 4, 4],
        [0, 3, 3, 3, 3, 4, 3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [0, 3, 3, 3, 3, 4, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [0, 3, 3, 7, 4, 4, 4, 4, 4, 4, 4, 2, 2, 0, 4, 4, 4],
        [0, 3, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 0, 0, 0],
        [0, 7, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 2, 0, 4, 4, 4],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4],
    ]
    comparison = occur_table[one][two]
    if comparison == 1:
        print('office of the first, nothing of the second')
        result = [True, False, False]
    elif comparison == 2:
        print('office of the second, nothing of the first')
        result = [False, True, False]
    elif comparison == 3:
        print('office of the first, commemoration of the second')
        result = [True, "comm", False]
    elif comparison == 4:
        print('office of the second, commemoration of the first')
        result = ["comm", True, False]
    elif comparison == 5:
        print('office of the first, translation of the second')
        result = [True, "tran", False]
    elif comparison == 6:
        print('office of the second, translation of the first')
        result = [False, "tran", False]
    elif comparison == 7:
        print('office of the more noble, commemoration of the other')
        result = [False, False, "comm"]
    else:
        print('office of the more noble, translation of the other')
        result = [False, False, "tran"]
    return result


def stitch(tem):
    rome = roman.roman_sanctoral
    # temp = map(__import__, "temporal." + "temporal_" + tem)
    temp = importlib.import_module("temporal." + "temporal_" + tem)
    temps = temp.temporal
    print("==> dictionary import successful")
    tempOne = {}
    tempTwo = {}
    all_dates = full_year(int(tem))
    # TODO: combine the dictionaries, making lists for every conflict.
    for date in temps.keys():
        if len(date) == 6:
            tempTwo.__setitem__(date[0:5], temps.get(date))
        else:
            tempOne.__setitem__(date, temps.get(date))
    # TODO: resolve the conflicts using the occurance and concurrance tables.
    for x in all_dates:
        pass  #! compare all the concurring and occuring dates
        one = tempOne.get(x)
        two = tempTwo.get(x)
        tre = rome.get(x)
    # TODO: output a new dictionary with the completed year.
    return 0
