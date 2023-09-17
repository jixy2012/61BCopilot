from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv('../.env')

load_dotenv()

DATABASE_URL = os.getenv("POSTGRESQL_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
