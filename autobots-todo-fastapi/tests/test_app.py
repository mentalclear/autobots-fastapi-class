from fastapi.testclient import TestClient

# import requests
from app.main import app

client = TestClient(app)


def test_root_route():
    # same with requests:
    # response = requests.get("http://localhost:8000")
    # assert response.ok

    response = client.get("/")
    assert response.ok
    assert response.json()["msg"] == "Hello World"
