from enum import Enum
from service.date_and_time import DateAndTime

class DecolarDestinations(Enum):
    """Class that represents all destinations avaible at https://www.decolar.com/ and their
    abbreviations.
    """

    BRASILIA = "BSB"
    RIO_BRANCO = "RBR"
    MACEIO = "MCZ"
    MACAPA = "MCP"
    MANAUS = "MAO"
    SALVADOR = "SSA"
    FORTALEZA = "FOR"
    VITORIA = "VIX"
    GOIANIA = "GYN"
    SAO_LUIS = "SLZ"
    CUIABA = "CGB"
    CAMPO_GRANDE = "CGR"
    BELO_HORIZONTE = "BHZ"
    BELEM = "BEL"
    JOAO_PESSOA = "JPA"
    CURITIBA = "CWB"
    RECIFE = "REC"
    TERESINA = "THE"
    RIO_DE_JANEIRO = "RIO"
    NATAL = "NAT"
    PORTO_ALEGRE = "POA"
    PORTO_VELHO = "PVH"
    BOA_VISTA = "BVB"
    FLORIANOPOLIS = "FLN"
    SAO_PAULO = "SAO"
    ARACAJU = "AJU"
    PALMAS = "PMW"

class DestinationPackageModel():
    def __init__(self, ) -> None:
        
        self.__start_date = None
        self.__stay_time = 0
        self.__destinations = list()
        self.__start_destination = None
        self.__least_cost_path = list()
        self.__last_scrapped_date = None
        self.__user_id = None
    
    def set_start_date(self, date: str):
        if DateAndTime.is_ISO_format(date):
            self.__start_date = date

    def get_start_date(self, ):
        return self.__start_date

    def set_stay_time(self, stay_time: int):
        if stay_time <= 0:
            return
        self.__stay_time = stay_time

    def get_stay_time(self, ):
        return self.__stay_time

    def set_destinations(self, destination: DecolarDestinations):
        if destination in self.__destinations:
            return
        self.__destinations.append(destination)

    def set_destinations(self, destinations: list):
        for destination in destinations:
            if type(destination) == DecolarDestinations and destination not in self.__destinations:
                self.__destinations.append(destination)

    def get_destinations(self,):
        return self.__destinations

    def set_start_destination(self, start_destination: DecolarDestinations):
        if start_destination not in self.__destinations:
            self.__destinations.append(start_destination)
        self.__start_destination = start_destination
    
    def get_start_destination(self, ):
        return self.__start_destination

    def set_least_cost_path(self, destination: DecolarDestinations, date: str):
        if DateAndTime.is_ISO_format(date):
            self.__least_cost_path.append(destination, date)
    
    def get_least_cost_path(self, ):
        return self.__least_cost_path

    def set_last_scrapped_date(self, date: str):
        if DateAndTime.is_ISO_format(date):
            self.__last_scrapped_date = date
    
    def get_last_scrapped_date(self,):
        return self.__last_scrapped_date

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_user_id(self,):
        return self.__user_id
