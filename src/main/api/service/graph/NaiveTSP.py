from service.scraper.scraper_service import DecolarScraper
from service.date_and_time import DateAndTime
from model.destinations.destinations_model import DecolarDestinations
from selenium import webdriver

def NaiveTSP(start_point: DecolarDestinations, destinations: list, start_date, stay_time):
    flight_dates = DateAndTime.get_dates_in_interval(stay_time, start_date, len(destinations)+1)
    minimum_cost_path = [start_point]
    aux_destinations = destinations.copy()
    
    total_cost = 0

    while True:
        lowest_price = 1000000 # Find better way to start lowest_price
        driver = webdriver.Chrome()
        for destination in aux_destinations:
            result = DecolarScraper.get_flight_prices(destination, minimum_cost_path[-1], flight_dates[-1], driver)
            if len(result) == 0:
                print("Scraper didnt wait for page to load")
                continue
            if min(result) <= lowest_price:
                aux_destination = destination
                lowest_price = min(result)
                print(f"Lowest price found from {destination.name} to {minimum_cost_path[-1].name} (R${lowest_price})")
        driver.close()
        
        minimum_cost_path.append(aux_destination)
        print(type(aux_destination))
        print(aux_destination)
        print(minimum_cost_path)
        aux_destinations.remove(aux_destination)
        flight_dates.pop()

        if len(aux_destinations) == 0:
            break

NaiveTSP(DecolarDestinations.BRASILIA, [DecolarDestinations.ARACAJU, DecolarDestinations.BELEM, DecolarDestinations.BELO_HORIZONTE], "2022-09-30", 5)


    


    

        

    
