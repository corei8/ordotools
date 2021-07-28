import sys
from datetime import datetime
from datetime import timedelta

# from temporal import roman
import temporal
from sanctoral import roman

# sys.path.append(".")
# import temporal.roman


def stitch(tem):
    rome = roman.roman_sanctoral
    temp = map(__import__, "temporal." + "temporal_" + tem)
    print("==> dictionary import successful")
    # TODO: combine the dictionaries, making lists for every conflict.

    # TODO: resolve the conflicts using the occurance and concurrance tables.
    # TODO: output a new dictionary with the completed year.
    return 0
