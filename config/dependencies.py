""" This houses the get_db function that returns a database session"""

from sqlalchemy.orm import Session
from fastapi import Depends
from config.database import SessionLocal
from typing import Any
from passlib.context import CryptContext


def get_db() -> Session:
    """Returns a database session

    Returns:
            db: A database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
