from fastapi import APIRouter
from service.user.user_service import UserService
from repository.schemas.user_schemas import CreateUserSchema, AuthUserSchema
from repository.schemas.recovery_schemas import ForgotPasswordSchema, RecoverySchema

user_router = APIRouter()

@user_router.post('/user/create')
async def create_user(user: CreateUserSchema):
    return await UserService.create_user(user)

@user_router.get('/user/{user_id}')
async def get_user(user_id: str):
    return await UserService.get_user(user_id)

@user_router.post('/user/forgot_password')
async def forgot_password(forgotPasswordSchema: ForgotPasswordSchema):
    return await UserService.get_user_by_email(forgotPasswordSchema.email);

@user_router.post('/user/change_password')
async def change_password(recoverySchema: RecoverySchema):
    return await UserService.change_password(recoverySchema)

@user_router.post('/user/auth')
async def auth_user(authUserSchema: AuthUserSchema):
    return await UserService.authenticate_user(authUserSchema.email, authUserSchema.password);