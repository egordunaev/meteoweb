import requests
import os
from db.db import CitiesDB

api_key = os.environ.get("OWM_API_KEY", "")


class OpenWeather:
    def __init__(self):
        self.city = dict()
        self.weather = dict()
        self.scheduled = bool()

    def get_city(self, city_id):
        cities_db = CitiesDB()
        return cities_db.get_city(city_id)

    def get_weather(self, city_id):
        self.weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&APPID={api_key}&units=metric", headers={"User-Agent": "Mozilla/5.0"})
        return self.weather.json()
