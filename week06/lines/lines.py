import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

count = 0
with open(sys.argv[1], "r") as file:
    lines = file.readlines()
    for line in lines:
        a = line.strip()
        if a and a[0] != '#':
            count += 1
print(count)
