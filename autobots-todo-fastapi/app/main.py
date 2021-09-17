from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.main import create_model

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

@app.post("/create-user", response_model=UserOut)
async def create_user(user: UserIn):
    return user