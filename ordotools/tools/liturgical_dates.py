from datetime import datetime


def integer_to_roman(num: int) -> str:
    return (
        "_",
        "I",
        "II",
        "III",
        "IV",
        "V",
        "VI",
        "VII",
        "VIII",
        "IX",
        "X",
        "XI",
        "XII",
        "XIII",
        "XIV",
        "XV",
        "XVI",
        "XVII",
        "XVIII",
        "XIX",
        "XX",
        "XXI",
        "XXII",
        "XXIII",
        "XXIV",
        "XXV",
        "XXVI",
        "XXVII",
        "XXVIII",
        "XXIX",
        "XXX",
        "XXXI",
        "XXXII",
        "XXXIII",
    )[num]


def nth(num: int) -> str:
    return f"{str(num)}{['st', 'nd', 'rd'][num-1] if num < 4 and 0 < num else 'th'}"


def dominical(year=int) -> str:
    letter, y, c = '', int(str(year)[2:]), int(str(year)[:2])
    index = (y+(y/4)+5*(c % 4)-1) % 7
    letters = ['G', 'F', 'E', 'D', 'C', 'B', 'A']
    first_letter, second_letter = '', ''
    try:
        datetime(year, 2, 29)
        first_letter = letters[int(index)-1]
        if int(index) < 0:
            first_letter = letters[6]
        second_letter = letters[int(index)]
    except ValueError:
        second_letter = letters[int(index)]
    letter = first_letter+second_letter
    return letter


def golden_number(year=int) -> int:
    # todo remove the other golden number function in utils
    return (year+1) % 19


def epact_adjust(year=int) -> int:
    l, s, c = 0, 0, int(str(year)[:2])
    if c % 2:
        l = -1
    if not (c-2) % 4:
        l = -1
    if not c % 3:
        if not (c-17) % 25:
            s = 0
        else:
            s = 1
    if not (c-18) % 25:
        s = 1
    return l + s


def epact_build(adjust=int) -> list:
    build_base, day, x = [], 1, 0
    while x != 19:
        day += 11*(x if x == 0 else 1)
        if day > 30:
            day -= 30
        build_base.append(day)
        x += 1
    build = []
    for y in build_base:
        y += adjust
        if y > 31:
            y -= 31
        elif y <= 0:
            y += 31
        build.append(y)
    return build


def epact(year=int) -> str:
    # ? should we nest the other two functions here?
    e, base, i = '', 1600, 0
    while year >= base:
        i += epact_adjust(year)
        year -= 100
    epact_list = epact_build(i)
    e = integer_to_roman(epact_list[golden_number(year)-1])
    if e == 'XXXI':
        e = '*'
    return e


def epact_chart(year=int) -> int:
    """ This function is guaranteed to be accurate """
    gn = golden_number(year)
    epct = 0
    if 0 <= year <= 1582:
        epct = 0
    elif 1583 <= year <= 1699:
        epct = 1
    elif 1700 <= year <= 1899:
        epct = 2
    elif 1900 <= year <= 2199:
        epct = 3
    elif 2200 <= year <= 2299:
        epct = 4
    elif 2300 <= year <= 2399:
        epct = 5
    elif 2400 <= year <= 2499:
        epct = 6
    elif 2500 <= year <= 2599:
        epct = 7
    elif 2600 <= year <= 2899:
        epct = 8
    elif 2900 <= year <= 3099:
        epct = 9
    else:
        epct = 0
    matrix = [
        [30, 11, 22, 3, 14, 25, 6, 17, 28, 9, 20, 1, 12, 23, 4, 15, 26, 7, 18, ],
        [1, 12, 23, 4, 15, 26, 7, 18, 29, 10, 21, 2, 13, 24, 5, 16, 27, 8, 19, ],
        [30, 11, 22, 3, 14, 25, 6, 17, 28, 9, 20, 1, 12, 23, 4, 15, 26, 7, 18, ],
        [29, 10, 21, 2, 13, 24, 5, 16, 27, 8, 19, 30, 11, 22, 3, 14, 25, 6, 17, ],
        [28, 9, 20, 1, 12, 23, 4, 15, 26, 7, 18, 29, 10, 21, 2, 13, 24, 5, 16, ],
        [27, 8, 19, 30, 11, 22, 3, 14, 25, 6, 17, 28, 9, 20, 1, 12, 23, 4, 15, ],
        [28, 9, 20, 1, 12, 23, 4, 15, 26, 7, 18, 29, 10, 21, 2, 13, 24, 5, 16, ],
        [27, 8, 19, 30, 11, 22, 3, 14, 25, 6, 17, 28, 9, 20, 1, 12, 23, 4, 15, ],
        [26, 7, 18, 29, 10, 21, 2, 13, 24, 5, 16, 27, 8, 19, 30, 11, 22, 3, 14, ],
        [25, 6, 17, 28, 9, 20, 1, 12, 23, 4, 15, 26, 7, 18, 29, 10, 21, 2, 13, ],
    ]
    return matrix[epct][gn-1]
