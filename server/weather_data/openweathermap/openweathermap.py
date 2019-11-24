import requests
import os
from db.db import CitiesDB

api_key = os.environ.get("OWM_API_KEY", "")


class OpenWeather:
    def __init__(self, country_name, city_name):
        self.city = self.get_city(country_name, city_name)
        self.weather = self.get_weather(self.city["id"])

    def get_city(self, country, city):
        cities_db = CitiesDB()
        return cities_db.get_city(country, city)

    def get_weather(self, city_id):
        self.weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&APPID={api_key}&units=metric", headers={"User-Agent": "Mozilla/5.0"})
        return self.weather.json()
