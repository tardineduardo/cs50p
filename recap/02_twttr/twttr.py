def main():
	s1 = input("Input: ")
	s2 = ""
	for c in s1:
		if not isvowel(c):
			s2 += c
	print(s2)


def isvowel(c):
	return (c in "aeiouAEIOU")


main()
