import uuid
from fastapi import HTTPException
from datetime import date
from repository.schemas.package_schemas import PackagesSchema, PackageDTO
from repository.trip_package.package_repository import PackageRepository
from model.trip_package.package_model import DecolarDestinations, Package
from service.date_and_time import DateAndTime
from service.scraper.scraper_service import DecolarScraper
from service.graph.NaiveTSP import naive_tsp

class PackageService():

    @classmethod
    async def create_package(cls, package: PackagesSchema):

        if not cls.__is_valid_start_date(package):
            return HTTPException(400, detail="Invalid start date")
        if package.start_destination in package.destinations:
            return HTTPException(400, detail="Start destination shouldnt be on the destinations list")

        new_package = Package(
            start_date=package.start_date,
            stay_time=package.stay_time,
            destinations=package.destinations,
            start_destination=package.start_destination,
            user_id = package.user_id,
            package_id=str(uuid.uuid4())
        )

        package_repository = PackageRepository.instance()
        package_repository.set_trip_package(new_package)

        return PackageDTO(
                    start_date=new_package.get_start_date(),
                    stay_time=new_package.get_stay_time(),
                    destinations=new_package.get_destinations(),
                    start_destination=new_package.get_start_destination(),
                    least_cost_path=new_package.get_least_cost_path(),
                    user_id=new_package.get_user_id(),
                    package_id=new_package.get_package_id()
                )

    @classmethod
    async def get_package(cls, package_id: str):
        package_repository = PackageRepository.instance()
        for package in package_repository.get_trip_packages():
            if package.get_package_id() == package_id:
                return PackageDTO(
                    start_date=package.get_start_date(),
                    stay_time=package.get_stay_time(),
                    destinations=package.get_destinations(),
                    start_destination=package.get_start_destination(),
                    least_cost_path=package.get_least_cost_path(),
                    user_id=package.get_user_id(),
                    package_id=package.get_package_id()
                )
        return HTTPException(400, detail="Invalid package id")

    @classmethod
    async def update_package(cls, package_id: str):
        
        package_repository = PackageRepository.instance()
        for package in package_repository.get_trip_packages():
            if package.get_package_id() == package_id:
                destinations_list = cls.__parse_list_to_destinations(package.get_destinations())
                print(destinations_list)
                start_destination = cls.__parse_string_to_destinations(package.get_start_destination())
                print(start_destination)
                result = naive_tsp(
                    start_destination, 
                    destinations_list, 
                    package.get_start_date(), 
                    package.get_stay_time()
                )
                package.set_least_cost_path(result)
                package.set_last_scrapped_date(str(date.today()))
                return result
        return HTTPException(400, detail="Invalid package id")
                
    @classmethod
    def __parse_string_to_destinations(cls, string: str):

        for destination in DecolarDestinations:
            if string == destination.value:
                return destination

    @classmethod
    def __parse_list_to_destinations(cls, destinations: list):

        result = list()
        for destination in destinations:
            parsed_destination = cls.__parse_string_to_destinations(destination)
            if parsed_destination:
                result.append(parsed_destination)
            else:
                return None
        
        return result
        
    @classmethod
    def __is_valid_start_date(cls, package: PackagesSchema):

        if not DateAndTime.is_ISO_format(package.start_date):
            return False # Start Date not in ISO format 
        if date.fromisoformat(package.start_date) < date.today():
            return False # Start date must be after {str(date.today())}
        return True
        