from pydantic_settings import BaseSettings

# Configuration settings
class Settings(BaseSettings):
    BASE_URL: str

    TMDB_API_KEY:str
    DATABASE_DRIVERNAME: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    LOG_LEVEL: str = "INFO"

    model_config = {'env_file': '.env', 'env_file_encoding': 'utf-8'}
settings = Settings()


