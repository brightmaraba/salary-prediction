import os
import requests
from dotenv import load_dotenv

load_dotenv()

def convert(amount):
    url = os.getenv("URL")
    response = requests.get(url)
    data = response.json()
    exchange_rate = data['conversion_rates']['KES']
    return amount * exchange_rate