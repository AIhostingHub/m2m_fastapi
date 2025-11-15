
import os
from pydantic_settings import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

APP_DIR = os.path.dirname(os.path.abspath(__file__))

class Settings(BaseSettings):
    db_user: str = "horizen"
    db_pass: str = "Horizen"
    db_host: str = "127.0.0.1"
    db_port: int = 3306
    db_name: str = "m2m"

    class Config:
        env_file = os.path.join(APP_DIR, ".env")
        env_file_encoding = "utf-8"

settings = Settings()

DATABASE_URL = (
    f"mysql+pymysql://{settings.db_user}:{settings.db_pass}"
    f"@{settings.db_host}:{settings.db_port}/{settings.db_name}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False,
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
