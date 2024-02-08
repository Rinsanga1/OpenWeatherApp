from app.models import CSC
import requests
import datetime
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os

load_dotenv()
api_key = os.getenv('API_KEY')


def search_weather(cityi):
    buffer = CSC.query.filter_by(city=cityi).first()
    lat = buffer.lat
    lon = buffer.lon
    state = buffer.state
    country = buffer.country
    sunrise, sunset, temp, humidity, wether, windspeed, feelslike,icon,ldt = weather(
        lat, lon, api_key)
    return sunrise, sunset, temp, humidity, wether, windspeed, feelslike,icon,ldt, state, country


def weather(lat, lon, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    response = requests.get(url).json()
    weather = response['weather'][0]['main']
    icon = response['weather'][0]['icon']
    temp = int(response['main']['temp'] - 273.15)
    humidity = response['main']['humidity']
    windspeed = int(response['wind']['speed'])
    feelslike = int(response['main']['feels_like'] - 273.15)
    sunrisets, sunsetts, offset = response['sys']['sunrise'], response['sys']['sunset'], response['timezone']
    sunrise, sunset, localdt = sunrise_sunset(sunrisets, sunsetts, offset)
    return sunrise, sunset, temp, humidity, weather, windspeed, feelslike, icon,localdt


def sunrise_sunset(sunrisets, sunsetts, offset):
    def convert_timestamp_to_timezone(timestamp, timezone_offset):
        return datetime.utcfromtimestamp(timestamp + timezone_offset)
    sunrise_datetime = convert_timestamp_to_timezone(sunrisets, offset)
    sunset_datetime = convert_timestamp_to_timezone(sunsetts, offset)
    offset_datetime = datetime.utcnow() + timedelta(seconds=offset)
    sunrise_str = sunrise_datetime.strftime("%-I:%M %p %Z%z")  
    sunset_str = sunset_datetime.strftime("%-I:%M %p %Z%z")  
    offset_str = offset_datetime.strftime("%Y/%m/%d %-I:%M %p %Z%z")
    return sunrise_str, sunset_str, offset_str
