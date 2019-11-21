from pymongo import MongoClient


class WeatherDB(MongoClient):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.meteoweb_db = self.client["meteoweb"]
        self.weather_col = self.meteoweb_db["weather"]

    def get_city(self, city_id):
        return self.weather_col.find_one({"id": city_id})

    def get_all(self):
        return self.weather_col.find()

    def get_by_country(self, locale):
        return self.weather_col.find({"country": locale})

    def create_city(self, city):
        self.weather_col.insert(city)

    def delete_city(self, city_id):
        self.weather_col.delete_one({"id": city_id})

    def add_weather_data(self, city_id, weather_data, timestamp):
        _weather = self.get_city(city_id)["weather"]
        _weather.update({timestamp: weather_data})
        self.weather_col.update_one({"id": city_id}, {"$set": {"weather": _weather}})
