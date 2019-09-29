from flask import Flask, escape, request
from weather_data.gismeteo.gismeteo_search import GisMeteoSearcher

app = Flask(__name__)


@app.route('/')
def hello():
    search = GisMeteoSearcher("ivanovo", "Russian Federation")
    result = request.args.get("result", search.get_city_link(search.city_name, search.country))
    return f'Hello, {escape(result)}!'
