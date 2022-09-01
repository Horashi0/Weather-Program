from pprint import pprint
import datetime as dt
import requests

# Create a account and make a API key at https://openweathermap.org/
API_key = ""

# temperature conversion


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return round(celsius)

# ip grabber


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data


# Choice, the information displayed on screen
choice = input(
    "Hello would you like to input your location automatically?(1) or manually(2) ")
# Automatically gets weather
if choice.lower() == "1":
    city = get_location()["city"]
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=57&lon=-2.15&appid={API_key}&units=metric" + \
        API_key+"&q="+city
    # all of my units and conversions needed
    weather_data = requests.get(url).json()
    temp_kelvin = weather_data["main"]["temp"]
    temp_kelvin_feels_like = weather_data["main"]["feels_like"]
    temp_celsius = kelvin_to_celsius(temp_kelvin)
    temp_celsius_feels_like = kelvin_to_celsius(temp_kelvin_feels_like)
    sunrise_time = dt.datetime.utcfromtimestamp(
        weather_data["sys"]["sunrise"] + weather_data["timezone"])
    sunset_time = dt.datetime.utcfromtimestamp(
        weather_data["sys"]["sunset"] + weather_data["timezone"])
    clouds = weather_data["weather"][0]["description"]
    wind_speed = weather_data["wind"]["speed"]
    wind_degrees = weather_data["wind"]["deg"]
    place = weather_data["name"]
    identification = weather_data["id"]
    timezone = weather_data["timezone"]
    humidity = weather_data["main"]["humidity"]
    time_id = dt.datetime.utcfromtimestamp(
        weather_data["dt"] + weather_data["timezone"])
    # prints the displayed information on screen
    print(f"")
    print(f"Temperature in {city}: {temp_celsius}°C")
    print(f"Temperature in {city} feels like: {temp_celsius_feels_like}°C")
    print(f"Humidity in {city}: {humidity}%")
    print(f"Wind speed in {city}: {wind_speed}m/s")
    print(f"Wind direction in {city}: {wind_degrees}°")
    print(f"General Weather in {city}: {clouds}")
    print(f"Sun rises in {city} at {sunrise_time} local time")
    print(f"Sun sets in {city} at {sunset_time} local")
# Manually enter city
if choice.lower() == "2":
    # city = info displayed on screen where the user enters the city
    city = input("Enter a location: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=57&lon=-2.15&appid={API_key}&units=metric" + \
        API_key+"&q="+city
    weather_data = requests.get(url).json()
    # all of my units and conversions needed
    temp_kelvin = weather_data["main"]["temp"]
    temp_kelvin_feels_like = weather_data["main"]["feels_like"]
    temp_celsius = kelvin_to_celsius(temp_kelvin)
    temp_celsius_feels_like = kelvin_to_celsius(temp_kelvin_feels_like)
    sunrise_time = dt.datetime.utcfromtimestamp(
        weather_data["sys"]["sunrise"] + weather_data["timezone"])
    sunset_time = dt.datetime.utcfromtimestamp(
        weather_data["sys"]["sunset"] + weather_data["timezone"])
    clouds = weather_data["weather"][0]["description"]
    wind_speed = weather_data["wind"]["speed"]
    wind_degrees = weather_data["wind"]["deg"]
    place = weather_data["name"]
    identification = weather_data["id"]
    timezone = weather_data["timezone"]
    humidity = weather_data["main"]["humidity"]
    time_id = dt.datetime.utcfromtimestamp(
        weather_data["dt"] + weather_data["timezone"])
    # information displayed on screen
    print(f"")
    print(f"Temperature in {city}: {temp_celsius}°C")
    print(f"Temperature in {city} feels like: {temp_celsius_feels_like}°C")
    print(f"Humidity in {city}: {humidity}%")
    print(f"Wind speed in {city}: {wind_speed}m/s")
    print(f"Wind direction in {city}: {wind_degrees}°")
    print(f"General Weather in {city}: {clouds}")
    print(f"Sun rises in {city} at {sunrise_time} local time")
    print(f"Sun sets in {city} at {sunset_time} local time")
    print(f"The current time in {place}: {time_id}")
