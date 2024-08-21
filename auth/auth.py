""" This module contains the all security details """

from passlib.context import CryptContext

pwd_content = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """This hashes the user's password"""
    return pwd_content.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """This verifies a password"""
    bool_value = pwd_content.verify(password, hashed_password)
    return bool_value
