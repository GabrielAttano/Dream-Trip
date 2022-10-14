from pydantic import BaseModel

class CreateUserSchema(BaseModel):
    email: str
    username: str
    password: str

class UserDTO(BaseModel):
    email: str
    username: str
    id: str