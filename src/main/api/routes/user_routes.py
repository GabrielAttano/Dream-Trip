from fastapi import APIRouter
from service.user.user_service import UserService
from repository.schemas.user_schemas import CreateUserSchema

user_router = APIRouter()

@user_router.post('/user/create')
async def create_user(user: CreateUserSchema):
    return await UserService.create_user(user)

@user_router.get('/user/{user_id}')
async def get_user(user_id: str):
    return await UserService.get_user(user_id)