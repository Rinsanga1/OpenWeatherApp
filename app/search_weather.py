from app.models import CSC
import requests
from dotenv import load_dotenv
import os
import datetime

load_dotenv()
api_key = os.getenv('API_KEY')


def search_weather(cityi):
    buffer = CSC.query.filter_by(city=cityi).first()
    lat = buffer.lat
    lon = buffer.lon
    state = buffer.state
    country = buffer.country
    sunrise, sunset, temp, humidity, wether, windspeed, feelslike,icon = weather(
        lat, lon, api_key)
    return sunrise, sunset, temp, humidity, wether, windspeed, feelslike,icon, state, country


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
    sunrise, sunset = sunrise_sunset(sunrisets, sunsetts, offset)
    return sunrise, sunset, temp, humidity, weather, windspeed, feelslike, icon


def sunrise_sunset(sunrisets, sunsetts, offset):
    def unix_timestamp_to_datetime(timestamp):
        return datetime.datetime.utcfromtimestamp(timestamp)

    def convert_to_timezone(dt, timezone_offset):
        return dt + datetime.timedelta(seconds=timezone_offset)

    def convert_timestamp_to_timezone(timestamp, timezone_offset):
        dt_utc = unix_timestamp_to_datetime(timestamp)
        dt_timezone = convert_to_timezone(dt_utc, timezone_offset)
        return dt_timezone
    sunrise_datetime = convert_timestamp_to_timezone(sunrisets, offset)
    sunset_datetime = convert_timestamp_to_timezone(sunsetts, offset)
    sunrise_str = sunrise_datetime.strftime("%-I:%M %Z%z")
    sunset_str = sunset_datetime.strftime("%-I:%M %Z%z")
    return sunrise_str, sunset_str
