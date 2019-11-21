import requests
import json
import os

api_key = os.environ.get("OWM_API_KEY", "")


class OpenWeather:
    def __init__(self, country_name, city_name):
        self.city = self.get_city(country_name, city_name)
        self.weather = self.get_weather(self.city["id"])

    def get_city(self, country, city):
        with open("server/weather_data/openweathermap/city.list.json", encoding="utf8") as cities_json:
            cities = json.load(cities_json)
        for item in cities:
            if item["name"].lower() == city and item["country"] == country:
                return item
        return None

    def get_weather(self, city_id):
        self.weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&APPID={api_key}", headers={"User-Agent": "Mozilla/5.0"})
        return self.weather.json()
