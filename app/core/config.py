from pydantic import BaseSettings


class Settings(BaseSettings):

    app_title: str = 'Тестовое задание'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'

    class Config:
        env_file = '..env'

settings = Settings()