from flask import Flask , render_template , request
from OpenWeather import search_weather

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

    return render_template('index.html', weather_data=weather_data)


if __name__ == "__main__":
    app.run(debug=True)
