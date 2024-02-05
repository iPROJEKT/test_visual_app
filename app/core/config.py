from pydantic import BaseSettings


class Settings(BaseSettings):

    app_title: str = 'Тестовое задание'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'

    class Config:
        arbitrary_types_allowed = True
        env_file = '..env'

settings = Settings()
