from sqlalchemy.orm import sessionmaker
from app.database.connection import engine


session_local = sessionmaker(bind=engine, autoflush=False)


