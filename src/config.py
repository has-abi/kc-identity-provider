from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict 


class Settings(BaseSettings):
    APP_NAME: str = "auth-service"
    API_PREFIX: str = "/api/auth"
    KC_SERVER_URL: str
    KC_REALM_NAME: str
    KC_CLIENT_ID: str
    KC_CLIENT_SERCRET_KEY: str = ""

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings():
    return Settings()
