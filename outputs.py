import subprocess
from datetime import datetime
import os
import importlib
from functions import latex_replacement


def readme_calendar(year):
    print('rendering README.md...')
    mdl = importlib.import_module(
        'calen.calendar_' + str(year)).calen
    mdldates = sorted(mdl)
    with open('README.md', 'a') as f:
        f.write('\n\n')
        f.write('| Day | Date | Rank | Feast |')
        f.write('|---|---|---|---|')
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
            if 'com1' in mdl[x].keys():
                f.write(" | | | | " + '\\textit{Com:} ' +
                        latex_replacement(mdl[x]['com1']) + ' | ')
                f.write('\n')
            else:
                pass
            if 'comm2' in mdl[x].keys():
                if len(mdl[x]['comm2']['feast']) > 0:
                    f.write(" | | | | " + '\\textit{Com:} ' +
                            latex_replacement(mdl[x]['comm2']['feast']) + ' | ')
                    f.write('\n')
                else:
                    pass
            else:
                pass
            if 'comm3' in mdl[x].keys():
                if len(mdl[x]['comm3']['feast']) > 0:
                    f.write(" | | | | " + '\\textit{Com:} ' +
                            latex_replacement(mdl[x]['comm3']['feast']) + ' | ')
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
