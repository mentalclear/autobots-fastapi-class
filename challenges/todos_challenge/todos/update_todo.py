import requests
import json

def update_todo(url, value):
    """This function updates and existing ToDo from False to True"""
    response = requests.patch(url, json={"done": value})
    result = json.loads(response.text)
    return (result, response.status_code)
