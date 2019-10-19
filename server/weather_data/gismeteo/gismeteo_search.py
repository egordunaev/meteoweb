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

    def get_link(self, city_name, country, district_name=None):
        try:
            return self.get_country_link(country)
        except Exception as ex:
            raise ex

    def get_city_link(self, city_name, country_link):
        try:
            page = requests.get(f"{gismeteo_addr}{country_link}", headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(page.content, "html.parser")
            soup_city = soup.find_all("div", {"class": "catalog_list catalog_list_ordered"})
        except Exception as ex:
            raise ex

    def get_country_link(self, country):
        try:
            page = requests.get(f"{gismeteo_addr}/catalog/", headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(page.content, "html.parser")
            soup_country = soup.find_all("div", {"class": "catalog_item"})  # .find_all("div", {"class": "catalog_item"})
            for item in soup_country:
                _country = item.contents[0].contents[1].strip()
                if country in _country:
                    return item.contents[0].attrs["href"]
            return soup_country
        except Exception as ex:
            raise ex
