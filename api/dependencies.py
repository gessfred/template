from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB_PORT = os.getenv("DB_PORT", 5432)
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

engine_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@db-postgresql-fra1-33436-do-user-6069962-0.b.db.ondigitalocean.com:{DB_PORT}/{DB_NAME}"
engine = create_engine(engine_url)

Base = declarative_base()
#

SessionLocal = sessionmaker(bind=engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()