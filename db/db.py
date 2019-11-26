from pymongo import MongoClient
from os import environ
import json

db_host = environ.get("DB_HOST", "")
db_port = environ.get("DB_PORT", "")


class WeatherDB(MongoClient):
    def __init__(self):
        self.client = MongoClient(db_host, int(db_port))
        self.meteoweb_db = self.client["meteoweb"]
        self.weather_col = self.meteoweb_db["weather"]

    def get_city(self, city_id):
        return self.weather_col.find_one({"id": city_id})

    def get_all(self):
        return self.weather_col.find()

    def get_by_country(self, locale):
        return self.weather_col.find({"country": locale})

    def add_city(self, city):
        self.weather_col.insert(city)

    def delete_city(self, city_id):
        if self.get_city(city_id) is not None:
            self.weather_col.delete_one({"id": city_id})

    def add_weather_data(self, city_id, weather_data, timestamp):
        _city = self.get_city(city_id)
        if _city is not None:
            _weather = _city["weather"]
            _weather.update({timestamp: weather_data})
            self.weather_col.update_one({"id": city_id}, {"$set": {"weather": _weather}})


class CitiesDB(MongoClient):
    def __init__(self):
        self.client = MongoClient(db_host, int(db_port))
        self.meteoweb_db = self.client["meteoweb"]
        self.cities = self.meteoweb_db["cities"]
        if self.cities is None:
            self.create_cities()

    def get_city(self, locale, city_name):
        return self.cities.find_one({"country": locale, "name": city_name.title()})

    def get_cities_by_country(self, locale):
        return self.cities.find({"country": locale})

    def get_cities(self, locale, city_name):
        return self.cities.find({"country": locale, "name": city_name})

    # populates cities collection from city.list file
    def create_cities(self):
        self.meteoweb_db.create_collection("cities")
        self.cities = self.meteoweb_db["cities"]
        with open("city.list.json", encoding="utf8") as cities_json:
            cities = json.load(cities_json)
        for item in cities:
            self.cities.insert_one(item)
