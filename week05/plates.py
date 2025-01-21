def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6 or not s[0].isalpha() or not s[1].isalpha():
        return False

    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i+1].isalpha():
            return False

    for i in range(2, len(s)):
        if s[i - 1].isalpha() and s[i] == '0':
            return False

    for i in range(len(s)):
        if not s[i].isalnum():
            return False

    return True

if __name__ == "__main__":
    main()
