# from fastapi.testclient import TestClient

# # import requests
# from app.main import app

# client = TestClient(app)


# def test_root_route():
#     # same with requests:
#     # response = requests.get("http://localhost:8000")
#     # assert response.ok

#     response = client.get("/")
#     assert response.ok
#     assert response.json()["msg"] == "Hello World"
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app import models

def test_create_user(client: TestClient):
    response  = client.post(
        "/create-user", json={"username":"Test1", "password":"Test1"}
    )
    data = response.json()
    assert response.status_code == 200
    assert data['id'] is not None
    

def test_create_user_raises_username_taken(session: Session, client: TestClient):
    user_1 = models.User(username="Test1", password="Test1")
    session.add(user_1)
    session.commit()

    response = client.post(
        "/create-user",  json={"username":"Test1", "password":"Test1"}
    )    
    data = response.json()
    assert response.status_code == 409
    assert data['detail'] == "Username already registered"