from pydantic import BaseModel
from typing import List


class User(BaseModel):
    name: str
    age: int
    email: str

    class Config:
        orm_mode = True


class Game(BaseModel):
    name: str

    class Config:
        orm_mode = True


class UserSchema(User):
    games: List[Game]


class GameSchema(Game):
    users: List[User]
