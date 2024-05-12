from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = '8000'

    DATABASE_URL: str


settings = AppSettings()
