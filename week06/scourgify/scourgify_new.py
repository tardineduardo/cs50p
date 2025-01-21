#This is not my code. After I completed and submitted the exercise,
#I asked AI how my code could be improved and simplified.

import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Usage: python script.py input.csv output.csv")

input_file = sys.argv[1]
output_file = sys.argv[2]

if not (input_file.endswith(".csv") and output_file.endswith(".csv")):
    sys.exit("Both input and output files must be CSV files")

with open(input_file, "r", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

for row in rows:
    row["name"] = row["name"].strip('"')

for row in rows:
    row["first"], row["last"] = row["name"].split(", ")
    del row["name"]

fieldnames = ["first", "last", "house"]

with open(output_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
