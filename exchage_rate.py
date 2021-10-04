import requests

url = 'https://v6.exchangerate-api.com/v6/d4bc26a1e2c3b8da4d623a49/latest/USD'
response = requests.get(url)
data = response.json()
exchange_rate = data['conversion_rates']['KES']

print(exchange_rate)