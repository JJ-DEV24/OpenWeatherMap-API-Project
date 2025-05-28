import requests
import os
from pprint import pprint
from datetime import datetime
import asyncio  # event loop

import aiohttp
from datetime import datetime

"""Tasks - await"""

location_coordinates = {"london": (51.5073219, -0.1276474), "paris": (48.8588897, 2.3200410217200766),
                        "lisbon": (38.7077507, -9.1365919), "harare": (-17.831773, 31.045686)}

async def get_weather(latitude: float,
                      longitude: float):  # coroutine function (async) returns coroutine object (see below)
    api_key = os.getenv("openweatherapi")
    url1 = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"  # API call for current weather
    async with aiohttp.ClientSession() as session:
        async with session.get(url1) as response:  # async context manager
            result = await response.json()
            return result

async def main():
    startTime = datetime.now()
    pprint(datetime.now() - startTime)

    london_lat, london_lon = location_coordinates.get('london')
    task1 = get_weather(london_lat, london_lon)  # coroutine object stored in task
    paris_lat, paris_lon = location_coordinates.get('paris')
    task2 = get_weather( paris_lat, paris_lon)
    lisbon_lat, lisbon_lon = location_coordinates.get('lisbon')
    task3 = get_weather( lisbon_lat, lisbon_lon)
    harare_lat, harare_lon = location_coordinates.get('harare')
    task4 = get_weather(harare_lat, harare_lon)

    result1 = await task1
    result2 = await task2
    result3 = await task3
    result4 = await task4

    print(result1, result2, result3, result4)

    delta = datetime.now() - startTime
    pprint(delta.total_seconds())
    pprint(delta.seconds)

asyncio.run(main())