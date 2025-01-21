import emoji

def main():
	string = input()
	if (":)" in string):
		string = string.replace(":)", ":slightly_smiling_face:")
	if (":(" in string):
		string = string.replace(":(", ":slightly_frowning_face:")
	print(emoji.emojize(string))


main()
