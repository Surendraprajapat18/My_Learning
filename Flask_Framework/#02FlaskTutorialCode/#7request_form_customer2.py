import requests
r = requests.get("https://financialmodelingprep.com/api/v3/actives")
print(r.text)