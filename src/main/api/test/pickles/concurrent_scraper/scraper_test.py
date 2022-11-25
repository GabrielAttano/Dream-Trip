from model.trip_package.package_model import DecolarDestinations
from service.graph.NaiveTSP import naive_tsp, nearest_neighbor
import time
import random
import pickle

def get_random_destinations(total_destinations):
    allDestinations = [x for x in DecolarDestinations]
    destinations = list()
    while len(destinations) < total_destinations:
        newDestination = allDestinations[random.randint(0, len(allDestinations) - 1)]
        if newDestination not in destinations:
            destinations.append(newDestination)
    return destinations

def test_scraping_time(total_destinations, stay_time, start_date):
    destinations = get_random_destinations(total_destinations)
    start = time.time()
    naive_tsp(destinations[0], destinations[1:], start_date, stay_time)
    end = time.time()
    return {'destinations': destinations, 'time': (end - start)}

def test_concurrent_scraping_time(total_destinations, stay_time, start_date):
    destinations = get_random_destinations(total_destinations)
    print(destinations)
    start = time.time()
    nearest_neighbor(destinations[0], destinations[1:], start_date, stay_time)
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

# start_date = "2022-11-30"
# stay_time = 5
# file_name = f"concurrent_6Destinations1.pkl"
# result = list()
# for j in range (0, 15):
#     print(f"scrap test {j}")
#     result.append(test_concurrent_scraping_time(6, stay_time, start_date))
#     print(f"scraped test {j} finished")
# save_in_pickle(result, file_name)




# result = dict()
# for i in range(3, 6):
#     resultList = list()
#     loaded_pickle = load_pickle(f"concurrent_{i}Destinations.pkl")
#     for info in loaded_pickle:
#         resultList.append(info["time"])
#     result[f"time_{i}destinations"] = resultList
# for key in result:
#     print(average(result[key]))

# use this to get average
result = list()
loaded_pickle = load_pickle(f"concurrent_6destinations.pkl")
for info in loaded_pickle:
    result.append(info['time'])
loaded_pickle = load_pickle(f"concurrent_6destinations1.pkl")
for info in loaded_pickle:
    result.append(info['time'])

result.remove(result[0])
print(average(result))
