
def main():
	while(True):
		string = input("Fraction: ")
		if convert(string):
			print(gauge(convert(string)))
			break

def convert(fraction):
	if '/' in fraction:
		variables = fraction.split('/')
		try:
			a = int(variables[0])
			b = int(variables[1])
		except ValueError:
			raise ValueError
		else:
			if b == 0:
				raise ZeroDivisionError
			elif (a <= b):
				return round((a/b*100))
	else:
		raise ValueError


def gauge(percentage):
	if percentage >= 99:
		return "F"
	elif percentage <= 1:
		return "E"
	else:
		return f"{percentage:.0f}%"

if __name__ == "__main__":
	main()
