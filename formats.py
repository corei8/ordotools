import sys
from datetime import datetime
from datetime import timedelta

#! this function is not useable as is
def htmlify(gen_file, year, cycle):
	original_stdout = sys.stdout
	with open(gen_file + ".html", "w") as f:
    		sys.stdout = f
        print(
            """
        <!DOCTYPE html>
        <html lang='en'>
        <head>
            <meta charset='UTF-8'>
            <meta http-equiv='X-UA-Compatible' content='IE=edge'>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <title>"""
            + str(year)
            + """ Ordo</title>
            <style>
                .styled-table {
                    border-collapse: collapse;
                    margin: 25px 0;
                    font-size: 0.9em;
                    font-family: sans-serif;
                    min-width: 400px;
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
                }
                .styled-table thead tr {
                    background-color: #009879;
                    color: #ffffff;
                    text-align: left;
                }
                .styled-table tbody tr {
                    border-bottom: 1px solid #dddddd;
                }

                .styled-table tbody tr:nth-of-type(even) {
                    background-color: #f3f3f3;
                }

                .styled-table tbody tr:last-of-type {
                    border-bottom: 2px solid #009879;
                }
                .styled-table tbody tr.active-row {
                    font-weight: bold;
                    color: #009879;
                }
            </style>
        </head>
        <body>
        <table class="styled-table">
        """
        )
        print("<tr><th>Feast</th><th>Rank</th><th>Weekday</th><th>Date</th></tr>")
        for row in cycle:
            print("<tr>")
            print(
                "<td>"
                + row[0]
                + "</td><td>"
                + row[1]
                + "</td><td>"
                + str(row[2])
                + "</td>"
            )
            print("</tr>")
        print("</table></body></html>")
    	sys.stdout = original_stdout