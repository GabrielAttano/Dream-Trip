from pydantic import BaseModel
from model.trip_package.package_model import Package


class User():
    def __init__(self, email: str, username: str, password: str, id: str, creation_date) -> None:
        self.__username = username
        self.__password = password
        self.__id = id
        self.__email = email
        self.__creation_date = creation_date
        self.__packages = list()

    def get_username(self, ):
        return self.__username
    
    def get_password(self, ):
        return self.__password

    def get_email(self, ):
        return self.__email

    def get_id(self, ):
        return self.__id

    def get_creation_date(self, ):
        return self.__creation_date

    def get_packages(self, ):
        return self.__packages
    
    def set_packages(self, package: Package):
        self.__packages.append(package.get_package_id());

    def set_password(self, new_password):
        self.__password = new_password
