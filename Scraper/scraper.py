from typing import final
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from enum import Enum
from bs4 import BeautifulSoup
from datetime import timedelta, date

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

    __base_search_url = "https://www.decolar.com/shop/flights/results/oneway/"

    @classmethod
    def get_flight_prices(cls, start_destination: DecolarDestinations, end_destination: DecolarDestinations, departure_date, driver: webdriver.Chrome):
        """ Get flight prices from start_destination to end_destination

        Args:
            start_destination (DecolarDestinations): Departure location
            end_destination (DecolarDestinations): Arrival location
            departure_date (String): Departure date "YYYY-MM-DD"
            driver (webdriver.Chrome): The webdriver to be used

        Returns:
            List: A list containing all prices
        """

        if start_destination.value == end_destination.value:
            return

        costs = list()

        url = cls.__format_search_url(start_destination, end_destination, departure_date)
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, "lxml")
        final_prices = soup.find_all("p", class_="item-fare fare-price")
        for final_price in final_prices:
            final_price_amount = final_price.find("span", class_="amount price-amount").text
            costs.append(int(final_price_amount.replace(".", "")))

        return costs

    @classmethod
    def get_multiple_flight_prices(cls, start_destinations: list, end_destination: DecolarDestinations, departure_date: str, driver: webdriver.Chrome):
        """Get flight prices from start_destinations to end_destination

        Args:
            start_destinations (list): A list containing all departure options 
            end_destination (DecolarDestinations): Arrival location
            departure_date (str): Departure date "YYYY-MM-DD"
            driver (webdriver.Chrome): The webdriver to be used

        Returns:
            dict: A dictionary with the start_destinations.name as keys and their respective costs as values 
        """

        flight_costs = dict()

        for destination in start_destinations:
            if destination == end_destination:
                continue

            url = cls.__format_search_url(destination, end_destination, departure_date)
            driver.get(url)

            costs = list()
            soup = BeautifulSoup(driver.page_source, "lxml")
            final_prices = soup.find_all("p", class_="item-fare fare-price")
            for final_price in final_prices:
                final_price_amount = final_price.find("span", class_="amount price-amount").text
                costs.append(int(final_price_amount.replace(".", "")))
            flight_costs[destination.name] = costs

        return flight_costs
        
    @classmethod
    def __format_search_url(cls, start_destination: DecolarDestinations, end_destination: DecolarDestinations, departure_date):
        url = cls.__base_search_url + start_destination.value + "/" + \
            end_destination.value + "/" + departure_date + "/1/0/0"
        return url

class DateHandler():
    
    @classmethod
    def get_flight_dates(cls, interval, initial_date, total_flights):
        start = date.fromisoformat(initial_date)
        flight_dates = list()
        flight_dates.append(start)

        time_interval = timedelta(days=interval)
        for i in range(1, total_flights):
            flight_dates.append(flight_dates[i-1] + time_interval)
        
        return [x.isoformat() for x in flight_dates]
            