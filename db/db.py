from pymongo import MongoClient

client = MongoClient('localhost', 27017)
meteoweb_db = client["meteoweb"]
weather_col = meteoweb_db["weather"]
