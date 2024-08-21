""" This module handles the database configuration"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


Base = declarative_base()

engine = create_engine("sqlite:///users.db")

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
