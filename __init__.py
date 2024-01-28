from flask import Flask , render_template , request
from .search_weather import search_weather

def create_app():
    app = Flask(__name__)

    @app.route('/', methods = ('GET','POST'))
    def weather():
        weather_data=0
        if request.method == 'POST':
            city=request.form['city']
            state=request.form['state']
            country=request.form['country']
            weather,temperature, humidity = search_weather(city,state,country)
            weather_data = { 'weather': weather , 'temperature': temperature, 'humidity': humidity , 'city': city}

        return render_template('base.html', weather_data=weather_data)

    return app

