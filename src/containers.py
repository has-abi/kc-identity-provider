from dependency_injector import containers, providers
from keycloak import KeycloakOpenID

from src.config import get_settings
from src.services.auth_service import AuthService

settings = get_settings()


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["src.apis"]
    )
    keycloak_openid = providers.Singleton(KeycloakOpenID, 
                                          server_url=settings.KC_SERVER_URL,
                                          realm_name=settings.KC_REALM_NAME,
                                          client_id=settings.KC_CLIENT_ID,
                                          client_secret_key=settings.KC_CLIENT_SERCRET_KEY)
    auth_service = providers.Singleton(AuthService, keycloak_openid=keycloak_openid)