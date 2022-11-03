from fastapi import APIRouter
from service.user.user_service import UserService
from repository.schemas.user_schemas import CreateUserSchema
from repository.schemas.recovery_schemas import Change_Password_Schema ,Forgot_Password_Schema

user_router = APIRouter()


@user_router.post('/user/create')
async def create_user(user: CreateUserSchema):
    return await UserService.create_user(user)


@user_router.get('/user/{user_id}')
async def get_user(user_id: str):
    return await UserService.get_user(user_id)


@user_router.post('/user/forgot_password')
async def forgot_password(email: Forgot_Password_Schema):
    return await UserService.get_user_by_email(email)

@user_router.post('/user/change_password')
async def change_password(request:  Change_Password_Schema):
    return await UserService.change_password(request)