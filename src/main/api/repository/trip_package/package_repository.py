from model.trip_package.package_model import Package

class PackageRepository():

    _instance = None

    def __init__(self, ) -> None:
        self.__trip_packages = list()
    
    @classmethod
    def instance(cls, ):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def get_trip_packages(self, ):
        return self.__trip_packages

    def set_trip_package(self, trip_package: Package):
        self.__trip_packages.append(trip_package)