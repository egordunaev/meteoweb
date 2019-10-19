from flask import Flask, escape, request
from weather_data.gismeteo.gismeteo_search import GisMeteoSearcher

app = Flask(__name__)


@app.route('/get-weather/<country>/<city>')
def output(country, city):
    search = GisMeteoSearcher(country, city)
    result = request.args.get("result", search.get_link(search.city_name, search.country))
    return f'{escape(result)}'
