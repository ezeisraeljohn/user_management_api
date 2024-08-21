""" This module contains the CRUD Operation for the user model
   - create_user: This function creates a new user
   - get_user_by_name: This function fetches a user by name
   - get_user_by_id: This function fetches a user by id
"""

from config.dependencies import get_db
from model.user import User
from sqlalchemy.orm import Session
from schema.user import UserCreate, UserUpdate
from auth.auth import hash_password, verify_password
from fastapi import HTTPException
from fastapi import status


def create_user(db: Session, user: UserCreate):
    """This function creates a new user

    Args:
            db (Session): A database session

    Returns:
            User: A new user
    """
    credentials = user.model_dump()
    if user.password:
        hashed_password = hash_password(user.password)
        new_user = User(
            name=credentials.get("name"),
            email=credentials.get("email", None),
            username=credentials.get("username", None),
            hashed_password=hashed_password,
        )
    else:
        new_user = User(
            name=credentials.get("name"),
            email=credentials.get("email", None),
            username=credentials.get("username", None),
        )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_name(name: str, db: Session) -> User:
    """This function fetches a user by name

    Args:
            name (str): The name of the user
            db (Session): A database session

    Returns:
            User: A user
    """
    user = db.query(User).filter(User.name == name).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


def get_user_by_id(user_id: int, db: Session) -> User:
    """This method fetches a user by id

    Args:
            user_id (int): The id of the user
            db (Session): A database session

    Returns:
            User: A user
    """

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


def update_user_by_id(user_id: int, db: Session, user: UserUpdate) -> User:
    """This updates the user by id"""
    db_user = db.query(User).filter(User.id == user_id).first()
    user_dict = user.model_dump()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    for key, value in user_dict.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def update_user_by_name(name: str, db: Session, user: UserUpdate) -> User:
    """This updates the user by id"""
    db_user = db.query(User).filter(User.name == name).first()
    user_dict = user.model_dump()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    for key, value in user_dict.items():
        setattr(db_user, key, value)

    db.commit()
    return db_user


def delete_user_by_id(user_id: int, db: Session) -> dict:
    "This function deletes a user and returns an empty response"
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}


def delete_user_by_name(name: str, db: Session) -> dict:
    """This function deletes a user and a message indicating deletion"""
    user = db.query(User).filter(User.name == name).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
