import subprocess
from datetime import datetime
import os
import importlib
from tools.feast import Feast
from tools.helpers import latex_replacement, translate_month


def build_latex_ordo(year, mdl: dict):
    """ build an ordo booklet in 8.5 by 5.5 """
    # try:
    #     mdl = importlib.import_module('calen.calendar_' + str(year)).calen
    # except AttributeError:
    #     pass
    # else:
    mdldates = sorted(mdl)
    with open("output/latex/ordo_" + str(year) + ".tex", "a") as f:
        f.truncate(0)
        f.write(
            r'''
% !TEX program = lualatex
\documentclass[10pt, openany]{book}
\title{Ordo '''+str(year)+r'''}
\author{Roman Catholic Institute}
\usepackage{ragged2e}
\usepackage{gregoriosyms} % for the versicle and response symbols
\usepackage{microtype}
\usepackage[T1]{fontenc}
\usepackage{fontspec}
\setmainfont[
    Path = /Library/Fonts/,
    Extension = .ttf,
    Ligatures = TeX,
    BoldFont = Cardob101,
    ItalicFont = Cardoi99,
    ]{Cardo104s}
\usepackage[latin]{babel}
\usepackage{geometry}
\geometry{
    paperheight=8.5in,
    paperwidth=5.5in,
    left=1.0in,
    right=1.0in,
    top=1.0in,
    bottom=1.0in,
    }
\usepackage{anyfontsize}
\usepackage{fancyhdr}
\pagestyle{fancy}
\renewcommand{\chaptermark}[1]{%
    \markboth{#1}{}
    }
\begin{document}
    % \maketitle
    % just something temporary for now
    \begin{titlepage}
        \begin{center}
            {\fontsize{50}{60}\selectfont \textsc{Ordo '''+str(year)+r'''}}
        \end{center}
        \begin{center}
            {\footnotesize \textsc{Roman Catholic Institute}}
        \end{center}
    \end{titlepage}
    \clearpage\begingroup\pagestyle{empty}\cleardoublepage\endgroup
    '''
        )
        for i in range(1, 13):
            month = datetime.strptime(
                str(i)+'/1/'+str(year), '%m/%d/%Y').strftime('%B')
            _month = translate_month(month)
            # todo get rid of the chapter number
            f.write(
                r'''
    \chapter{''' + _month + r'''}
                    ''')
            for x in mdldates:
                if x.strftime("%m").lstrip() == str(i):
                    feast = Feast(x, mdl[x])
                    # todo make the header of the last page of the previous month match the previous month
                    f.write(
                        r'''
        \begin{center}
            \begin{minipage}{3.5in}
                \vspace{2em}
                \begin{minipage}{0.5in}
                    {\Huge '''+latex_replacement(feast.feast_date_display)+r'''} \\
                    {\normalsize '''+feast.translate_weekday+r'''} \\
                    {\normalsize '''+feast.translate_color+r'''}
                \end{minipage}
                \begin{minipage}{3.0in}
                    \textbf{ \large '''+latex_replacement(feast.name)+r''' \\
                    \textnormal{\normalsize '''+feast.rank_v+r'''}} \\ ''' + latex_replacement(feast.com_in_title)+r'''
                \end{minipage}
                \begin{justify}''' + feast.office_type2latex + 
                feast.display_matins_as_latex +
                feast.display_lauds_as_latex +
                feast.display_little_hours_as_latex +
                feast.display_prime_as_latex +
                latex_replacement(feast.display_mass_as_latex()) +
                feast.display_vespers_as_latex +
                feast.display_compline_as_latex +r'''
                \end{justify}
            \end{minipage}
        \end{center}
    ''')
            f.write("\n\end{document}")
        file = 'ordo_'+str(year)+'.tex'
        working_dir = os.getcwd()
        os.chdir('output/latex/')
        subprocess.run(
            'lualatex '+file+' -interaction nonstopmode',
            shell=True,
            # stdout=subprocess.DEVNULL
        )
        # TODO: move the pdf into a seperate directory and overwrite the old one
        os.chdir(working_dir)
    return None


