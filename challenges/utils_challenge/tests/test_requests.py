from reqs.req_playground import *

base_url = "https://jsonplaceholder.typicode.com/users"

def test_return_code200():
    assert get_status_code(base_url) == 200

def test_get_content_type():
    assert get_content_type(base_url) == 'application/json; charset=utf-8'

def test_get_encoding():
    assert get_encoding(base_url) == 'utf-8'

def test_get_options():
    result = get_options(base_url)
    assert str(result[0]) == "<Response [204]>"
    assert result[1] == 'No Content'

def test_get_head():
    assert get_head(base_url) != None

