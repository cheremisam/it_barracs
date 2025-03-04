from datetime import date

from pydantic import BaseModel

class BaseUser(BaseModel):
    email: str
    username: str

class UserCreate(BaseUser):
    password: str

class User(BaseUser):
    id: int

    class Config:
        orm_mode = True
