def main():
	spacecraft = {"name": "James Webb Space Telescope"}
	spacecraft["distance"] = 500
	print(create_report(spacecraft))

def create_report(spacecraft):
	return f"""
	========= REPORT ========

	Name: {spacecraft["name"]}
	Distance: {spacecraft.get("distance")} km

	=========================
	"""

main()
