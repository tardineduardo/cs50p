camelCase = input("camelCase: ")
snake_case = ""

for i in camelCase:
    if i.isupper():
        print('_', end="")
        print(i.lower(), end="")
    elif i.islower():
        print(i, end="")
print()
