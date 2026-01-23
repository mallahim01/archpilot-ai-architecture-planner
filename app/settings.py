from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://admin:admin123@127.0.0.1:5432/myapp_db"
    JWT_SECRET: str = "change-me-super-secret"
    JWT_ALG: str = "HS256"
    JWT_EXPIRE_HOURS: int = 24

settings = Settings()
