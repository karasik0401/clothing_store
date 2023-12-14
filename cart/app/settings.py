from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from pydantic import Field

load_dotenv()

class Settings(BaseSettings):
    postgres_url: str = Field(env='POSTGRES_URL')
    

settings = Settings()
