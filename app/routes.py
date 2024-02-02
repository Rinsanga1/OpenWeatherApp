from flask import Flask,render_template,request
from app.search_weather import search_weather
from app.forms import City_Form
from app import app



@app.route('/', methods = ('GET','POST'))
def weather():
    form = City_Form()
    weather_data = None
    if request.method == 'POST':
        weather,temperature, humidity = search_weather(form.city_form.data)
        weather_data = { 'weather': weather , 'temperature': temperature, 'humidity': humidity }
    return render_template('base.html', form = form , weather_data=weather_data)
