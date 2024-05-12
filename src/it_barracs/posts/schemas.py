from datetime import date

from pydantic import BaseModel
from ..users.schemas import User

class BasePost(BaseModel):
    date: date
    text: str

class PostCreate(BasePost):
    user_id: int

class PostUpdate(BasePost):
    user_id: int

class Post(BasePost):
    id: int
    user: User

    class Config:
        orm_mode = True
