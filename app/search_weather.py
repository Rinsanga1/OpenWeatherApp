from app import app,db
from app.models import CSC
import sqlalchemy as sa
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')


def search_weather(cityi):
    buffer=CSC.query.filter_by(city=cityi).first()
    lat= buffer.lat
    lon= buffer.lon
    state = buffer.state
    country = buffer.country
    w,temperature,humidity = weather(lat,lon,api_key)
    return state,country,w,temperature,humidity



def weather(lat,lon,api_key):
    url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    response=requests.get(url).json()
    weather_main = response.get('weather')[0].get('main')
    main_temp = int(response.get('main').get('temp') - 273.15)
    main_humidity = response.get('main').get('humidity')
    return weather_main , main_temp , main_humidity

