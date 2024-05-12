from sqlalchemy import MetaData, Table, Column, Integer, String, DATETIME, ForeignKey
from src.it_barracs.users.models import users

metadata = MetaData()

posts = Table(
    'posts',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("date", DATETIME, nullable=False),
    Column("text", String, nullable=False),
    Column("user_id", Integer, ForeignKey(users.c.id))
)
