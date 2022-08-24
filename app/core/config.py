from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    RELATIONAL_DB_USER: str
    RELATIONAL_DB_PASSWORD: str
    RELATIONAL_DB_HOST: str
    RELATIONAL_DB_PORT: int
    RELATIONAL_DB_NAME: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    SYSTEM_USER_ID: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
