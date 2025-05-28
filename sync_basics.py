import asyncio
import requests
import os
from pprint import pprint
from datetime import datetime

startTime = datetime.now()
pprint(datetime.now() - startTime)


# watch corey schafer vid on env vars
# set the environment variable to store the api key
# Had to ensure that I ran different queries on the openweather api because when I timed it I was getting fast responses
# thinking that the data may have been cached on the sever side (open weather API).
# Testing: How many seconds my synchronous function "get_weather"  takes to make 4 different requests.I did this by
# using the dat time library to record the total amount of seconds. It took a total of 0.31 seconds by requesting data
# from 5 different areas relating to the city name.

def get_coordinates():
    city_name = "London"
    country_code = "GB"  # ISO 3166 country code for UK
    limit = 1
    api_key = os.getenv("openweatherapi")
    url1 = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit={limit}&appid={api_key}"  # Coordinates by location name
    url2 = f"http://api.openweathermap.org/geo/1.0/direct?q={'Paris'},{'FR'}&limit={limit}&appid={api_key}"
    url3 = f"http://api.openweathermap.org/geo/1.0/direct?q={'Lisbon'},{'PT'}&limit={limit}&appid={api_key}"
    url4 = f"http://api.openweathermap.org/geo/1.0/direct?q={'Harare'},{'ZWE'}&limit={limit}&appid={api_key}"
    response_1 = requests.get(url1)
    response_2 = requests.get(url2)
    response_3 = requests.get(url3)
    response_4 = requests.get(url4)
    with open("weather_data_1.json", "w+", encoding='utf-8') as file:
        file.write(str(response_1.json()))
    with open("weather_data_2.json", "w+", encoding='utf-8') as file:
        file.write(str(response_2.json()))
    with open("weather_data_3.json", "w+", encoding='utf-8') as file:
        file.write(str(response_3.json()))
    with open("weather_data_4.json", "w+", encoding='utf-8') as file:
        file.write(str(response_4.json()))


def get_weather(latitude: float, longitude: float):
    api_key = os.getenv("openweatherapi")
    url1 = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"  # API call for current weather
    response_1 = requests.get(url1)
    pprint(response_1.json())


london_lat = 51.5073219
london_lon = -0.1276474

get_weather(london_lat, london_lon)

# get_coordinates()
delta = datetime.now() - startTime
pprint(delta.total_seconds())
pprint(delta.seconds)
