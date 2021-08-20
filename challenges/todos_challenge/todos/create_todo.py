import requests
import json


def create_new_todo(url, payload):
    """ 
    This function sends a POST request to the provided URL using provided payload. 
    Expected paload: {"done": True/False, "title": "{Some Title}"}
    Returns a tuple with a response dictionary and the status code
    """
    response = requests.post(url, json=payload)
    content = json.loads(response.text)
    return (content, response.status_code)
