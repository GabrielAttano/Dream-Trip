from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from model.trip_package.package_model import DecolarDestinations
from service.date_and_time import DateAndTime
import datetime
class DecolarScraper():

    __base_search_url = "https://www.decolar.com/shop/flights/results/oneway/"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    @classmethod
    def get_flight_prices(cls, start_destination: DecolarDestinations, end_destination: DecolarDestinations, departure_date, driver: webdriver.Chrome(options= options)):

        if start_destination.value == end_destination.value:
            return

        
        # if departure_date < datetime.date.today():
        #     return

        costs = list()

        url = cls.__format_search_url(start_destination, end_destination, str(departure_date))
        driver.get(url)

        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "item-detail")))
        except:
            print("Didnt wait for page to load")
            return 

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
            costs = cls.get_flight_prices(destination, end_destination, departure_date, driver)
            flight_costs[destination.name] = costs

        return flight_costs
        
    @classmethod
    def __format_search_url(cls, start_destination: DecolarDestinations, end_destination: DecolarDestinations, departure_date):
        url = cls.__base_search_url + start_destination.value + "/" + \
            end_destination.value + "/" + departure_date + "/1/0/0"
        return url
