import requests
import os
from pprint import pprint
from datetime import datetime
import asyncio  # event loop

import aiohttp
import json
from datetime import datetime



location_coordinates = {"london": (51.5073219, -0.1276474), "paris": (48.8588897, 2.3200410217200766),
                        "lisbon": (38.7077507, -9.1365919), "harare": (-17.831773, 31.045686)}
african_countries = [
    ("ZAF", "South Africa", ["Cape Town", "Johannesburg", "Pretoria", "Durban"]),
    ("EGY", "Egypt", ["Cairo", "Alexandria", "Giza", "Luxor"]),
    ("DZA", "Algeria", ["Algiers", "Oran", "Constantine", "Annaba"]),
    ("ETH", "Ethiopia", ["Addis Ababa", "Dire Dawa", "Mek'ele", "Adama"]),
    ("MAR", "Morocco", ["Rabat", "Casablanca", "Fes", "Marrakech"]),
    ("NGA", "Nigeria", ["Lagos", "Abuja", "Kano", "Ibadan"]),
    ("KEN", "Kenya", ["Nairobi", "Mombasa", "Kisumu", "Nakuru"]),
    ("AGO", "Angola", ["Luanda", "Huambo", "Lobito", "Benguela"]),
    ("CIV", "Côte d'Ivoire", ["Yamoussoukro", "Abidjan", "Bouaké", "Daloa"]),
    ("TZA", "Tanzania", ["Dodoma", "Dar es Salaam", "Mwanza", "Arusha"]),
    ("GHA", "Ghana", ["Accra", "Kumasi", "Tamale", "Sekondi-Takoradi"]),
    ("COD", "Democratic Republic of the Congo", ["Kinshasa", "Lubumbashi", "Mbuji-Mayi", "Kisangani"]),
    ("UGA", "Uganda", ["Kampala", "Gulu", "Lira", "Mbarara"]),
    ("CMR", "Cameroon", ["Yaoundé", "Douala", "Garoua", "Bamenda"]),
    ("TUN", "Tunisia", ["Tunis", "Sfax", "Sousse", "Kairouan"]),
    ("LBY", "Libya", ["Tripoli", "Benghazi", "Misrata", "Tobruk"]),
    ("ZWE", "Zimbabwe", ["Harare", "Bulawayo", "Chitungwiza", "Mutare"]),
    ("SEN", "Senegal", ["Dakar", "Pikine", "Thiès", "Kaolack"]),
    ("SDN", "Sudan", ["Khartoum", "Omdurman", "Port Sudan", "Kassala"]),
    ("ZMB", "Zambia", ["Lusaka", "Ndola", "Kitwe", "Livingstone"]),
    ("GIN", "Guinea", ["Conakry", "Nzérékoré", "Kindia", "Kankan"]),
    ("MOZ", "Mozambique", ["Maputo", "Matola", "Nampula", "Beira"]),
    ("BFA", "Burkina Faso", ["Ouagadougou", "Bobo-Dioulasso", "Koudougou", "Ouahigouya"]),
    ("MLI", "Mali", ["Bamako", "Sikasso", "Mopti", "Kayes"]),
    ("BEN", "Benin", ["Porto-Novo", "Cotonou", "Djougou", "Parakou"]),
    ("GAB", "Gabon", ["Libreville", "Port-Gentil", "Franceville", "Oyem"]),
    ("BWA", "Botswana", ["Gaborone", "Francistown", "Molepolole", "Maun"]),
    ("NER", "Niger", ["Niamey", "Zinder", "Maradi", "Agadez"]),
    ("TCD", "Chad", ["N'Djamena", "Moundou", "Sarh", "Abéché"]),
    ("MDG", "Madagascar", ["Antananarivo", "Toamasina", "Antsirabe", "Mahajanga"])
]


#  ("ZAF", "South Africa", ["Cape Town", "Johannesburg", "Pretoria", "Durban"]),

def get_coords(data):
    country_code = data[0]  # ISO 3166 country code for UK
    city_name = data[2][0]
    limit = 1
    api_key = os.getenv("openweatherapi")
    url1 = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit={limit}&appid={api_key}"
    converted_json_object = requests.get(url1).json()  # this method.json returns python data structures/ objects
    lat = converted_json_object[0].get('lat')
    lon = converted_json_object[0].get('lon')
    return (lat,lon)


def get_weather(latitude: float,longitude: float):  # coroutine function (async) returns coroutine object (see below)
    api_key = os.getenv("openweatherapi")
    url1 = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"  # API call for current weather
    response_1 = requests.get(url1) # NB: Get requests is a synchronous request -- need to use async get request!
    return response_1.json()


def main():
    startTime = datetime.now()
    pprint(datetime.now() - startTime)
    list_of_coords = []
    results = []
    for country in african_countries:
        list_of_coords.append(get_coords(country))
    for each in list_of_coords:
        results.append(get_weather(each[0],each[1]))
    print(results)

    delta = datetime.now() - startTime
    pprint(delta.total_seconds())
    pprint(delta.seconds)


main()
