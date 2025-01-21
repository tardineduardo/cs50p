import sys

counter = 0
names = []
start = ""

while(True):
    try:
        name = input("Name: ")
        counter += 1
        names.append(name)
    except EOFError:
        break

if counter == 1:
    sentence = names[0]
elif counter == 2:
    sentence = names[0] + " and " + names[1]
else:
    for name in names[0:counter-2]:
        start += name + ', '
    sentence = start + names[counter-2] + ", and " + names[counter-1]

print(f"Adieu, adieu, to {sentence}")
