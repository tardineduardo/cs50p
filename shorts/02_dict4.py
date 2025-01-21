# ------> len(dict1) = int
# ------> dict1.keys() = listofkeys
# ------> dict1.pop(key) = value
# ------> dict1.clear() (= void)


# len is a builtin function, not a method


WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}


def main():
	print("Welcome to the Spelling Bee!")
	print("Your letters are: A I P C R H G")
	totalPoints = 0;
	while len(WORDS) > 0:
		print(f"{len(WORDS)} left!")
		guess = input("Guess a word: ")
		if guess == "GRAPHIC":
			WORDS.clear()
			totalPoints = 100;
			print("You've guessed the special word!")
		if guess in WORDS.keys():
			points = WORDS.pop(guess)
			totalPoints += points
			print(f"Good! You scored {points} points.")
	print(f"\nTotal points: {totalPoints}")
	print("That's the game!")


main()
