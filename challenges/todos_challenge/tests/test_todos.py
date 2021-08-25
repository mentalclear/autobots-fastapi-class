import random
from todos.create_todo import create_new_todo
from todos.read_todos import get_response_code, read_all_todos
from todos.utility import get_existing_todo_id
from todos.update_todo import update_todo
from todos.delete_todo import delete_todo


TODOS_URL = 'https://df-flask-todo-api-class.herokuapp.com/todos'
TODO_URL = 'https://df-flask-todo-api-class.herokuapp.com/todo'
rand_num = random.randint(1, 50)


def test_add_todos_returns_statuscode_200():
    payload = {"done": False, "title": f"Post TEST {rand_num}"}
    result = create_new_todo(TODO_URL, payload)

    # Testing for Status code 200
    assert result[1] == 200


def test_add_todos_incomplete_todo_set_false():
    payload = {"done": False, "title": f"Post TEST {rand_num}"}
    result = create_new_todo(TODO_URL, payload)

    # Testing for Done is set to False
    assert result[0]['done'] == False


def test_add_todos_title_is_correct():
    payload = {"done": False, "title": f"Post TEST {rand_num}"}
    result = create_new_todo(TODO_URL, payload)    

    # Testing for the title to be "Post TEST {random number}"
    assert result[0]['title'] == f"Post TEST {rand_num}"


def test_read_todos():    
    result = read_all_todos(TODOS_URL)
    test_dict = [title['title'] for title in result]

    # Testing for status code 
    assert get_response_code(TODOS_URL) == 200

    # Testing that returned list is not empty
    assert len(result) > 0

    # Testing that list element 0 is the size of 3
    assert len(result[0]) == 3

    # Testing that title "Post TEST" present in the test dictionary created
    assert f"Post TEST {rand_num}" in test_dict     


def test_update_todo():
    # Getting an existing ToDo, updating an existing ToDo 
    existing_todo_id = get_existing_todo_id(TODOS_URL)    
    todo_url = f"{TODO_URL}/{str(existing_todo_id)}"
    result = update_todo(todo_url, True)

    # Testing that existing ToDo id is greater than 0
    assert existing_todo_id > 0

    # Testing for response code 200
    assert result[1] == 200

    # Testing that 'done' key in ToDo has been changed from False to True
    assert result[0]['done'] == True


def test_delete_todo():
    existing_todo_id = get_existing_todo_id(TODOS_URL)
    todo_url = f"{TODO_URL}/{str(existing_todo_id)}"
    result = delete_todo(todo_url)

    # Testing for response code 200
    assert result[1] == 200

    # Testing for ToDo delete confirmation text
    assert result[0] == '"Todo Deleted!"'
    