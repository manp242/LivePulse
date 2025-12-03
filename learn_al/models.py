from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from db import Base

class Questions(Base):
    __tablename__ = 'questions'
    
    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)
    
class Choices(Base):
    __tablename__ = "choices"
    
    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("questions.id"))

