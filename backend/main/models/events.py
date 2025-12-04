from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Sequence, JSON
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from ..database import Base
import uuid



class Events(Base):
    __tablename__ = "events"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, index=True)
    summary = Column(String, index=True)
    keywords = Column(JSON)
    
    
    ### LATER ADD: 
        # event_time
        # where??
        # other stuff ask chat 
    
    ## first_detected_at, last_updated_at, trend_score, source_count, status
    
    


