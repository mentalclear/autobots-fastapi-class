import requests

def delete_todo(url):
    """ 
    This function deleted a ToDo by url provided 
    and returns response text and status code
    """
    response = requests.delete(url)
    return ((response.text).strip(), response.status_code)
