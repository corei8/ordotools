import subprocess
from datetime import datetime
import os
import importlib
from ordo_tools.ordo_tools import latex_replacement, Feast


def readme_calendar(year):
    mdl = importlib.import_module(
        'calen.calendar_' + str(year)).calen
    mdldates = sorted(mdl)
    with open('README.md', 'a') as f:
        f.truncate(0)
        f.write(
            r'''
# Ordo

Pre-Vatican II Roman Catholic Ordo with proper readings indicated for the Divine Office and the Mass.

## Python Specifications

Python 3.x.x 64-bit

### Modules:

dateutil

## Overview

The temporal cycle is generated by a funtion as a dictionary. The sanctoral cycle is made up of several files for country, region and diocese, and each file is a pre-built dictionary. These are combined with the temporal cycle after the latter is generated.

The result is a dictionary containing:

1. A liturgical calendar proper to an specified diocese (or several dioceses);
2. Indications of the peculiarities of the office of that day;
3. An ordo for the Mass of that day, or multiple Masses, if applicable.

Easter is the first feast (every 'event' is treated as a feast) to be determined, since most of the liturgical year depends upon the date of Easter. Christmas, being static with regard to its date, requires that we only find the day of the week on which it falls. We begin building the temporal calendar with 01-01.

## Progress

- [x] Temporal Calendar
- [ ] Combined Temporal and Sanctoral Calendar
- [ ] Masses
- [ ] Vespers
- [ ] Colors of Mass and Office
- [ ] Lessons for Laudes
- [ ] Prime
- [ ] Little Hours
- [ ] Solemnities
- [ ] Australian Calendar
- [ ] Canadian Calendar
                ''')
        f.write('\n\n')
        f.write('## Calendar for ' + str(year))
        f.write('\n\n')
        f.write('| Day | Date | Rank | Feast |')
        f.write('\n')
        f.write('|---|---|---|---|')
        f.write('\n')
        for x in mdldates:
            dow = datetime.strptime(
                x.strip('tranlsated ._')+'/'+str(year), '%m/%d/%Y').strftime('%a')
            if len(x) <= 6:
                f.write('| '+dow+' | '+latex_replacement(x)+' | ' +
                        mdl[x]['rank'][-1]+' | '+latex_replacement(mdl[x]['feast'])+' | ')
                f.write('\n')
            else:
                f.write('| '+dow+' | '+latex_replacement(x) + ' | ' +
                        mdl[x]['rank'][-1] + " | " + latex_replacement(mdl[x]['feast']) + ' | ')
                f.write('\n')
            # todo find a solution for labeling commemorations
            if 'com_1' in mdl[x].keys():
                f.write(" | | | | " + '*Com:* ' +
                        latex_replacement(mdl[x]['com_1']) + ' | ')
                f.write('\n')
            else:
                pass
            if 'com_2' in mdl[x].keys():
                if len(mdl[x]['com_2']['feast']) > 0:
                    f.write(" | | | | " + '*Com:* ' +
                            latex_replacement(mdl[x]['com_2']['feast']) + ' | ')
                    f.write('\n')
                else:
                    pass
            else:
                pass
            if 'com_3' in mdl[x].keys():
                if len(mdl[x]['com_3']['feast']) > 0:
                    f.write(" | | | | " + '*Com:* ' +
                            latex_replacement(mdl[x]['com_3']['feast']) + ' | ')
                    f.write('\n')
                else:
                    pass
            else:
                pass


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
            if 'com_1' in mdl[x].keys():
                f.write("" + '' + " & & & " + '\\textit{Com:} ' +
                        latex_replacement(mdl[x]['com_1']) + "\\\\\n")
            else:
                pass
            if 'com_2' in mdl[x].keys():
                if len(mdl[x]['com_2']['feast']) > 0:
                    f.write("" + '' + " & & & " + '\\textit{Com:} ' +
                            latex_replacement(mdl[x]['com_2']['feast']) + "\\\\\n")
                else:
                    pass
            else:
                pass
            if 'com_3' in mdl[x].keys():
                if len(mdl[x]['com_3']['feast']) > 0:
                    f.write("" + '' + " & & & " + '\\textit{Com:} ' +
                            latex_replacement(mdl[x]['com_3']['feast']) + "\\\\\n")
                else:
                    pass
            else:
                pass
        f.write("\end{longtable}\n\end{document}")
    file = 'calendar_'+str(year)+'.tex'
    working_dir = os.getcwd()
    os.chdir('output/latex/')
    subprocess.run('lualatex '+file+' -interaction nonstopmode',
                   shell=True, stdout=subprocess.DEVNULL)
    os.chdir(working_dir)
    return 0


def build_latin_calendar(year) -> None:
    # todo make this calendar import work with a variable
    mdl = importlib.import_module(
        'calen.calendar_' + str(year)).calen
    mdldates = sorted(mdl)
    with open('output/latex_calendar/calendar_'+str(year)+'.tex', 'a') as f:
        f.truncate(0)
        f.write(
            r"""
% !TEX program = lualatex
\documentclass[10pt]{article}
\usepackage{calendar_letter}
\usepackage[landscape, letterpaper, margin=.25in]{geometry}
\usepackage{palatino}
\begin{document}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\StartingDayNumber=1
"""
        )
        for i in range(1, 13):
            blank_days = datetime.strptime(
                str(i)+'/1/'+str(year), '%m/%d/%Y').strftime('%w')
            month = datetime.strptime(
                str(i)+'/1/'+str(year), '%m/%d/%Y').strftime('%B')
            f.write(
                r'''
\begin{center}
    \textsc{\LARGE '''+month+r'''}\\ % Month
    % \textsc{\large Year} \\ % Year
\end{center}
\begin{calendar}{\textwidth}
'''
            )
            for x in range(int(blank_days)):
                f.write(
                    r'''
\BlankDay
'''
                )
            f.write(r'''
\setcounter{calendardate}{1}
'''
                    )
            for x in mdldates:
                if int(x.split('/')[0]) == i:
                    feast = Feast(x, mdl[x])
                    f.write(
                        r'''
\day{'''+latex_replacement(feast.name)+r'''}{\vspace{1.5cm}}
'''
                    )
            f.write(
                r'''
\finishCalendar
\end{calendar}
\pagebreak
'''
            )
        f.write(
            r'''
\end{document}
            '''
        )
    file = 'calendar_'+str(year)+'.tex'
    working_dir = os.getcwd()
    os.chdir('output/latex_calendar/')
    subprocess.run('lualatex '+file+' -interaction nonstopmode', shell=True)
    os.chdir(working_dir)
    return None


def build_latex_ordo(year):
    # todo make this calendar import work with a variable
    mdl = importlib.import_module(
        'calen.calendar_' + str(year)).calen
    mdldates = sorted(mdl)
    with open("output/latex/ordo_" + str(year) + ".tex", "a") as f:
        f.truncate(0)
        f.write(
            r'''
% !TEX program = lualatex
\documentclass[10pt]{memoir}
\title{Ordo 2022}
%\usepackage{tabularx}
%\tracingtabularx
\usepackage{ragged2e}
\usepackage{geometry}
\usepackage[letterspace=1000]{microtype}
\usepackage[T1]{fontenc}
%\usepackage[usefilenames,RMstyle={Text,Semibold},SSstyle={Text,Semibold},TTstyle={Text,Semibold},DefaultFeatures={Ligatures=Common}]{plex-otf} %
% \usepackage{librecaslon}
% \usepackage{tgpagella}
\usepackage{fontspec}
\setmainfont[Path = /Library/Fonts/, Extension = .ttf, Ligatures = TeX, BoldFont = Cardob101, ItalicFont = Cardoi99,]{Cardo104s}
\usepackage[latin]{babel}
\setlength{\columnseprule}{0.4pt}
\geometry{paperwidth=8.5in, paperwidth=5.5in, left=1.0in, right=1.0in, top=1.0in, bottom=1.0in,}
\usepackage{fancyhdr}
\begin{document}
\pagestyle{fancy}
\thispagestyle{empty}
\begin{center}
\begin{minipage}[c][3in][c]{3.5in}
\begin{center}
{\HUGE \lsstyle ORDO}\\
\vspace{0.2in}
{\lsstyle \LARGE ''' + str(year) + r'''}
\end{center}
\end{minipage}
\begin{minipage}[b][][b]{3.5in}
\begin{center}
\vspace*{4.5in}
\textsc{\normalsize Roman Catholic Institute}
\end{center}
\end{minipage}
\end{center}
\pagebreak
\clearpage
\pagenumbering{arabic}
'''
                )
        for x in mdldates:
            feast = Feast(x, mdl[x])
            # todo #6 make the latin day of the week using FERIAS in temporal_cycle.py
            # todo use tables for the ordo parts to prevent breaking across pages
            f.write('\n')
            f.write('\\begin{minipage}{3.5in}\n')
            f.write('\\vspace{2em}')
            f.write('\\begin{center}\n')
            f.write(latex_replacement(feast.feast_date_display) + '\n')
            f.write('\\end{center}')
            f.write('\\textbf{ \\large ' + latex_replacement(feast.name) +
                    ', \\textnormal{\\normalsize ' + feast.rank_v + '}}')
            f.write(latex_replacement(feast.commemoration2latex()))
            f.write('\\begin{justify}\n')
            f.write(feast.office_type2latex)
            f.write('\n')
            f.write('\\textbf{Ad Mat: }')
            f.write('\n')
            f.write('\\textbf{Ad Lau: }')
            f.write('\n')
            f.write('\\textbf{Ad Horas: }')
            f.write(feast.preces)
            f.write('\n')
            f.write('\\textbf{Ad Primam: }')
            f.write(feast.preces)
            f.write('\n')
            f.write(feast.display_mass_as_latex())
            f.write('\n')
            f.write('\\textbf{In Vesp: }')
            f.write('\n')
            f.write('\\textbf{Ad Compl: }')
            f.write(feast.preces)
            f.write('\\end{justify}\n')
            f.write('\\end{minipage}\n')
            f.write('\n\n')
            # todo find a solution for labeling the commemorations
        f.write("\n\end{document}")
    file = 'ordo_'+str(year)+'.tex'
    working_dir = os.getcwd()
    os.chdir('output/latex/')
    subprocess.run('lualatex '+file+' -interaction nonstopmode',
                   shell=True)
    os.chdir(working_dir)
    return 0
