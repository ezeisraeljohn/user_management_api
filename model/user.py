""" This modules handles the creation of the user model
    
"""

from sqlalchemy import Column, Integer, String
from config.database import Base


class User(Base):
    """This class creates a user model"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, index=True, nullable=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True, nullable=True)
    hashed_password = Column(String(225), nullable=True)
