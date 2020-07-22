def easter(year):
    firstDigit = year // 100
    Remain19 = year % 19
    temp = (firstDigit - 15) // 2 + 202 - 11 * Remain19
    
    if firstDigit > 26: temp = temp - 1
    if firstDigit > 38: temp = temp - 1
    if firstDigit == 21 or firstDigit == 24 or firstDigit == 25 or firstDigit == 33 or firstDigit == 36 or firstDigit == 37: temp = temp - 1

    temp = temp % 30
    tA = temp + 21
    if temp == 29: tA = tA - 1
    if temp == 28 and Remain19 > 10: tA = tA -1
    # find the next Sunday
    tB = (tA - 19) % 7
    tC = (40 - firstDigit) % 4
    if tC == 3: tC = tC + 1
    

