import sys
from service.scraper.scraper_service import DecolarScraper
from service.date_and_time import DateAndTime
from service.scraper.updated_scraper.scraper_updated import concurrent_scrap
from model.trip_package.package_model import DecolarDestinations
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date
import time

def naive_tsp(start_destination: DecolarDestinations, destinations: list, start_date, stay_time):
    flight_dates = DateAndTime.get_dates_in_interval(stay_time, start_date, len(destinations)+1)
    minimum_cost_path = [start_destination]
    minimum_cost_result = list()
    aux_destinations = destinations.copy()
    
    total_cost = 0

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options= options)

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
    return minimum_cost_result

def nearest_neighbour(origin: DecolarDestinations, destinations: list, start_date: str, stay_time: int):
    base_url = "https://www.decolar.com/shop/flights/results/oneway/"
    result = {"lowest_cost_path": [], "total_price": 0}
    # Criando cópia da lista de destinos
    destinations_copy = destinations.copy()
    end_destination = origin # Definindo a origem como destino final ao começar o loop

    # criando lista com as datas (o tamanho tem que ser +1 pois a lista de destinations não inclui a origem)
    flight_dates = DateAndTime.get_dates_in_interval(stay_time, start_date, len(destinations_copy) + 1)

    while True:
        prices_dict = concurrent_scrap(base_url, end_destination, destinations_copy, flight_dates[-1])

        min_tuple = get_min(prices_dict)
        destination = min_tuple[0]
        cost = min_tuple[1]
        result["lowest_cost_path"].append((f"{destination} => {end_destination}", cost))
        result["total_price"] = result["total_price"] + cost

        destinations_copy.remove(destination) # remover destino da lista de destinos
        end_destination = destination # Definir destino como destino final do próximo loop
        flight_dates.pop() # Removendo última data

        print(result)
        if len(destinations_copy) == 0:
            prices_dict = concurrent_scrap(base_url, destination, origin, flight_dates[-1])
            min_tuple = get_min(prices_dict)
            result["lowest_cost_path"].append((f"{origin} => {destination}", min_tuple[1]))
            result["total_price"] = result["total_price"] + min_tuple[1]
            break

        
    print(result)
    

def get_min(prices_dict: dict):
    lowest_cost = sys.maxsize
    for key in prices_dict:
        if prices_dict[key] < lowest_cost:
            destination = key
            lowest_cost = prices_dict[key]
    return (destination, lowest_cost)

    

if __name__ == "__main__":
    origin = DecolarDestinations.BRASILIA
    destinations = [DecolarDestinations.ARACAJU, DecolarDestinations.BELEM, DecolarDestinations.BELO_HORIZONTE, DecolarDestinations.BOA_VISTA, DecolarDestinations.CUIABA]
    date = "2022-12-30"
    start = time.time()
    nearest_neighbour(origin, destinations, date, 10)
    end = time.time()
    print(f"time = {end - start}")
    

        

    
