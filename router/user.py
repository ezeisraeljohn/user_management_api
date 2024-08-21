""" Create the router for the user """

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from config.dependencies import get_db
from crud.user import (
    create_user,
    get_user_by_name,
    get_user_by_id,
    update_user_by_id,
    update_user_by_name,
    delete_user_by_id,
    delete_user_by_name,
)
from schema.user import UserCreate, User, UserUpdate
from typing import Annotated


router = APIRouter(tags=["User"])


@router.post("/user/", response_model=User)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    """This function creates a new user

    Args:
            user (UserCreate): The user model
            db (Session): A database session

    Returns:
            User: A new user
    """
    return create_user(db, user)


@router.get("/user/read/id/", response_model=User)
def read_user_by_id(user_id: Annotated[int, Query()], db: Session = Depends(get_db)):
    """This function fetches a user by id

    Args:
            user_id: The name of the user
            db (Session): A database session

    Returns:
            User: A user
    """
    return get_user_by_id(user_id=user_id, db=db)


@router.get("/user/read/name/", response_model=User)
def read_user_by_name(
    name: Annotated[str, Query(description="The name passed in as a query parameter")],
    db: Session = Depends(get_db),
):
    """This function fetches a user by name

    Args:
            name (str): The name of the user
            db (Session): A database session

    Returns:
            User: A user
    """
    user = get_user_by_name(name, db)
    return user


@router.put("/user/update/name/", response_model=User)
def edit_user_by_name(
    user: UserUpdate,
    name: Annotated[str, Query(description="The name passed in as a query parameter")],
    db: Session = Depends(get_db),
):
    """This function updates by taking the name as a query parameter

    Args:
            user (UserUpdate): The user model
            name (str): The name of the user
            db (Session): A database session

    Returns:
            User: A user
    """
    user = update_user_by_name(name, db, user)
    return user


@router.put("/user/update/id/", response_model=User)
def edit_user_by_id(
    user: UserUpdate,
    user_id: Annotated[int, Query(description="The id passed in as a query parameter")],
    db: Session = Depends(get_db),
):
    """This function updates user by taking the id as a query parameter

    Args:
            user (UserUpdate): The user model
            user_id: The id of the user
            db (Session): A database session

    Returns:
            User: A user
    """
    user = update_user_by_id(user_id, db, user)
    return user


@router.delete("/user/delete/id/", response_model=dict)
def remove_user_by_id(user_id: Annotated[int, Query()], db: Session = Depends(get_db)):
    """This function deletes a user by id

    Args:
            user_id: The id of the user
            db (Session): A database session

    Returns:
                dict: A dictionary wih the delete message
    """
    return delete_user_by_id(user_id, db)


@router.delete(
    "/user/delete/name/",
    response_model=None,
)
def remove_user_by_name(name: Annotated[str, Query()], db: Session = Depends(get_db)):
    """This function deletes a user by name

    Args:
            name: The name of the user
            db (Session): A database session

    Returns:
            dict: A dictionary wih the delete message
    """
    return delete_user_by_name(name, db)
