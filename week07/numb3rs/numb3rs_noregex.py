import re
import sys


def main():
    ip = input("IPv4 Address: ")
    if validate(ip):
        print("True")
    else:
        print("False")


def validate(ip):
    try:
        x1, x2, x3, x4 = ip.split('.')
    except ValueError:
        return False
    else:
        try:
            a1 = int(x1)
            a2 = int(x2)
            a3 = int(x3)
            a4 = int(x4)
        except ValueError:
            return False
        else:
            if (0 <= a1 <= 255) and (0 <= a2 <= 255) and (0 <= a3 <= 255) and (0 <= a4 <= 255):
                return True
            else:
                return False


if __name__ == "__main__":
    main()
