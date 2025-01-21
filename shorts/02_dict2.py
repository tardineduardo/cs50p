# ------> dict1.update(dict2)
# ------> dict1.get("key", "None")

def main():
	spacecraft = {"name": "James Webb Space Telescope"}
	spacecraft.update({"distance": 400, "orbit": "sun"})
	print(create_report(spacecraft))

	spacecraft.update({"name": "GAYYYY", "distance": 0})
	print(create_report(spacecraft))

def create_report(spacecraft):
	return f"""
	========= REPORT ========

	Name:\t{spacecraft["name"]}
	Distance:\t{spacecraft.get("distance")} km
	Orbit:\t{spacecraft.get("orbit")} km

	=========================
	"""

main()
