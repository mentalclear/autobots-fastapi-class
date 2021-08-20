import requests
import json

def read_all_todos(url):
    """ This funciton reads all todos from the app using the provided URL"""
    response = requests.get(url)
    results = json.loads(response.text)
    return results
    
def get_response_code(url):
    """ This funciton checks the response code that is returned after a GET request"""
    response = requests.get(url)        
    return response.status_code
