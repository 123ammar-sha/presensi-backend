import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# load env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# engine koneksi database
engine = create_engine(DATABASE_URL)
# session databse
SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind=engine)
# Base class tabel ORM
Base = declarative_base()

# dependency ambil sesi database setiap endpoint
def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()