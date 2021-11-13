from datetime import timedelta, datetime
import dateutil.easter
import importlib
import os
import re
import subprocess


ROMANS = ["I", "II", "III", "IV", "V", "VI", "VII",
          "VIII", "IX", "X", "XI", "XII", "XIII",
          "XIV", "XV", "XVI", "XVII", "XVIII", "XIX",
          "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV",
          "XXVI", "XXVII", "XXVIII", ]


class Feast:
    def __init__(self, feast_date: str, properties: dict):
        self.date = feast_date
        self.properties = properties

    def date(self):
        return datetime.strptime('%m%d', self.feast_date)

    def feast(self):
        return self.properties['feast']

    def rank(self, visual: bool):
        if visual == True:
            return self.properties['rank'][-1]
        else:
            return self.propertes['rank'][0]

    def to_dictionary(self):
        return self.properties


def easter(year: int):
    x = dateutil.easter.easter(year)
    return datetime(year=int(x.strftime('%Y')), month=int(x.strftime('%m')), day=int(x.strftime('%d')))


def day(year: int, month: int, day: int):
    x = datetime(year=year, month=month, day=day)
    return x


def week(i: int):
    return timedelta(weeks=i)


def indays(numdays: int):
    return timedelta(days=numdays)


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


def latex_replacement(string: str):
    clean_string = re.sub('&', '\&', re.sub('_', '\_', string))
    return clean_string


def nobility_solver(second, first):
    """ determintes the more noble feast from a tuple of 6 digits

    Args:
        second  (tuple): second feast date and ranking tuple
        first   (tuple): first feast date and ranking tuple

    Returns:
        tuple: feast dates in increasing nobility
    """
    for x, y in zip(second[1], first[1]):
        if x == y:
            continue
        else:
            if bool(x) != bool(y):
                if bool(x) == True:
                    return (first[0], second[0],)
            elif x < y:
                return (first[0], second[0],)
            else:
                return (second[0], first[0],)


def dict_clean(direct: str, dict: int):
    """ Gets rid of all dates in calendar which are appended with . or _;
    overwrites the calendar file with the resulting dictionary.

    Args:
        direct (integer)   : the relative path to the dictionary, 
                             in format calendar/calendar_
        dict   (dictionary): year of the calendar to clean
    """
    mdl = importlib.import_module(direct + str(dict))
    try:
        dic = mdl.temporal
    except AttributeError:
        dic = mdl.calen
    for second_ in sorted(dic):
        nobility_free = True
        if len(second_) >= 6:
            continue
        else:
            if not second_+'.' in sorted(dic):
                continue
            else:
                first_ = second_+'.'
                if dic[second_]['rank'][0] > dic[first_]['rank'][0]:
                    first, second = first_, second_
                elif dic[second_]['rank'][0] == dic[first_]['rank'][0]:
                    # * solve the nobility issue here
                    less_noble = nobility_solver(
                        (second_, dic[second_]['nobility'],),
                        (first_, dic[first_]['nobility'],)
                    )[0]
                    more_noble = nobility_solver(
                        (second_, dic[second_]['nobility'],),
                        (first_, dic[first_]['nobility'],)
                    )[1]
                    rank = dic[second_]['rank'][0]
                    if rank <= 10:  # ! refind this to exclude all but D1 and D2
                        dic.update({more_noble.strip('.'): dic[more_noble]})
                        dic.update(
                            {less_noble.strip('.')+' tranlsated': dic[less_noble]})
                    else:
                        dic[more_noble].update(
                            {'com1': dic[less_noble]['feast']})
                        dic.update({first.strip('.'): dic[more_noble]})
                    if len(more_noble) == 6:
                        dic.pop(more_noble)
                    if len(less_noble) == 6:
                        dic.pop(less_noble)
                    nobility_free = False
                    pass
                else:
                    first, second = second_, first_
                if nobility_free == False:
                    pass
                else:
                    # tranlsation
                    if dic[first]['rank'][0] <= 4 and dic[second]['rank'][0] <= 10:
                        dic.update({first.strip('.'): dic[first]})
                        dic.update({second.strip('.')+'_': dic[second]})
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
                f.write(re.sub(r"/(temporal|calendar)", '', re.sub(r"\.", r'/', direct)+str(dict))
                        + ' = {\n\''+line+'\': '+str(dic[line])+',\n')
            else:
                f.write('\''+line+'\' : '+str(dic[line])+',\n')
        f.write('}')
        return 0


def stitch(year: int, s: str):
    mdl_temporal = importlib.import_module(
        'temporal.temporal_' + str(year)).temporal
    mdl_sanctoral = importlib.import_module('sanctoral.' + s).sanctoral
    mdlt, mdls = sorted(mdl_temporal), sorted(mdl_sanctoral)
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
    calen = {}
    for feast in mdls:
        calen.update(
            {feast + '.' if feast in mdlt else feast: mdl_sanctoral[feast]}
        )
    for feast in mdlt:
        calen.update({feast: mdl_temporal[feast]})
    with open("calen/calendar_" + str(year) + ".py", "w") as f:
        f.truncate(0)
        for i, line in enumerate(sorted(calen)):
            if i == 0:
                f.write('calen = {\n\''+line+'\': '+str(calen[line])+',\n')
            else:
                f.write('\''+line+'\':'+str(calen[line])+',\n')
        f.write('}')
    return 0


def latex_full_cal_test(year):
    # todo make this calendar import work with a variable
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
\begin{enumerate}
    \item Ignore dates with a period or an underscore after the day -- these are being worked on.
    \item Check only that the commemorations are present and are spelt correctly.
    \item Check for consistency in ranks and feast naming.
\end{enumerate}
\rowcolors{1}{}{lightblue}
\begin{longtable}{ l l l l }
\hline
\textsc{Day} & \textsc{Date} & \textsc{Rank} & \textsc{Feast} \\
\hline
\endhead
"""
        )
        for x in mdldates:
            dow = datetime.strptime(
                x.strip('tranlsated ._')+'/'+str(year), '%m/%d/%Y'
            ).strftime('%a')
            if len(x) <= 6:
                f.write(""+dow+' & '+latex_replacement(x) + " & " + mdl[x]['rank'][-1] +
                        " & "+latex_replacement(mdl[x]['feast'])+"\\\\\n")
            else:
                f.write(""+dow+' & '+latex_replacement(x) + " & " + mdl[x]['rank'][-1] +
                        " & " + latex_replacement(mdl[x]['feast']) + "\\\\\n")
            # todo find a solution for labeling commemorations
            if 'com1' in mdl[x].keys():
                f.write("" + '' + " & & & " + '\\textit{Com:} ' +
                        latex_replacement(mdl[x]['com1']) + "\\\\\n")
            else:
                pass
            if 'comm2' in mdl[x].keys():
                if len(mdl[x]['comm2']['feast']) > 0:
                    f.write("" + '' + " & & & " + '\\textit{Com:} ' +
                            latex_replacement(mdl[x]['comm2']['feast']) + "\\\\\n")
                else:
                    pass
            else:
                pass
            if 'comm3' in mdl[x].keys():
                if len(mdl[x]['comm3']['feast']) > 0:
                    f.write("" + '' + " & & & " + '\\textit{Com:} ' +
                            latex_replacement(mdl[x]['comm3']['feast']) + "\\\\\n")
                else:
                    pass
            else:
                pass
        f.write("\end{longtable}\n\end{document}")
    file = 'calendar_'+str(year)+'.tex'
    working_dir = os.getcwd()
    os.chdir('output/latex/')
    print('compiling PDF...')
    subprocess.run('lualatex '+file+' -interaction nonstopmode',
                   shell=True, stdout=subprocess.DEVNULL)
    print('PDF complete!')
    os.chdir(working_dir)
    return 0
