import requests
import sys
import jsons
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
try:
    r = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=78c571ae39d6dcf6a68c9cf9d07371c497d884800e86262f25af6800f02cb164')
    p = r.json()
    i = p["data"]['priceUsd']
    price = float(i)
except requests.RequestException:
    sys.exit()
total = price * n
print(f"${total:,.4f}")


