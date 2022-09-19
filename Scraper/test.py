from scrap import DecolarDestinations, DecolarScraper

scraper = DecolarScraper()
scraper.get_flight_prices(DecolarDestinations.BRASILIA,DecolarDestinations.PORTO_ALEGRE, "2022-09-30")
