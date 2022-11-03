from pydantic import BaseModel
from model.user.user_model import User

class CreateUserSchema(BaseModel):
    email: str
    username: str
    password: str

class AuthUserSchema(BaseModel):
    email: str
    password: str

class UserDTO(BaseModel):
    email: str
    username: str
    packages: list
    creation_date: str
    id: str

def parseUserToDTO(user: User):
    return UserDTO(
        email=user.get_email(),
        username=user.get_username(),
        packages=user.get_packages(),
        creation_date=user.get_creation_date(),
        id=user.get_id()
    )
