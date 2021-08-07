import requests

def get_status_code(url):
    req = requests.get(url)
    return req.status_code

def get_content_type(url):
    req = requests.get(url)
    return req.headers['content-type']

def get_encoding(url):
    req = requests.get(url)
    return req.encoding

def get_options(url):
    req = requests.options(url)
    return [req, req.reason]

def get_head(url):
    req = requests.head(url)
    return req.headers