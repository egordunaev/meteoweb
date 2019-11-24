from flask import Flask
from weather_data.openweathermap.openweathermap import OpenWeather
from db.db import WeatherDB  # for testing
import datetime

app = Flask(__name__)


@app.route('/get-open-weather/<country_name>/<city_name>')
def open_weather_output(country_name, city_name):
    open_weather = OpenWeather(country_name, city_name)
    weather_db = WeatherDB()
    weather_db.add_weather_data(open_weather.city["id"], open_weather.weather, datetime.datetime.now().strftime("%Y%m%d%H%M"))
    return "Done"
