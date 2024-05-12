from typing import List

from fastapi import APIRouter, Depends
from . import schemas
from .service import PostsService

router = APIRouter(
    prefix='/posts',
    tags=['posts'],
)

@router.get('/', response_model=List[schemas.Post])
def get_posts(posts_service: PostsService = Depends()):
    return posts_service.get_many()

@router.get('/{post_id}', response_model=schemas.Post)
def get_posts(post_id: int, posts_service: PostsService = Depends()):
    return posts_service.get(post_id)
