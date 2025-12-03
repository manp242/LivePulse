from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Sequence, JSON
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from ..database import Base
import uuid


class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    email = Column(String, index=True)
    hobbies = Column(JSON)
    # age = Column(Integer, index=True)
    # phone = Column(Integer, index=True)
    # profession = Column(String, index=True)
    # interests = Column(String, index=True)
    # preferences = Column(String, index=True)


