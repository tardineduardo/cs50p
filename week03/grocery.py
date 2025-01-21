grocery = []

while(True):
    try:
        item = input("")
        grocery.append(item.lower())
    except (EOFError):
        print()
        break

grocerynew = sorted(set(grocery))

for object in (grocerynew):
    print(f"{grocery.count(object)} {object.upper()}")
