import uvicorn
from .config import settings

uvicorn.run(
    'it_barracs.app:app',
    host=settings.SERVER_HOST,
    port=settings.SERVER_PORT,
    reload=True,
)