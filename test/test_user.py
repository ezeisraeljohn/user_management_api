""" This contains all testing done in pythest for the user model"""

from fastapi.testclient import TestClient
from app import app
from model.user import User
from config.dependencies import get_db
from sqlalchemy.orm import Session


client = TestClient(app)


def test_root_response():
    """Test the client response"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "title": "Welcome to the User Management API",
        "description": "This is a simple User Management API",
        "version": "0.1.0",
        "documentation": "/api/v1/docs",
    }


def test_status_response():
    """Test the status response"""
    response = client.get("/status/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_user():
    """Test the create user function"""
    response = client.post(
        "/user/create/",
        json={
            "name": "John Doe",
            "email": "ezeisraeljohn@gmail.com",
            "username": "john_doe",
        },
    )


def test_read_user_by_id():
    """Test the read user by id function"""
    user = User(name="John Doe")
    db = next(get_db())
    db.add(user)
    db.commit()
    db.refresh(user)
    id = user.id
    response = client.get("/user/read/id/", params={"user_id": id})
    assert response.status_code == 200
    assert response.json() == {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "username": user.username,
    }


def test_read_user_by_name():
    """Test the read user by name function"""
    user = User(name="Mary Jane")
    db = next(get_db())
    db.add(user)
    db.commit()
    db.refresh(user)
    name = user.name
    response = client.get("/user/read/name/", params={"name": name})
    assert response.status_code == 200
