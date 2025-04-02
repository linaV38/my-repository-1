import requests

url = "https://api.binance.com/api/v3/ticker/price"

response = requests.get(url, params={"symbol": "BITCUSDT"})

content = response.content

price = response.json()
print(price)
print(type(price))