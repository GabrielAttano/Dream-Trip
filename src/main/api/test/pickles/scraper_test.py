from model.trip_package.package_model import DecolarDestinations
from service.graph.NaiveTSP import naive_tsp
import time
import random
import pickle

def test_scraping_time(total_destinations, stay_time, start_date):
    allDestinations = [x for x in DecolarDestinations]
    destinations = list()
    while len(destinations) < total_destinations:
        newDestination = allDestinations[random.randint(0, len(allDestinations))]
        if newDestination not in destinations:
            destinations.append(newDestination)
    start = time.time()
    naive_tsp(destinations[0], destinations[1:], start_date, stay_time)
    end = time.time()
    return {'destinations': destinations, 'time': (end - start)}

def save_in_pickle(data, file_name):
    file = open(file_name, 'wb')
    pickle.dump(data, file)
    file.close()

def load_pickle(file_name):
    file = open(file_name, 'rb')
    loaded = pickle.load(file)
    file.close()
    return loaded

def average(numbers: list):
    result = 0
    for number in numbers:
        result += number
    return result / len(numbers)
    
result = dict()
for i in range(3, 7):
    resultList = list()
    loaded_pickle = load_pickle(f"timeSpent_{i}DestinationsNormal0.pkl")
    for info in loaded_pickle:
        resultList.append(info["time"])
    result[f"time_{i}destinations"] = resultList
for key in result:
    print(average(result[key]))
