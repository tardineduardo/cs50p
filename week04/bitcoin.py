import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    a = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("json request error.")

n = a*float(response.json()['bpi']['USD']['rate_float'])

print(f"${n:,.4f}")
