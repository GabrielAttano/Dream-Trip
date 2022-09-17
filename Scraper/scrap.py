from typing import final
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from enum import Enum
from bs4 import BeautifulSoup


class DecolarDestinations(Enum):
    """Class that represents all destinations avaible at https://www.decolar.com/ and their
    abbreviations.
    """

    BRASILIA = "BSB"
    PORTO_ALEGRE = "POA"
    SALVADOR = "SSA"


class DecolarScraper():

    def __init__(self) -> None:
        self.__base_search_url = "https://www.decolar.com/shop/flights/results/oneway/"
        self.__driver = webdriver.Chrome()

    def get_flight_prices(self, start_destination: DecolarDestinations, end_destination: DecolarDestinations, departure_date):
        url = self.__format_search_url(
            start_destination, end_destination, departure_date)
        self.__driver.get(url)
        soup = BeautifulSoup(self.__driver.page_source, "lxml")
        final_prices_container = soup.find_all(
            "p", class_="item-fare fare-price")
        for final_price in final_prices_container:
            amount = final_price.find("span", class_="amount price-amount")
            print(amount.text)
        self.__driver.close()

    def __format_search_url(self, start_destination: DecolarDestinations, end_destination: DecolarDestinations, departure_date):
        url = self.__base_search_url + start_destination.value + "/" + \
            end_destination.value + "/" + departure_date + "/1/0/0"
        return url
