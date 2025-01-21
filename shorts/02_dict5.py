# ------> dict1.items() ----->NAO ENTENDI NADA DESSE ITEMS


WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}


def main():
	print("Welcome to the Spelling Bee!")
	for word, points in WORDS.items():
		print(f"{word} was worth {points} points")


main()
