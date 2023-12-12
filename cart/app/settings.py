from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    postgres_url: str = "postgresql://postgres:password@microservice-postgres-1:5432/cart"

settings = Settings()