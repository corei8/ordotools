Sub EasterDate (d, m, y)

' EASTER DATE CALCULATION FOR YEARS 1583 TO 4099

' y is a 4 digit year 1583 to 4099
' d returns the day of the month of Easter
' m returns the month of Easter

' Easter Sunday is the Sunday following the Paschal Full Moon
' (PFM) date for the year

' This algorithm is an arithmetic interpretation of the 3 step
' Easter Dating Method developed by Ron Mallen 1985, as a vast
' improvement on the method described in the Common Prayer BookFunction EasterHodges(dy, mth, ByVal y, ByVal method) As Boolean

'by David Hodges, derived by refining the "Butcher's Ecclesiastical Calendar" rule
'eliminating one step in the process
Dim a, b, c, d, e, f, g, h, j, k, m, n, p
' Validate arguments
    If method <> 3 Or y < 1583 Or y > 4099 Then
        EasterHodges = False
        d = 0
        m = 0
        MsgBox "Hodges method only applies to the revised calculation in the Gregorian calendar from 1583 to 4099 AD"
        Exit Function
    End If
    EasterHodges = True
    a = y \ 100
    b = y Mod 100
    c = (3 * (a + 25)) \ 4
    d = (3 * (a + 25)) Mod 4
    e = (8 * (a + 11)) \ 25
    f = (5 * a + b) Mod 19
    g = (19 * f + c - e) Mod 30
    h = (f + 11 * g) \ 319
    j = (60 * (5 - d) + b) \ 4
    k = (60 * (5 - d) + b) Mod 4
    m = (2 * j - k - g + h) Mod 7
    n = (g - h + m + 114) \ 31
    p = (g - h + m + 114) Mod 31
    dy = p + 1
    mth = n
'Easter Sunday is g - h + m days after March 22nd
'(the earliest possible Easter date)
End Function