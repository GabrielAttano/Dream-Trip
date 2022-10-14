from service.scraper.scraper_service import DecolarScraper
from model.trip_package.package_model import DecolarDestinations
from selenium import webdriver
import time

def test_scraping_time(total_destinations, end_destination: DecolarDestinations, departure_date, driver: webdriver.Chrome):
    destinations = [x for x in DecolarDestinations]
    start = time.time()
    dict_result = DecolarScraper.get_multiple_flight_prices(destinations[:total_destinations], end_destination, departure_date, driver)
    end = time.time()
    print(dict_result)
    for key, value in dict_result.items():
        if(len(value) <= 0):
            continue
        print(f"{key} -> {end_destination.name}: {min(value)}")
    print(f"total time = {end - start}")


# print(DateHandler.get_flight_dates(10, "2022-09-21", 5))
driver = webdriver.Chrome()
test_scraping_time(7, DecolarDestinations.PALMAS, "2022-10-25", driver)