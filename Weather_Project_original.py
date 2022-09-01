import sys
import requests
from pprint import pprint

# Create a account and make a API key at https://openweathermap.org/
API_key = ""

city = input("Enter a city: ")

base_url = f"https://api.openweathermap.org/data/2.5/weather?lat=57&lon=-2.15&appid={API_key}&units=metric" + API_key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
