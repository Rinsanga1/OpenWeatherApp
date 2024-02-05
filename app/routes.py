from flask import Flask, json, render_template, request, jsonify
from app.search_weather import search_weather
from app.forms import City_Form
from app import app, db
from app.models import CSC
import sqlalchemy as sa

app.app_context().push()
cities = db.session.scalars(sa.select(CSC.city)).all()


@app.route('/', methods=('GET', 'POST'))
def weather():
    form = City_Form()
    weather_data = None
    if request.method == 'POST':
        state,country,weather, temperature, humidity = search_weather(form.city_form.data)
        weather_data = {'state': state, 'country': country , 'weather': weather,
                        'temperature': temperature, 'humidity': humidity}
    return render_template('base.html', form=form, weather_data=weather_data)


@app.route('/suggestion')
def suggest_city():
    term = request.args.get('term')
    suggestions = [city for city in cities if term.lower() in city.lower()]

    return jsonify(suggestions)
