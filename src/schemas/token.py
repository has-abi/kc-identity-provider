from pydantic import BaseModel

class AccessToken(BaseModel):
    access_token: str
    expires_in: int
    refresh_expires_in: int
    refresh_token: str

class RefreshToken(BaseModel):
    refreshToken: str