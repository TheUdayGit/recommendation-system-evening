from sqlalchemy import create_engine, URL
from app.core.config import settings

# database url for "MYSQL"

database_url = URL.create(drivername=settings.DATABASE_DRIVERNAME,
                          username=settings.DATABASE_USER,
                          password=settings.DATABASE_PASSWORD,
                          host=settings.DATABASE_HOST,
                          database=settings.DATABASE_NAME,
                          port=settings.DATABASE_PORT,
                          )
engine = create_engine(url=database_url, echo=(settings.LOG_LEVEL == 'debug'))
