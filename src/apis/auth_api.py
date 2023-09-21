from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from src.containers import Container
from src.services.auth_service import AuthService
from src.schemas.user import UserLogin
from src.schemas.token import AccessToken, RefreshToken


auth_router = APIRouter()

@auth_router.post("/login", response_model=AccessToken)
@inject
def login(user: UserLogin, auth_service: AuthService = Depends(Provide[Container.auth_service])):
    return auth_service.login(user)


@auth_router.post("/refresh-token", response_model=AccessToken)
@inject
def login(token: RefreshToken, auth_service: AuthService = Depends(Provide[Container.auth_service])):
    return auth_service.refresh_token(token)


@auth_router.post("/logout")
@inject
def login(token: RefreshToken, auth_service: AuthService = Depends(Provide[Container.auth_service])):
    return auth_service.logout(token)