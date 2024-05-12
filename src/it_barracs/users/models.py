from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password_hash", String, nullable=False)
)
