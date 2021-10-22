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
from sqlalchemy import schema
from sqlalchemy.orm import Session
from app import models, schemas
from app import crud


def test_create_user(client: TestClient):
    response = client.post(
        "/create-user", json={"username": "Test1", "password": "Test1"}
    )
    data = response.json()
    assert response.status_code == 200
    assert data["id"] is not None


def test_create_user_raises_username_taken(session: Session, client: TestClient):
    user_1 = models.User(username="Test1", password="Test1")
    session.add(user_1)
    session.commit()

    response = client.post(
        "/create-user", json={"username": "Test1", "password": "Test1"}
    )
    data = response.json()
    assert response.status_code == 409
    assert data["detail"] == "Username already registered"


def test_todo_model(session: Session):
    todo = models.ToDo(title="Buy Milk", done=False)
    session.add(todo)
    session.commit()

    todo_db = session.query(models.ToDo).filter(models.ToDo.id == 1).first()
    assert todo_db.title == "Buy Milk"


def test_todo_default_done(session: Session):
    todo = models.ToDo(title="Buy Milk", done=False)
    session.add(todo)
    session.commit()

    todo_db = session.query(models.ToDo).filter(models.ToDo.id == 1).first()
    assert todo_db.done == False


def test_create_todo(session: Session):
    todo_dict = {"title": "Buy milk", "done": False}
    todo = crud.create_todo(db=session, todo=schemas.ToDoCreate(**todo_dict))

    assert todo.id == 1


def test_create_todo_route(client: TestClient):
    # Todo - title and done
    response = client.post("/create-todo", json={"title": "Buy Milk", "done": False})
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 1
    assert data["title"] == "Buy Milk"
    assert data["done"] is False
