from sqlalchemy import Column, Integer, String, DATETIME, ForeignKey
from sqlalchemy.orm import relationship
from ..users.models import User

from ..database import Base
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    date = Column(DATETIME, nullable=False)
    text = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship(User, back_populates='posts')
