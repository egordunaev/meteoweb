from pymongo import MongoClient
from os import environ

db_host = environ.get("DB_HOST", "")
db_port = environ.get("DB_PORT", "")


class WeatherDB(MongoClient):
    def __init__(self):
        self.client = MongoClient(db_host, int(db_port))
        self.meteoweb_db = self.client["meteoweb"]
        self.weather_col = self.meteoweb_db["weather"]
        self.cities_col = self.meteoweb_db["cities"]

    def get_city(self, city_id):
        return self.weather_col.find_one({"id": city_id})

    def get_all(self):
        return self.weather_col.find()

    def get_by_country(self, locale):
        return self.weather_col.find({"country": locale})

    def add_city(self, city):
        if self.get_city(city["id"]) is None:
            self.weather_col.insert(city)

    def delete_city(self, city_id):
        if self.get_city(city_id) is not None:
            self.weather_col.delete_one({"id": city_id})

    def add_weather_data(self, city_id, weather_data, timestamp):
        if self.get_city(city_id) is not None:
            _weather = self.get_city(city_id)["weather"]
            _weather.update({timestamp: weather_data})
            self.weather_col.update_one({"id": city_id}, {"$set": {"weather": _weather}})
