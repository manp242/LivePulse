from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# URL to our DB
URL_DATABASE = 'postgresql://postgres:postgre@localhost:5432/LivePulse_1'

## creates the SQLAlchemy Engine
#   - used to communicate with SQL
#   - does NOTTT run queries or CRUD tables 
engine = create_engine(URL_DATABASE)

# creates a session per CRUD request basically
SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind=engine)


Base = declarative_base()