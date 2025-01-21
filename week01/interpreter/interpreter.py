expression = input("Expression: ")
element = expression.split()
if element[1] == "+":
    print("{:.1f}".format(int(element[0]) + int(element[2])))
elif element[1] == "-":
    print("{:.1f}".format(int(element[0]) - int(element[2])))
elif element[1] == "*":
    print("{:.1f}".format(int(element[0]) * int(element[2])))
elif element[1] == "/":
    print("{:.1f}".format(int(element[0]) / int(element[2])))
