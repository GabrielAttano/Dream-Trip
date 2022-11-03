import string
import random
from fastapi import HTTPException
from datetime import date
import re
import uuid
from model.user.user_model import User
from repository.user.user_repository import UserRepository
from repository.schemas.user_schemas import UserDTO, CreateUserSchema
from repository.schemas.recovery_schemas import RecoverySchema


class UserService():

    minimun_length_username = 6
    max_length_username = 20
    minimun_length_password = 10
    max_length_password = 30
    minimun_digits_password = 3
    minimum_special_characters = 1

    @classmethod
    async def create_user(cls, new_user: CreateUserSchema):

        if not cls.__is_valid_username(new_user.username):
            return HTTPException(400, detail="Invalid Username")
        if not cls.__is_valid_password(new_user.password):
            return HTTPException(400, detail="Invalid Password")
        if not cls.__is_valid_email(new_user.email):
            return HTTPException(400, detail="Invalid Email")

        userRepository = UserRepository.instance()
        for user in userRepository.get_users():
            if user.get_username() == new_user.username:
                return HTTPException(400, detail="Username already exists")
            if user.get_email() == new_user.email:
                return HTTPException(400, detail="Email already in use")

        user = User(new_user.email, new_user.username, new_user.password, str(uuid.uuid4()), str(date.today()))
        userRepository.set_user(user)
        return UserDTO(
            email=user.get_email(),
            username=user.get_username(),
            id=user.get_id()
        )
    
    @classmethod
    async def get_user(cls, user_id: str):
        userRepository: UserRepository = UserRepository.instance()
        for user in userRepository.get_users():
            if user.get_id() == user_id:
                return UserDTO(
                    email=user.get_email(),
                    username=user.get_username(),
                    id=user.get_id()
                )
        return HTTPException(400, detail="User not found")

    @classmethod
    async def get_user_by_email(cls, email: str):
        userRepository: UserRepository = UserRepository.instance()
        for user in userRepository.get_users():
            if user.get_email() == email:
                return UserDTO(
                    email=user.get_email(),
                    username=user.get_username(),
                    id=user.get_id()
                )
        return HTTPException(400, detail="User not found")

    @classmethod
    async def change_password(cls, request: RecoverySchema):
        userRepository: UserRepository = UserRepository.instance()
        for user in userRepository.get_users():
            if user.get_id() == request.user_id:
                print(f"old password = {user.get_password()}")
                user.set_password(request.new_password)
                print(f"new password = {user.get_password()}")
                return UserDTO(
                    email=user.get_email(),
                    username=user.get_username(),
                    id=user.get_id()
                )
        return HTTPException(400, detail="User not found")

    @classmethod
    async def authenticate_user(cls, email: str, password: str):
        userRepository: UserRepository = UserRepository.instance()
        for user in userRepository.get_users():
            if user.get_email() == email:
                if user.get_password() == password:
                    return UserDTO(
                        email=user.get_email(),
                        username=user.get_username(),
                        id=user.get_id()
                    )
                else:
                    return HTTPException(400, detail="Invalid password")
        return HTTPException(400, detail="No users found with the specified email");


    @classmethod
    def __is_valid_email(cls, email: str):
        if re.search(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email):
            return True
        else:
            return False

    @classmethod
    def __is_valid_username(cls, username: str):

        if len(username) < cls.minimun_length_username or len(username) > cls.max_length_username:
            return False # Invalid length error
        if re.search(r"[^[a-zA-Z0-9_]+$", username):
            return False # Special character error

        return True
    
    @classmethod
    def __is_valid_password(cls, password: str):

        if len(password) < cls.minimun_length_password or len(password) > cls.max_length_password:
            return False
        if re.search(r"[^[a-zA-Z0-9]+$", password):
            return False

        numbers = sum(c.isdigit() for c in password)
        if numbers < cls.minimun_digits_password:
            return False
        
        special_characters = sum(not c.isdigit() and not c.isalpha() for c in password)
        if special_characters < cls.minimum_special_characters:
            return False
        
        return True


def generateRecoveryCode():
    new_code = ''
    minusculas = string.ascii_lowercase
    maiusculas = string.ascii_uppercase
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(7):
        new_code = new_code + minusculas[random.randrange(len(minusculas))]
    new_code = new_code + maiusculas[random.randrange(len(maiusculas))]
    new_code = new_code + numeros[random.randrange(len(numeros))]
    return new_code