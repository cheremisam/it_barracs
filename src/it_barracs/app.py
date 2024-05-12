from fastapi import FastAPI

from . import api

tags_metadata = [
    {
        'name': 'posts',
        'description': 'Создание, редактирование, удаление и просмотр постов.'
    },
]

app = FastAPI(
    title='It Barracs',
    description='Сервис для отработки навыков CRUDошлепства',
    version='1.0.0',
    openapi_tags=tags_metadata,
)

app.include_router(api.router)
