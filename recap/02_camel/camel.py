def main():
	camel = input("camelCase: ")
	new = ""
	for c in camel:
		if c.isupper():
			new += ("_" + c.lower())
		else:
			new += c
	print(new)


main()


# def main():
#     camel = input("camelCase: ")
#     new = ''.join(['_' + c.lower() if c.isupper() else c for c in camel])
#     print(new)


# main()
