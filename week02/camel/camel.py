# this is not mine, this is from chatgpt

camelCase = input("camelCase: ")
snake_case = ""

for i in camelCase:
    if i.isupper():
        snake_case += '_'
        snake_case += i.lower()
    elif i.islower():
        snake_case += i

print(snake_case)
