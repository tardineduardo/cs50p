def greetingValue(greeting: str)-> int:
	strippedGreeting = greeting.lstrip().lower()
	if strippedGreeting.startswith("hello"):
		return 0
	elif strippedGreeting.startswith("h"):
		return 20
	else:
		return 100


def main():
	greeting = input("Greeting: ")
	print(f"${greetingValue(greeting)}")


main()