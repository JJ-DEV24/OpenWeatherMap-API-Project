# OpenWeatherMap API Project

This project was built to learn how to use the AsycnIO Python library to make asynchronous API requests using [task groups](https://docs.python.org/3/library/asyncio-task.html#task-groups).


# Description

I used 3 diferrent ways of making API calls to the server to request weather forecast data from various cities. I did this by making synchronous requests, and asynchronous requests using task groups. 
To measure the time taken to retrieve the data using all three API calls, I used the datetime module in Python.

The outcome of this project revealed asychronous requests using task groups took significantlly less time to retireve the data than synchronous requests.


# Motivations
The purpose of this project was to learn how to implement a feature into my [Sounds and Lyrics](https://github.com/JJ-DEV24/SoundsAndLyrics) application in which the user can retrieve song lyrics from an entire album.


## Resources: 
FAST API's article [Concurrency and Async/ Await](https://fastapi.tiangolo.com/async/)

[Fluent Python book by O’Reilly](https://www.oreilly.com/library/view/fluent-python/9781491946237/) - Concurrency with Asyncio

[Python Documentation on task groups](https://docs.python.org/3/library/asyncio-task.html#task-groups)
