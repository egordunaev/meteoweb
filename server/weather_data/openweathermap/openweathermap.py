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
        with open("server/weather_data/openweathermap/city.list.json", encoding="utf8") as cities_json:
            cities = json.load(cities_json)
        for item in cities:
            if item["name"].lower() is city and item["country"] is country:
                return item
        return None

    def get_weather(self, city_id):
        weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&APPID={api_key}", headers={"User-Agent": "Mozilla/5.0"})
        # weather_dict = weather.json() - use this when finished
        return weather.json()
