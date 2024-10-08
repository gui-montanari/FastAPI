from typing import ClassVar
from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DBBaseModel: ClassVar[DeclarativeMeta] = declarative_base()
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:postgres@localhost:5432/faculdade'

    JWT_SECRET: str = '8ML-vlZOlPnpZOFfX3jswVdgWQZA0nFFRTbGEGw3RZw'
    """
    import secrets

    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'
    # 60 minutos * 24 horas * 7 dias => 1 SEMANA
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings = Settings = Settings()

