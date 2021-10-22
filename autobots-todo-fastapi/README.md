# Autobots FastAp Todo API

This repo is in conjunction with autobots.

## Setup
- Clone the repo
- Run `poetry install`


## Start the local server with following command:
` poetry run uvicorn app.main:app --reload `


## Request Body

- **User**
 - username: str  
 - password: str 
 - created_at: date_time
 - updated_at: date_time
 - todos Array[Todos]
- **ToDo**
 - title: str
 - done: Bool
 

 ## Homework

 - Get a user 
 - Get a todo
 - Update a todo done
 - Delete a todo

 ### To run code coverage: 
`poetry run pytest --cov-report html:html_cov_report --cov=app tests/`
`poetry run pytest --cov-report term --cov=app tests/`

