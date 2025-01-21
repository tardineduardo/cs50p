dict = {
    "january": "01",
    "february": "02",
    "march": "03",
    "april": "04",
    "may": "05",
    "june": "06",
    "july": "07",
    "august": "08",
    "september": "09",
    "october": "10",
    "november": "11",
    "december": "12",
}

while True:
    date = input("Date: ")
    if date.count("/") == 2:
        a_type = date.split("/")
        try:
            a_month = int(a_type[0])
            a_day = int(a_type[1])
            a_year = int(a_type[2])
        except ValueError:
            pass
        else:
            if (0 < a_month < 13) and (0 < a_day < 32) and (0 <= a_year < 9999):
                if len(str(a_month)) == 1:
                    a_month = "0" + str(a_month)
                if len(str(a_day)) == 1:
                    a_day = "0" + str(a_day)

                if len(str(a_year)) == 3:
                    a_year = "0" + str(a_year)
                elif len(str(a_year)) == 2:
                    a_year = "00" + str(a_year)
                elif len(str(a_year)) == 1:
                    a_year = "000" + str(a_year)

                print(f"{a_year}-{a_month}-{a_day}")
                break

    elif date.count(",") == 1:
        b_type = date.replace(",", "").split(" ")
        try:
            b_month = dict[b_type[0].lower()]
            b_day = int(b_type[1])
            b_year = int(b_type[2])
        except (ValueError, NameError, KeyError):
            pass
        else:
            if (0 < b_day < 32) and (0 <= b_year < 9999):
                if len(str(b_day)) == 1:
                    b_day = "0" + str(b_day)

                if len(str(b_year)) == 3:
                    b_year = "0" + str(b_year)
                elif len(str(b_year)) == 2:
                    b_year = "00" + str(b_year)
                elif len(str(b_year)) == 1:
                    b_year = "000" + str(b_year)
                print(f"{b_year}-{b_month}-{b_day}")
                break


