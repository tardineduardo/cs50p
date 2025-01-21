def main():
    timeinput = input("What time is it? ")
    final = convert(timeinput)
    if 7 <= final <= 8:
        print("breakfast time")
    if 12 <= final <= 13:
        print("lunch time")
    if 18 <= final <= 19:
        print("dinner time")



def convert(time):
    parts = time.split(':')
    return float(parts[0]) + (float(parts[1]) / 60)



if __name__ == "__main__":
    main()
