import importlib
from datetime import timedelta, datetime
import re
import subprocess
import os

ROMANS = ["I", "II", "III", "IV", "V", "VI", "VII",
          "VIII", "IX", "X", "XI", "XII", "XIII",
          "XIV", "XV", "XVI", "XVII", "XVIII", "XIX",
          "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV",
          "XXVI", "XXVII", "XXVIII", ]


def easter(year: int):
    firstDigit, Remain19 = year // 100, year % 19
    temp = (firstDigit - 15) // 2 + 202 - 11 * Remain19
    if firstDigit > 26:
        temp = temp - 1
    if firstDigit > 38:
        temp = temp - 1
    if (
        firstDigit == 21
        or firstDigit == 24
        or firstDigit == 25
        or firstDigit == 33
        or firstDigit == 36
        or firstDigit == 37
    ):
        temp = temp - 1
    temp = temp % 30
    tA = temp + 21
    if temp == 29:
        tA = tA - 1
    if temp == 28 and Remain19 > 10:
        tA = tA - 1
    tB, tC = (tA - 19) % 7, (40 - firstDigit) % 4
    if tC == 3:
        tC = tC + 1
    if tC > 1:
        tC = tC + 1
    temp = year % 100
    tD = (temp + (temp // 4)) % 7
    tE = ((20 - tB - tC - tD) % 7) + 1
    d = tA + tE
    if d > 31:
        d = d - 31
        m = 4
    else:
        m = 3
    return datetime(year=year, month=m, day=d)


def day(year: int, month: int, day: int):
    return datetime(year=year, month=month, day=day)


def week(i: int):
    return timedelta(weeks=i)


def indays(numdays: int):
    x = timedelta(days=numdays)
    return x


def weekday(date: int):
    return date.strftime("%a")


def findsunday(date):  # ! this can be better handled with %w -- no conversion necessary
    if date.strftime("%a") == "Mon":
        x = 1
    if date.strftime("%a") == "Tue":
        x = 2
    if date.strftime("%a") == "Wed":
        x = 3
    if date.strftime("%a") == "Thu":
        x = 4
    if date.strftime("%a") == "Fri":
        x = 5
    if date.strftime("%a") == "Sat":
        x = 6
    if date.strftime("%a") == "Sun":
        x = 0
    return timedelta(days=x)


def leap_year(year: int):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


""" def matthew(leapyear: bool, easter: int,):
    if leapyear == True:
        if easter(easter)-week(9)-indays(4) > datetime.strptime('02/23', '%m/%d'):
            return 0 # todo Mass can be either of the feast or of the vigil
        else:
            return 0 # todo no commemoration of the vigil in office, Mass private of either ferial, feast or vigil
    else:
        return 0 """


def transfer(year: int, diocese: str):
    """ Calculate the date of all feasts that can be transferred

    Args:
        year (integer)  : year of the ordo
        diocese (string): diocese of the current calendar
    Returns:
        0
    """
    # ? is the feast a double of the first or second cass?
    # ? what is the pre-eminence?
    # here we have to consider, in order:
    # RITE,
    # GREATER SOLEMNITY,
    # QUALITY,
    # DIGNITY,
    # QUALITY OF THE PROPER.
    nobility = {'rite': 'd I cl' or 'd II cl', 'solemnity': 0,
                'quality': 0, 'dignity': 0, 'proper': False}
    # for the other feasts:
    # use the ranking in occurance.md
    return 0


def dict_clean(direct: str, dict: int):
    """ Gets rid of all dates in calendar which are appended with . or _;
    overwrites the calendar file with the resulting dictionary.

    Args:
        direct (integer)   : the relative path to the dictionary, in format calendar/calendar_
        dict   (dictionary): year of the calendar to clean
    """
    mdl = importlib.import_module(direct + str(dict))
    try:
        dic = mdl.temporal
    except AttributeError:
        dic = mdl.calen
    for second_ in sorted(dic):
        gtg = True
        if len(second_) >= 6:
            continue
        else:
            if not second_+'.' in sorted(dic):
                print('Did not find dotted date: \t'+second_+'.')
                continue
            else:
                print('Found a dotted date.....: \t'+second_+'.')
                first_ = second_+'.'
                if dic[second_]['rank'][0] > dic[first_]['rank'][0]:
                    first, second = first_, second_
                elif dic[second_]['rank'][0] == dic[first_]['rank'][0]:
                    # ! nobility
                    gtg = False  # for testing only
                    pass
                else:
                    first, second = second_, first_
                if gtg == False:
                    pass
                else:
                    # tranlsation
                    if dic[first]['rank'][0] <= 4 and dic[second]['rank'][0] <= 10:
                        dic.update({first.strip('.'): dic[first]})
                        dic.update({'trans ' + second.strip('.'): dic[second]})
                    # no commemoration
                    elif dic[first]['rank'][0] <= 4 and dic[second]['rank'][0] > 10:
                        dic.update({first.strip('.'): dic[first]})
                    # commemoration
                    # todo refined these ranges:
                    elif 19 > dic[first]['rank'][0] > 4 and 19 > dic[second]['rank'][0] >= 6:
                        dic[first].update({'com1': dic[second]['feast']})
                        dic.update({first.strip('.'): dic[first]})
                    # no commemoration
                    else:
                        dic.update({first.strip('.'): dic[first]})
                    if len(first) == 6:
                        dic.pop(first)
                    if len(second) == 6:
                        dic.pop(second)
    with open(re.sub(r"\.", r'/', direct) + str(dict) + ".py", "a") as f:
        f.truncate(0)
        for i, line in enumerate(sorted(dic)):
            if i == 0:
                f.write(re.sub(r"/(temporal|calendar)", '', re.sub(r"\.", r'/', direct) + str(dict)) +
                        ' = {\n\'' + line + '\' : ' + str(dic[line]) + ',\n')
            else:
                f.write('\'' + line + '\' : ' + str(dic[line]) + ',\n')
        f.write('}')
        f.close()
        return 0


def stitch(year: int, s: str):
    mdl_temporal = importlib.import_module(
        'temporal.temporal_' + str(year)).temporal
    mdl_sanctoral = importlib.import_module('sanctoral.' + s).sanctoral
    mdlt, mdls = sorted(mdl_temporal), sorted(mdl_sanctoral)
    # todo for adjusting the feasts of the year:
    # todo matthew(leap_year(year), easter(year))
    if leap_year(year) == False:
        pass
    else:
        for event in mdls:
            if not 'leapdate' in mdl_sanctoral[event]:
                pass
            else:
                new_date = mdl_sanctoral[event].get('leapdate')
                mdl_sanctoral.update({new_date if not new_date in mdl_sanctoral else (
                    new_date+'.' if not new_date+'.' in mdl_sanctoral else new_date+'_'): mdl_sanctoral[event]})
    calen = {}  # ! see if it is cheaper to make a dic and update it at the same time
    for feast in mdls:
        calen.update(
            {feast + '.' if feast in mdlt else feast: mdl_sanctoral[feast]}
        )
    for feast in mdlt:
        calen.update({feast: mdl_temporal[feast]})
    # ! test:
    for x in sorted(calen.keys()):
        print(x)

    with open("calen/calendar_" + str(year) + ".py", "w") as f:
        f.truncate(0)
        for i, line in enumerate(sorted(calen)):
            if i == 0:
                f.write('calen = {\n\''+line+'\': '+str(calen[line])+',\n')
            else:
                f.write('\''+line+'\':'+str(calen[line])+',\n')
        f.write('}')
    f.close()
    return 0


def latex_full_cal_test(year):
    # ! make this calendar import work with a variable
    mdl = importlib.import_module(
        'calen.calendar_' + str(year)).calen
    mdldates = sorted(mdl)
    with open("output/latex/calendar_" + str(year) + ".tex", "a") as f:
        f.truncate(0)
        f.write(
            r"""
% !TEX program = lualatex
\documentclass[10pt]{article}
\title{Ordo -- Full Calendar -- 2022}
\usepackage{longtable}
\usepackage{geometry}
\usepackage[letterspace=500]{microtype}
\usepackage[T1]{fontenc}
\usepackage[usefilenames,RMstyle={Text,Semibold},SSstyle={Text,Semibold},TTstyle={Text,Semibold},DefaultFeatures={Ligatures=Common}]{plex-otf} %
\usepackage[latin]{babel}
\usepackage{fontspec}
% LETTERPAPER:
\geometry{paperheight=8.5in, paperwidth=11in, left=1.0in, right=1.0in, top=1.0in, bottom=1.0in,}
\usepackage[table]{xcolor}
\definecolor{lightblue}{rgb}{0.93,0.95,1.0}
\begin{document}
%\maketitle
\textit{\centering\footnotesize Ignore dates with periods after the day.}
\rowcolors{1}{}{lightblue}
\begin{longtable}{ l l l }
\hline
\textsc{Date} & \textsc{Rank} & \textsc{Feast} \\
\hline
\endhead
"""
        )
        for x in mdldates:
            if len(x) <= 6:
                f.write("" + x + ', ' + datetime.strptime(x.strip('.') + '/' + str(year), '%m/%d/%Y').strftime('%a') + " & " + mdl[x]['rank'][-1] +
                        " & " + re.sub(r'&', '\&', mdl[x]['feast']) + "\\\\\n")
            else:
                f.write("" + x + ', ' + datetime.strptime(x.strip('trans .') + '/' + str(year), '%m/%d/%Y').strftime('%a') + " & " + mdl[x]['rank'][-1] +
                        " & " + re.sub(r'&', '\&', mdl[x]['feast']) + "\\\\\n")
            # todo find a solution for labeling commemorations
            if 'com1' in mdl[x].keys():
                f.write("" + '' + " & & " + '\\textit{Com:} ' +
                        re.sub(r'&', '\&', mdl[x]['com1']) + "\\\\\n")
            else:
                pass
            if 'comm2' in mdl[x].keys():
                if len(mdl[x]['comm2']['feast']) > 0:
                    f.write("" + '' + " & & " + '\\textit{Com:} ' +
                            re.sub(r'&', '\&', mdl[x]['comm2']['feast']) + "\\\\\n")
                else:
                    pass
            else:
                pass
            if 'comm3' in mdl[x].keys():
                if len(mdl[x]['comm3']['feast']) > 0:
                    f.write("" + '' + " & & " + '\\textit{Com:} ' +
                            re.sub(r'&', '\&', mdl[x]['comm3']['feast']) + "\\\\\n")
                else:
                    pass
            else:
                pass
        f.write("\end{longtable}\n\end{document}")
    f.close()
    file = 'calendar_'+str(year)+'.tex'
    working_dir = os.getcwd()
    os.chdir('output/latex/')
    subprocess.run('lualatex '+file+' -interaction nonstopmode', shell=True)
    os.chdir(working_dir)
    return 0
