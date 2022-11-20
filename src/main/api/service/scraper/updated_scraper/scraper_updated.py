from model.trip_package.package_model import DecolarDestinations

# Scrap imports
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
# manager to install the latest chrome drivre
from webdriver_manager.chrome import ChromeDriverManager
# Threading
from concurrent.futures import ThreadPoolExecutor, wait

def run_process(url):
    driver = get_driver(True)
    if connect_to_base(driver, url):
        costs = parse_html(driver.page_source)
        driver.quit()
        return costs
    else:
        driver.quit()

def connect_to_base(driver, url):
    connection_attempts = 0
    while connection_attempts <= 3:
        try:
            driver.get(url)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "item-detail")))
            return True
        except Exception as e:
            print(e)
            connection_attempts += 1
    return False

def parse_html(html):
    # Faz o parse do html e retorna uma list com os valores
    soup = BeautifulSoup(html, "lxml")
    costs = list()
    for final_price in soup.find_all("p", class_="item-fare fare-price"):
        final_price_amount = final_price.find("span", class_="amount price-amount").text
        costs.append(int(final_price_amount.replace(".", "")))
    return costs

def format_search_url( base_url, start_destination: DecolarDestinations, end_destination: DecolarDestinations, departure_date):
    url = base_url + start_destination.value + "/" + \
            end_destination.value + "/" + departure_date + "/1/0/0"
    return url

def get_driver(headless = False):
    if headless:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(ChromeDriverManager().install(), options= options)
        return driver
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        return driver

def concurrent_scrap(base_url, end_destination, destinations, date):
    if isinstance(destinations, DecolarDestinations):
        costs = run_process(format_search_url(base_url, destinations, end_destination, date))
        return {destinations: min(costs)}
    future = []
    with ThreadPoolExecutor() as executor:
        for number in range(0, len(destinations)):
            future.append(executor.submit(
                run_process, 
                format_search_url(base_url, destinations[number], end_destination, date)
            ))

    # Esperando todos os scraps
    wait(future)

    # Setando um dict com os valores (Key = nome do destino, value = menor preço)
    costs_dict = {}
    counter = 0
    for i in future:
        cost = min(i.result()) # função para pegar o return no future
        costs_dict[destinations[counter]] = cost # Adicionando cost no dict
        counter += 1
    return costs_dict

if __name__ == "__main__":

    base_url = "https://www.decolar.com/shop/flights/results/oneway/"

    # variables
    origin = DecolarDestinations.BRASILIA
    destinations = [DecolarDestinations.ARACAJU, DecolarDestinations.BELEM, DecolarDestinations.BOA_VISTA]
    date = "2022-12-30"

    result = concurrent_scrap(base_url, origin, destinations, date)
    print(result)