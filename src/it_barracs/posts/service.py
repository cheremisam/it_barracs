from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from ..database import get_session
from . import models


class PostsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_many(self) -> List[models.Post]:
        posts = (
            self.session
            .query(models.Post)
            .all()
        )
        return posts

    def get(self, post_id: int) -> models.Post:
        post = (
            self.session
            .query(models.Post)
            .filter(models.Post.id == post_id)
            .first()
        )
        return post
