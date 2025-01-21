from sys import argv
from sys import exit
import pyfiglet
import random

figlet = pyfiglet.Figlet()
fonts = figlet.getFonts()

# check for invalid command line arguments.
if len(argv) not in [1, 3]:
    exit("Error")
if (len(argv) == 3) and (argv[1] not in ["-f", "--font"] or argv[2] not in fonts):
    exit("Error")

# get user's input
a = input("Input: ")

# format and print user's input
if len(argv) == 3:
    print(pyfiglet.figlet_format(a, font=argv[2]))
if len(argv) == 1:
    print(pyfiglet.figlet_format(a, font=random.choice(fonts)))
