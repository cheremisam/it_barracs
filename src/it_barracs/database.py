from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={'check_same_thread': False}
)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()

def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
