def iscorrect(answer):
	if answer.strip(" ") == "42":
		return True
	if answer.lower() == "forty two":
		return True
	if answer.lower() == "forty-two":
		return True
	return False


def main():
	answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
	if iscorrect(answer):
		print("Yes")
	else:
		print("No")


main()