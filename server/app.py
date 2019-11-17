from flask import Flask, escape, request
from weather_data.gismeteo.gismeteo_search import GisMeteoSearcher
from weather_data.openweathermap.openweathermap import OpenWeather

app = Flask(__name__)


@app.route('/get-weather/<country>/<city>')
def output(country, city):
    search = GisMeteoSearcher(country, city)
    result = request.args.get("result", search.get_link(search.city_name, search.country))
    return f'{escape(result)}'


@app.route('/get-open-weather/<country_name>/<city_name>')
def open_weather_output(country_name, city_name):
    open_weather = OpenWeather(country_name, city_name)
    return open_weather.get_weather(555312)
