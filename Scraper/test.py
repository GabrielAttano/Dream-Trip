from scraper import DecolarDestinations, DecolarScraper
from selenium import webdriver
import time

def test_scraping_time(total_destinations, end_destination: DecolarDestinations, departure_date, driver: webdriver.Chrome):
    scraper = DecolarScraper()
    destinations = [x for x in DecolarDestinations]
    start = time.time()
    dict_result = scraper.get_multiple_flight_prices(destinations[:total_destinations], end_destination, departure_date, driver)
    end = time.time()
    print(dict_result)
    print(f"total time = {end - start}")

driver = webdriver.Chrome()
test_scraping_time(10, DecolarDestinations.PALMAS, "2022-09-30", driver)
