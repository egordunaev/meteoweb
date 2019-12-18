from flask import Flask
from weather_data.openweathermap.openweathermap import OpenWeather
from db.db import WeatherDB  # for testing
import datetime
import threading
import schedule
import time

app = Flask(__name__)


@app.route('/get-open-weather/<country_name>/<city_name>')
def open_weather_output(country_name, city_name):
    open_weather = OpenWeather()
    weather_db = WeatherDB()
    if weather_db.get_city(open_weather.city["id"]) is None:
        weather_db.add_city(open_weather)
    else:
        weather_db.add_weather_data(open_weather.city["id"], open_weather.weather, datetime.datetime.now().strftime("%Y%m%d%H%M"))
    return "Done"


@app.route("/collect-data/<point_id>")
def schedule_data_collection(point_id):
    schedule.every(1).minutes.do(run_threaded, collect_data(point_id)).tag(str(point_id))
    run_schedule()
    return "done"


@app.route("/cancel/<point_id>")
def cancel_scheduling(point_id):
    weather_db = WeatherDB()
    weather_db.update_scheduling_status(point_id, False)
    schedule.clear(str(point_id))


def collect_data(point_id):
    open_weather = OpenWeather()
    weather_db = WeatherDB()
    city = weather_db.get_city(point_id)
    if city is None:
        open_weather.city = open_weather.get_city(point_id)
        open_weather.weather = open_weather.get_weather(point_id)
        open_weather.scheduled = True
        weather_db.add_city(open_weather)
    else:
        open_weather.weather = open_weather.get_weather(point_id)
        weather_db.add_weather_data(point_id, open_weather.weather, datetime.datetime.now().strftime("%Y%m%d%H%M"))


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)
