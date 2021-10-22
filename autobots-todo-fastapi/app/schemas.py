from typing import Optional
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Boolean


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class ToDoBase(BaseModel):
    title: str


class ToDoCreate(ToDoBase):
    done: Optional[bool]


class ToDo(ToDoBase):
    id: int
    done: bool

    class Config:
        orm_mode = True
