from service.scraper.scraper_service import DecolarScraper
from service.date_and_time import DateAndTime
from model.trip_package.package_model import DecolarDestinations
from selenium import webdriver
from datetime import date

def naive_tsp(start_destination: DecolarDestinations, destinations: list, start_date, stay_time):
    flight_dates = DateAndTime.get_dates_in_interval(stay_time, start_date, len(destinations)+1)
    minimum_cost_path = [start_destination]
    minimum_cost_result = list()
    aux_destinations = destinations.copy()
    
    total_cost = 0
    driver = webdriver.Chrome()

    while True:
        lowest_price = 1000000 # Find better way to start lowest_price
        
        for destination in aux_destinations:
            result = DecolarScraper.get_flight_prices(destination, minimum_cost_path[-1], date.fromisoformat(flight_dates[-1]), driver)
            if result is None:
                print("Scraper didnt wait for page to load")
                continue
            if min(result) <= lowest_price:
                aux_destination = destination
                lowest_price = min(result)
        
        minimum_cost_result.append(((aux_destination, minimum_cost_path[-1]), lowest_price, flight_dates[-1]))
        minimum_cost_path.append(aux_destination)
        aux_destinations.remove(aux_destination)
        flight_dates.pop()

        if len(aux_destinations) == 0:
            break
    
    temp = minimum_cost_result[-1]
    temp = temp[0]
    temp = temp[0]
    result = DecolarScraper.get_flight_prices(start_destination, temp, start_date, driver)
    minimum_cost_result.append(((start_destination, temp), min(result), start_date))
    minimum_cost_result.reverse()
    print(minimum_cost_result)
    
    return minimum_cost_result




# naive_tsp(DecolarDestinations.BRASILIA, [DecolarDestinations.ARACAJU, DecolarDestinations.BELEM, DecolarDestinations.BELO_HORIZONTE], "2022-10-30", 5)


    


    

        

    
