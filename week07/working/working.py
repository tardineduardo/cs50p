import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches := re.search(r"^([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM) to ([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM).*", s):
        h2 = matches.group(2) # minutes1
        h5 = matches.group(5) # minutes2
        h3 = matches.group(3) # meridien1
        h6 = matches.group(6) # meridien2
        h1 = adjust_hour(int(matches.group(1)), h3) # hour1
        h4 = adjust_hour(int(matches.group(4)), h6) # hour2

    try:
        if ":" in s:            # input has format '2:00 AM'
            return h1 + h2 + " to " + h4 + h5
        else:                   # input has format '2 AM'
            return h1 + ":00" + " to " + h4 + ":00"
    except UnboundLocalError:
        raise ValueError()      # if parsing fails, 'convert' should raise 'ValueError'

# adjusting hour from 12h to 24h
def adjust_hour(hour, meridiem):
    if meridiem == "AM" and hour < 10:
        return (f"{hour:02}")
    elif meridiem == "PM" and hour != 12:
        return (f"{(hour + 12):02}")
    elif meridiem == "AM" and hour == 12:
        return "00"
    else:
        return str(hour)

if __name__ == "__main__":
    main()
