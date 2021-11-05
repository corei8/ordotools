import importlib
from datetime import timedelta, datetime
import re
from subprocess import run

ROMANS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV",
          "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", ]


def easter(year: int):
    firstDigit, Remain19 = year // 100, year % 19
    # // Remain19 = year % 19
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
    # // tC = (40 - firstDigit) % 4
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


def findsunday(date):  # this can be better handled with %w
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


#! this function is not necessary?
def full_year(year):
    year_list = []
    yearstart = datetime(year=year, month=1, day=1)
    while yearstart.strftime("%Y") != str(year + 1):
        year_list.append(yearstart.strftime("%m/%d"))
        yearstart += timedelta(days=1)
    return year_list


def occur(one, two):
    '''
    If one occurs on two...
    '''
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
    comparison = occur_table[one][-(two+1)]
    if comparison == 1:
        result = 1
    elif comparison == 2:
        result = 2
    elif comparison == 3:
        result = 3
    elif comparison == 4:
        result = 4
    elif comparison == 5:
        result = 5
    elif comparison == 6:
        result = 6
    elif comparison == 7:
        result = 7
    else:
        result = 8
    return result


def concur(seq, pre):
    """ Compares concurring days and determines the rule to be applied, as found in the breviary

    Args:
        seq (integer): the concurring value of the following day
        pre (integer): the concurring value of the current (previous) day

    Returns:
        integer: corresponds to the concurrance options in the breviary
    """
    concur_table = [
        [4, 0, 4, 4, 4, 4, 4, 4, 3, 3, 0],
        [2, 2, 2, 4, 4, 4, 4, 4, 5, 2, 4],
        [2, 2, 2, 4, 4, 4, 4, 4, 3, 3, 4],
        [4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4],
        [4, 4, 4, 4, 4, 4, 4, 5, 3, 1, 3],
        [4, 4, 4, 4, 4, 4, 5, 3, 3, 1, 3],
        [4, 4, 4, 4, 4, 5, 3, 3, 3, 1, 3],
        [4, 4, 4, 4, 5, 3, 3, 3, 1, 1, 3],
        [4, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3],
        [4, 0, 0, 0, 3, 3, 3, 3, 1, 1, 3],
    ]
    comparison = concur_table[seq][-(pre+1)]
    if comparison == 1:
        result = 1   # all of the following, nothing of the preceding
    elif comparison == 2:
        result = 2  # all of the preceding, nothing of the following
    elif comparison == 3:
        result = 3  # all of the following, commemoration of the preceding
    elif comparison == 4:
        result = 4  # all of the preceding, commemoration of the following
    else:
        result = 5  # all  of the more noble, commemoration of the other; in equality, a cap the following, commemoration of the preceding
    return result


def concurrance(dict):
    mdl = importlib.import_module('calen.calendar_' + str(dict)).calen
    mdlkeys = sorted(mdl)
    i = 0
    for pre in mdlkeys:
        seq = mdlkeys[i+1]
        ranker = concur(mdl[seq]['rank'][2]. mdl[pre]['rank'][3])
        print(ranker)
    return 0
# ? should we use a seperate function for the concurrnace?


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


def dict_clean(direct, dict):
    """ Gets rid of all dates in calendar which are appended with a .,
    overwrites the calendar file with the resulting dictionary.

    Args:
        direct (integer)  : the relative path to the dictionary, in format calendar/calendar_
        dict   (dictionary): year of the calendar to clean
    """
    mdl = importlib.import_module(direct + str(dict))
    i = 0
    try:
        dic = mdl.temporal
    except AttributeError:
        dic = mdl.calen
    x = sorted(dic)
    for second_ in x:
        try:
            first_ = x[i+1]
        except IndexError:
            print('\n-=+=- calendar sanitized -=+=-\n')
            break
        if first_[0:5] == second_ and len(first_) == 6:
            print(second_)
            # ranker = occur(dic[second]['rank'][1], dic[first]['rank'][0])
            if dic[second_]['rank'][1] > dic[first_]['rank'][1]:
                ranker = occur(dic[second_]['rank'][0], dic[first_]['rank'][1])
                first = first_  # higher feast
                second = second_
            else:  # ! fixme!!
                ranker = occur(dic[first_]['rank'][0], dic[second_]['rank'][1])
                second = first_
                first = second_  # higher feast
            print('\trank of the first: ' + str(dic[first]['rank'][1]))
            print('\trank of the second: ' + str(dic[second]['rank'][1]))
            if ranker == 1:
                # office of the first
                print('rule ' + str(ranker) +
                      ' : office of the first, nothing of the second')
                dic.update({first.strip('.'): dic[first]})
                del dic[second], dic[first]
            elif ranker == 2:
                # office of the second
                print('rule : office of the second, nothing of the second')
                dic.update({first.strip('.'): dic[second]})
                del dic[second], dic[first]
            elif ranker == 3:
                # commemoration of the second
                print('rule ' + str(ranker) +
                      ' : office of the first, commemoration of the second')
                dic[second].update(
                    {
                        'feast': dic[first]['feast'],
                        'rank': dic[first]['rank'],
                        'com1': dic[second]['feast']
                    }
                )  # 'target': dic[first]['target'],
                del dic[first]
            elif ranker == 4:
                # commemoration of the first
                print('rule ' + str(ranker) +
                      ' : office of the second, commemoration of the first')
                dic.update(
                    {
                        second.strip('.'): {
                            'feast': dic[first]['feast'],
                            'rank': dic[first]['rank'],
                            'com1': dic[second]['feast']
                        }
                    }
                )  # 'target': dic[second]['target'],
                del dic[first]
            elif ranker == 5:
                # translation of the second
                print('rule ' + str(ranker) +
                      ' : office of the first, translation of the second')
                dic.update({'trans' + second.strip('.'): dic[second]})
                del dic[second]
            elif ranker == 6:
                # translation of the first
                print('rule ' + str(ranker) +
                      ' : office of the second, translation of the first')
                dic.update({'trans_' + first.strip('.'): dic[first]})
                del dic[first]
            elif ranker == 7:
                # office of more noble, commemoration of the less noble
                print('rule ' + str(ranker) +
                      ' : office of the more noble, commemoration of the less noble')
                pass
            elif ranker == 8:
                # office of the more noble, translation of the less noble
                print('rule ' + str(ranker) +
                      ' : office of the more noble, translation of the less noble')
                pass
            else:
                pass
        else:
            pass
        i += 1
        # except IndexError:
        #    break
    gen_file = re.sub(r"\.", r'/', direct) + str(dict)
    with open(gen_file + ".py", "a") as f:
        f.truncate(0)
        i = 0
        for line in sorted(dic):
            if i == 0:
                f.write(re.sub(r"/(temporal|calendar)", '', gen_file) +
                        ' = {\n\'' + line + '\' : ' + str(dic[line]) + ',\n')
            else:
                f.write('\'' + line + '\' : ' + str(dic[line]) + ',\n')
            i += 1
        f.write('}')
        f.close()


def dict_clean_2(direct, dict):
    """ Second generation of dict_clean(). Gets rid of all dates in calendar which are appended with a .,
    overwrites the calendar file with the resulting dictionary.

    Args:
        direct (integer)  : the relative path to the dictionary, in format calendar/calendar_
        dict   (dictionary): year of the calendar to clean
    """
    mdl = importlib.import_module(direct + str(dict))
    # // i = 0
    try:
        dic = mdl.temporal
    except AttributeError:
        dic = mdl.calen
    x = sorted(dic)
    first_ = ''
    for i, second_ in enumerate(x):
        gtg = True
        try:
            first_ = x[i+1]  # see if a dotted date exists
        except IndexError:
            break
        if first_.strip('.') == second_ and len(first_) == 6:
            print('\nConflicting feast: ' + second_)
            if dic[second_]['rank'][0] > dic[first_]['rank'][0]:
                first, second = first_, second_
                print(
                    '\tranks: ' + str(dic[first]['rank'][0]) +
                    ' vs ' + str(dic[second]['rank'][0])
                )
            elif dic[second_]['rank'][0] == dic[first_]['rank'][0]:
                # ! nobility
                print(
                    '\tranks: ' + str(dic[first]['rank'][0]) +
                    ' vs ' + str(dic[second]['rank'][0])
                )
                gtg = False  # for testing only
                pass
            else:
                first, second = second_, first_
                print(
                    '\tranks: ' + str(dic[first]['rank'][0]) +
                    ' vs ' + str(dic[second]['rank'][0])
                )                
            if gtg == True:
                if dic[first]['rank'][0] <= 4 and dic[second]['rank'][0] <= 10:
                    # there is no commemoration, but a tranlsation
                    dic.update({first.strip('.'): dic[first]})
                    dic.update({'trans ' + second.strip('.'): dic[second]})
                elif dic[first]['rank'][0] <= 4 and dic[second]['rank'][0] > 10:
                    # no commemoration because of solemnity
                    dic.update(
                        {first.strip('.'): dic[first]})
                elif dic[first]['rank'][0] > 4 and dic[second]['rank'][0] >= 6:
                    # there is a commemoration
                    dic[first].update({'com1': dic[second]['feast']})
                    dic.update({first.strip('.'): dic[first]})
                else:
                    # no commemoration because of lack of solemnity
                    dic.update(
                        {first.strip('.'): dic[first]})
                # get rid of the dotted dates
                if len(first) == 6:
                    dic.pop(first)
                if len(second) == 6:
                    dic.pop(second)
            else:
                pass
        else:
            pass
        # // i += 1
    # // gen_file = re.sub(r"\.", r'/', direct) + str(dict)
    with open(re.sub(r"\.", r'/', direct) + str(dict) + ".py", "a") as f:
        f.truncate(0)
        i = 0
        for i, line in enumerate(sorted(dic)):
            if i == 0:
                f.write(re.sub(r"/(temporal|calendar)", '', re.sub(r"\.", r'/', direct) + str(dict)) +
                        ' = {\n\'' + line + '\' : ' + str(dic[line]) + ',\n')
            else:
                f.write('\'' + line + '\' : ' + str(dic[line]) + ',\n')
            # // i += 1
        f.write('}')
        f.close()


def stitch(t, s):
    mdltemporal = importlib.import_module(
        'temporal.temporal_' + str(t)).temporal
    mdlsanctoral = importlib.import_module('sanctoral.' + s).sanctoral
    mdlt, mdls = sorted(mdltemporal), sorted(mdlsanctoral)
    calen = {}
    for feast in mdls:
        if feast in mdlt:
            calen.update({feast+'.': mdlsanctoral[feast]})
        else:
            calen.update({feast: mdlsanctoral[feast]})
    for feast in mdlt:
        calen.update({feast: mdltemporal[feast]})
    with open("calen/calendar_" + str(t) + ".py", "w") as f:
        f.truncate(0)
        i = 0
        for line in sorted(calen):
            if i == 0:
                f.write('calen = {\n\'' + line +
                        '\' : ' + str(calen[line]) + ',\n')
            else:
                f.write('\'' + line + '\' : ' + str(calen[line]) + ',\n')
            i += 1
        f.write('}')
    f.close()
    print('calendar stitched and written.')

    return 0


def latex_full_cal_test(year):
    mdl = importlib.import_module(
        'calen.calendar_' + str(year)).calen
    mdldates = sorted(mdl)
    with open("output/latex/calendar_" + str(year) + ".tex", "a") as f:
        f.truncate(0)
        f.write(
            r"""
% !TEX program = lualatex
\documentclass{article}
\title{Ordo -- Full Calendar -- 2022}
\usepackage{longtable}
\usepackage{geometry}
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
            f.write("" + x + ', ' + datetime.strptime(x.strip('.') + '/' + str(year), '%m/%d/%Y').strftime('%a') + " & " + mdl[x]['rank'][-1] +
                    " & " + re.sub(r'&', '\&', mdl[x]['feast']) + "\\\\\n")
            try:
                f.write("" + '' + " & & " + 'Commemorate: ' +
                        re.sub(r'&', '\&', mdl[x]['com1']) + "\\\\\n")
            except KeyError:
                pass
        f.write("\end{longtable}\n\end{document}")
    f.close()
    # produce the pdf from the tex file:
    # run('cd output/latex', shell=True)
    # run('lualatex temporal_' + str(year) + '.tex', shell=True)
    return 0
