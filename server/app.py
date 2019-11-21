from flask import Flask, escape, request
from weather_data.gismeteo.gismeteo_search import GisMeteoSearcher
from weather_data.openweathermap.openweathermap import OpenWeather
from db.db import WeatherDB  # for testing
import datetime

app = Flask(__name__)


@app.route('/get-weather/<country>/<city>')
def output(country, city):
    search = GisMeteoSearcher(country, city)
    result = request.args.get("result", search.get_link(search.city_name, search.country))
    return f'{escape(result)}'


@app.route('/get-open-weather/<country_name>/<city_name>')
def open_weather_output(country_name, city_name):
    open_weather = OpenWeather(country_name, city_name)
    weather_db = WeatherDB()
    weather_db.add_weather_data(open_weather.city["id"], open_weather.weather, datetime.datetime.now().strftime("%Y%m%d%H%M"))
    return "Done"
