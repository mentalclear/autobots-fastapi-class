import requests

# The app's URL 'https://df-react-todo-client-class.herokuapp.com/'
BASE_URL = 'https://df-flask-todo-api-class.herokuapp.com/todos'

# TODO Create these tests for above app's API:

def test_get_todos():
    response = requests.get(BASE_URL)
    assert response.status_code == 200


def test_add_todos():
    pass


def test_delete_todos():
    pass


def test_mark_todos_complete():
    pass
