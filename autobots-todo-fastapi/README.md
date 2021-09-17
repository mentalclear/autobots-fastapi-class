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
 
