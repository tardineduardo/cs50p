while(True):
    string = input("Fraction: ")
    if '/' in string:
        variables = string.split('/')
        try:
            a = int(variables[0])
            b = int(variables[1])
        except (ValueError, ZeroDivisionError):
            pass
        else:
		if (a <= b):
                if (a/b*100 >= 99):
                    print("F")
                    break
                elif (a/b*100 <= 1):
                    print("E")
                    break
                else:
					print(f"{a/b*100:.0f}%")
					break
