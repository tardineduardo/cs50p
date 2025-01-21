import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches1 = re.findall(r"\bum\b", s, flags=re.IGNORECASE)
    return(len(matches1))


if __name__ == "__main__":
    main()
