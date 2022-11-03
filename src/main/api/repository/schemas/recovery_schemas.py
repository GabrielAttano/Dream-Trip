from pydantic import BaseModel


class Change_Password_Schema(BaseModel):
    username: str
    email: str
    new_password: str


class Forgot_Password_Schema(BaseModel):
    email: str