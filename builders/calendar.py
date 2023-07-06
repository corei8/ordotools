from datetime import datetime
from tools.feast import Feast
import os
import subprocess
from tools.helpers import latex_replacement


class PrintCalendar:
    def __init__(self, year: int, data: dict):
        self.year = year
        self.data = data

    @property
    def build(self) -> None:

        months = []
        for y in range(12):
            months.append([])
        for x in self.data:
            month = int(x.strftime("%m"))-1  # strftime for months starts on 1
            months[month].append(Feast(x, self.data[x]))

        with open("output/latex_calendar/calendar_"+str(self.year)+".tex", "w") as f:
            # f.truncate(0)
            f.write(r"""
% !TEX program = lualatex
\documentclass[10pt]{article}
\usepackage{letter_calendar}
\usepackage[landscape, letterpaper, margin=.25in]{geometry}
% \usepackage{palatino}
\begin{document}
\pagestyle{empty}
\setlength{\parindent}{0pt}
                    """)
            for i, month in enumerate(months):
                the_month = datetime.strptime(f"{i+1}/1/{self.year}", "%m/%d/%Y").strftime("%B")
                blank_beginning = int(month[0].date.strftime("%w"))
                blank_ending = 5-int(month[-1].date.strftime("%w"))

                lead_blanks = "&"*blank_beginning if blank_beginning != 0 else ""
                end_blanks = "&"*blank_ending+r"\\ \hline" if blank_ending != 0 else r"\\ \hline"
        

                f.write("\r")
                f.write(r'''
\begin{center}
    \textsc{\LARGE '''+the_month+r'''}\\ % Month
\end{center}
                    ''')

                f.write("\r")
                f.write(r"\latinweekdays")
                f.write("\r")

                week = ""
                f.write(r"\begin{tabularx}{\textwidth}{|X|X|X|X|X|X|X|}")
                f.write("\r")
                f.write(r"\hline")
                f.write("\r")

                for c, x in enumerate(month):

                    day_of_week = int(x.date.strftime("%w"))

                    if c == 0:
                        week += lead_blanks

                    if day_of_week < 6:
                        ender = "& "
                    else:
                        ender = r"\\ \hline"

                    if x.color == "purple":
                        color = "violet"
                    elif x.color == "green":
                        color = "ForestGreen"
                    else:
                        color = x.color

                    # background = "white"
                    # if day_of_week == 0 or day_of_week == 7:
                    #     background = "lightgray"

                    week += r"""
                        \theday{"""+str(c+1)+\
                        r"""}{"""+latex_replacement(x.name)+\
                        r"""}{"""+color+\
                        r"""}{"""+x.rank_v.split("cum")[0]+\
                        r"""}""" + ender
                        # r"""}{"""+background+\

                    if c+1 == len(month) and day_of_week != 6:
                        f.write(week+end_blanks)
                        break  # maybe not necessary
                    elif day_of_week == 6:
                        f.write(week)
                        week = ""
                    else:
                        pass
    
                f.write("\r")
                f.write(r"\end{tabularx}")
                f.write("\r")
                f.write(r"\pagebreak")
                f.write("\r")

            f.write(r"\end{document}")
        file = f"calendar_{str(self.year)}.tex"
        working_dir = os.getcwd()
        os.chdir("output/latex_calendar/")
        subprocess.run(f"lualatex {file} -interaction nonstopmode", shell=True)
        os.chdir(working_dir)
        return None
