from datetime import date

from pydantic import BaseModel
from ..users.schemas import User

class BasePost(BaseModel):
    date: date
    text: str
    user_id: int

class PostCreate(BasePost):
    pass

class PostUpdate(BasePost):
    pass

class Post(BasePost):
    id: int
    user: User

    class Config:
        orm_mode = True
