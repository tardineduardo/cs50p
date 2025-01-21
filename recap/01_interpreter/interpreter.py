def sum(a, b) -> float:
	return float(int(a) + int(b))

def sub(a, b) -> float:
	return float(int(a) - int(b))

def mul(a, b) -> float:
	return float(int(a) * int(b))

def div(a, b) -> float:
	return float(int(a) / int(b))

def main():
	math = input("Expression: ")
	expression = math.split(" ")
	if len(expression) != 3:
		return
	if (expression[1] == "+"):
		print(f"{sum(expression[0], expression[2]):.1f}")
	if (expression[1] == "-"):
		print(f"{sub(expression[0], expression[2]):.1f}")
	if (expression[1] == "*"):
		print(f"{mul(expression[0], expression[2]):.1f}")
	if (expression[1] == "/"):
		print(f"{div(expression[0], expression[2]):.1f}")


main()