import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
if not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")

with open(sys.argv[1], "r") as file:
    first = file.readlines()

first[0] = ("last,first,house")
for i in range(len(first)):
    first[i] = first[i].replace('"', '')
    first[i] = first[i].replace(' ', '')

second = csv.DictReader(first)

with open(sys.argv[2], 'w') as csvfile:
    newfieldnames = ['first', 'last', 'house']
    stonks = csv.DictWriter(csvfile, fieldnames=newfieldnames)

    stonks.writeheader()
    stonks.writerows(second)
    for row in second:
        stonks.writerow(row)
