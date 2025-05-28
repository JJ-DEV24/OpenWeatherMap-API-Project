import requests
import os
from pprint import pprint
from datetime import datetime
import asyncio  # event loop

import aiohttp
from datetime import datetime


"""Task Groups"""
# Provides built-in error handling unlike "Gather". This cancels all the other tasks if there is an error with one of the tasks

location_coordinates: dict[str, tuple[float, float]] = {"london": (51.5073219, -0.1276474),
                                                        "paris": (48.8588897, 2.3200410217200766),
                                                        "lisbon": (38.7077507, -9.1365919),
                                                        "harare": (-17.831773, 31.045686)}  # stored coordinates in a list instead of a tuple


async def get_weather(latitude: float,
                      longitude: float):  # coroutine function (async) returns coroutine object (see below)
    api_key = os.getenv("openweatherapi")
    url1 = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"  # API call for current weather
    # response_1 = requests.get(url1) # NB: Get requests is a synchronous request -- need to use async get request!
    # pprint(response_1.json())
    async with aiohttp.ClientSession() as session:
        async with session.get(url1) as response:  # async context manager
            result = await response.json()
            return result


# Our main function contains task groups (see below)
async def main():
    start_time = datetime.now()
    pprint(datetime.now() - start_time)
    tasks = []
    async with asyncio.TaskGroup() as tg:  # This is an asynchronous context manager which has been abbreviated to "tg".
        for city in location_coordinates:
            lat, lon = location_coordinates.get(city)
            coroutine_object = get_weather(lat, lon)
            task = tg.create_task(coroutine_object)
            tasks.append(task)
    results = [task.result() for task in tasks]  # list comprehension
    for result in results:
        print(result)
    delta = datetime.now() - start_time
    pprint(delta.total_seconds())
    pprint(delta.seconds)


asyncio.run(main())
