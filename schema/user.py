""" This module contains the pydantic schema for the user model"""

from pydantic import BaseModel, Field
from typing import Annotated, Optional


class UserBase(BaseModel):
    """This class creates a user base schema"""

    email: Annotated[
        Optional[str],
        Field(
            default=None,
            description="The email of the user",
        ),
    ]
    name: Annotated[str, Field(default=None, description="The name of the user")]

    username: Annotated[
        Optional[str],
        Field(default=None, description="The username of the user"),
    ]


class UserCreate(UserBase):
    """This class creates a user create schema"""

    password: Annotated[
        Optional[str],
        Field(
            default=None,
            description="The password of the user",
            min_length=8,
            max_length=16,
        ),
    ]
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "John Doe",
                "email": "johndoe@gmail.com",
                "username": "john_doe",
                "id": 1,
            }
        }
    }


class UserUpdate(UserBase):
    """This updates the user"""

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "John Doe",
                "email": "johndoe@gmail.com",
                "username": "john_doe",
                "id": 1,
            }
        }
    }


class User(UserBase):
    """This is the user schema"""

    id: Annotated[
        int,
        Field(
            description="The id of the user",
        ),
    ]
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "John Doe",
                "email": "johndoe@gmail.com",
                "username": "john_doe",
                "id": 1,
            }
        }
    }

    class ConfigDict:
        from_attributes = True
