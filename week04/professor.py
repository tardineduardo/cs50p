import random
import sys


def main():

	level = get_level()

	#todo: create a for loop that will take create a string with two random ints, the solution will be a the same strings added.
	# store this in a dictionary and prompts the user in a for loop.

	questions = {}
	for i in range(10):
		a = generate_integer(level)
		b = generate_integer(level)
		questions[str(a) + " + " + str(b) + " = "] = a+b

#	for key in questions:
#		print("Key:", key)
#		print("Value:", questions[key])
#		IT WORKS!

	score = 0
	for question in questions:
		tries = 0
		while tries < 4:
			guess = input(f"{question}")
			if guess == str(questions[question]):
				score += 1
				break
			else:
				print("EEE")
				tries += 1
				if tries == 3:
					print(question + str(questions[question]))
					break
	print(f"Score: {score}")

def get_level():
	while True:
		n = input("Level: ")
		if n in ['1', '2', '3']:
			break
	return int(n)

def generate_integer(level):
	if level == 1:
		return random.randint(0, 9)
	elif level == 2:
		return random.randint(10, 99)
	elif level == 3:
		return random.randint(100, 999)
	else:
		sys.exit("ValueError")

if __name__ == "__main__":
	main()
