def main():
	distances = {
		"opala": 100,
		"monza": 120,
		"parati": 45,
		"gurgel": 500,
		"fusca": 10
	}
	for name in distances.values():
		print(f"{name} is {distances[name]}")


main()
