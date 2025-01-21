import re

def main():
    ip = input("IPv4 Address: ")
    if validate(ip):
        print("True")
    else:
        print("False")


def validate(ip):
    if re.search(r"^((\d\.|[1-9]\d\.|1[0-9][0-9]\.|2([0-4][0-9]|5[0-5])\.)){3}(\d|[1-9]\d|1[0-9][0-9]|2([0-4][0-9]|5[0-5]))$", ip):
       return True
    else:
        return False


if __name__ == "__main__":
    main()
