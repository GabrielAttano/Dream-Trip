from model.user.user_model import User

class UserRepository():

    _instance = None

    def __init__(self, ) -> None:
        self.__users_in_memory = list()
    
    @classmethod
    def instance(cls, ):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def get_users(self, ):
        return self.__users_in_memory

    def set_user(self, user: User):
        self.__users_in_memory.append(user)