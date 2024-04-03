from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dependencies import engine


engine = create_engine("postgresql://postgres:secret@localhost:5432/test_db")
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_docker_engine():
  try:
    db = Session()
    yield db
  finally:
    db.close()