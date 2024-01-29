import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')


def search_weather(city,state,country):
    lat,lon = lat_lon(city,state,country,api_key)
    weather_data = weather(lat,lon,api_key)
    return weather_data



def lat_lon(city,state,country,api_key):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&appid={api_key}'
    response = requests.get(url).json()
    lat=response[0].get('lat')
    lon=response[0].get('lon')
    return lat,lon


def weather(lat,lon,api_key):
    url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    response=requests.get(url).json()
    weather_main = response.get('weather')[0].get('main')
    main_temp = response.get('main').get('temp')
    main_humidity = response.get('main').get('humidity')
    return weather_main , main_temp , main_humidity

