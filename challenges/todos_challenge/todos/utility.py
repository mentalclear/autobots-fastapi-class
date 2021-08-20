import requests
import json

def get_existing_todo_id(url):
    """This function gets an id from an existing ToDo to use later in the update URL"""
    response = requests.get(url)
    results = json.loads(response.text)
    return results[0]["id"]