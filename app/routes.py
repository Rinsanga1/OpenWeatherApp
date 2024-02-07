from app import app, db
from flask import Flask, json, render_template, request, jsonify
import sqlalchemy as sa
from app.search_weather import search_weather
from app.forms import City_Form
from app.models import CSC

app.app_context().push()
cities = db.session.scalars(sa.select(CSC.city)).all()


@app.route('/', methods=('GET', 'POST'))
def weather():
    form = City_Form()
    weather_data = None
    if request.method == 'POST':
        sunrise,sunset,temp,humidity,wether,windspeed,feelslike,icon,state,country = search_weather(form.city_form.data)
        weather_data = {'state': state, 'country': country , 'weather': wether,'sunrise': sunrise, 'sunset': sunset,
                        'temperature': temp, 'humidity': humidity , 'windspeed' : windspeed , 'feelslike': feelslike ,'icon': icon}
    return render_template('base.html', form=form, weather_data=weather_data)


@app.route('/suggestion')
def suggest_city():
    term = request.args.get('term')
    suggestions = [city for city in cities if term.lower() in city.lower()]
    return jsonify(suggestions)

