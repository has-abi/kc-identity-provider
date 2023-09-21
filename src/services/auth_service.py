from keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakAuthenticationError, KeycloakPostError
from fastapi import HTTPException, status

from src.schemas.user import UserLogin
from src.schemas.token import RefreshToken, AccessToken
from src import logger


class AuthService:
    def __init__(self, keycloak_openid: KeycloakOpenID) -> None:
        self.keycloak_openid = keycloak_openid

    def login(self, user: UserLogin) -> AccessToken:
        try:
            token = self.keycloak_openid.token(user.email, user.password)
        except KeycloakAuthenticationError as kc_error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid user credentials"
            ) from kc_error
        logger.info("User login: %s", user.email)
        return AccessToken(**token)
    
    def refresh_token(self, token: RefreshToken) -> AccessToken:
        try:
            new_token = self.keycloak_openid.refresh_token(refresh_token=token.refreshToken)
        except KeycloakPostError as kc_error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid refresh token"
            ) from kc_error
        return AccessToken(**new_token)
    
    def logout(self, token: RefreshToken) -> None:
        try:
            self.keycloak_openid.logout(refresh_token=token.refreshToken)
        except KeycloakPostError as kc_error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid refresh token"
            ) from kc_error