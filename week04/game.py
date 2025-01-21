import random
import sys

while(True):
    n = input("Level: ")
    try:
        level = int(n)
    except ValueError:
        continue
    if level > 0:
        break

secret = random.randint(1, level)


while (True):
    m = input("Guess: ")
    try:
        guess = int(m)
    except ValueError:
        continue
    if guess <= 0:
        continue

    if secret < guess:
        print("Too large!")
        continue
    elif secret > guess:
        print("Too small!")
        continue
    else:
        print("Just right!")
        break

