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
    RIO_BRANCO = "RBR"
    MACEIO = "MCZ"
    MACAPA = "MCP"
    MANAUS = "MAO"
    SALVADOR = "SSA"
    FORTALEZA = "FOR"
    VITORIA = "VIX"
    GOIANIA = "GYN"
    SAO_LUIS = "SLZ"
    CUIABA = "CGB"
    CAMPO_GRANDE = "CGR"
    BELO_HORIZONTE = "BHZ"
    BELEM = "BEL"
    JOAO_PESSOA = "JPA"
    CURITIBA = "CWB"
    RECIFE = "REC"
    TERESINA = "THE"
    RIO_DE_JANEIRO = "RIO"
    NATAL = "NAT"
    PORTO_ALEGRE = "POA"
    PORTO_VELHO = "PVH"
    BOA_VISTA = "BVB"
    FLORIANOPOLIS = "FLN"
    SAO_PAULO = "SAO"
    ARACAJU = "AJU"
    PALMAS = "PMW"


class DecolarScraper():

    def __init__(self) -> None:
        self.__base_search_url = "https://www.decolar.com/shop/flights/results/oneway/"

    def get_flight_prices(self, start_destination: DecolarDestinations, end_destination: DecolarDestinations, departure_date, driver: webdriver.Chrome):
        if start_destination.value == end_destination.value:
            return

        costs = list()

        url = self.__format_search_url(start_destination, end_destination, departure_date)
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, "lxml")
        final_prices = soup.find_all("p", class_="item-fare fare-price")
        for final_price in final_prices:
            final_price_amount = final_price.find("span", class_="amount price-amount")
            costs.append(int(final_price_amount.text))

        driver.close()
        return costs

    def get_multiple_flight_prices(self, start_destinations: list, end_destination: DecolarDestinations, departure_date, driver: webdriver.Chrome):
        flight_costs = dict()

        for destination in start_destinations:
            if destination == end_destination:
                continue

            url = self.__format_search_url(destination, end_destination, departure_date)
            driver.get(url)

            costs = list()
            soup = BeautifulSoup(driver.page_source, "lxml")
            final_prices = soup.find_all("p", class_="item-fare fare-price")
            for final_price in final_prices:
                final_price_amount = final_price.find("span", class_="amount price-amount").text
                costs.append(int(final_price_amount.replace(".", "")))
            flight_costs[destination.name] = costs

        driver.close()
        return flight_costs

    def __format_search_url(self, start_destination: DecolarDestinations, end_destination: DecolarDestinations, departure_date):
        url = self.__base_search_url + start_destination.value + "/" + \
            end_destination.value + "/" + departure_date + "/1/0/0"
        return url


