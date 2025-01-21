import sys
import csv
import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

with open(sys.argv[1], "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

print(tabulate.tabulate(data, "keys", tablefmt="grid"))




#with open(sys.argv[1], "r") as file:
#   reader = csv.DictReader(file)
#    for row in reader:
#        print(row)
#    print(tabulate.tabulate(reader, tablefmt="grid"))
