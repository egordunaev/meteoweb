#  used for searching exact city link in gismeteo.com
import requests
import os
from bs4 import BeautifulSoup

gismeteo_addr = os.environ.get("GISMETEO_ADDR", "")


class GisMeteoSearcher:
    def __init__(self, city_name, country, district_name=None):
        self.city_name = city_name
        self.district_name = district_name
        self.country = country

    def get_city_link(self, city_name, country, district_name=None):
        try:
            page = requests.get(f"{gismeteo_addr}/search/{self.city_name}/", headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(page.content, "html.parser")
            cities = soup.find_all("div", {"class": "catalog_list"})  # .find_all("div", {"class": "catalog_item"})
            return "done"  # temp
        except Exception as ex:
            raise ex
