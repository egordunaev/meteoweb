import requests
import json
import os

api_key = os.environ.get("OWM_API_KEY", "")


class OpenWeather:
    def __init__(self, country, city):
        self.country = country
        self.city = city
        self.city_id = self.get_city_id(self.country, self.city)

    def get_city_id(self, country, city):
        return "temp"

    def get_weather(self, city_id):
        weather = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?id={city_id}&APPID={api_key}", headers={"User-Agent": "Mozilla/5.0"})
        return weather.json()
