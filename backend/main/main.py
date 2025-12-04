
from uuid import uuid4
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from .database import engine, SessionLocal
from typing import List, Optional, Annotated
from sqlalchemy.orm import Session
from .models import users
from .models import events
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
users.Base.metadata.create_all(bind=engine)
########## CLASSES

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # your React/Vite frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


## user input of person
class PersonInput(BaseModel):
    name: str
    email: str
    # age: int
    # profession: Optional[str]
    # phone: Optional[int]
    hobbies: List[str] = Field(default_factory=list)
    # interests: Optional[List[str]] = Field(default_factory=list)
    # preferences: Optional[List[str]] = Field(default_factory=list)

## my_person with ID
class Person(PersonInput):
    id: str
    
    class Config:
        from_attributes = True

### updatePerson model
class PersonUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    profession: Optional[str] = None
    phoneNumber: Optional[int] = None
    hobbies: Optional[List[str]] = None
    interests: Optional[List[str]] = None
    preferences: Optional[List[str]] = None

class EventsInput(BaseModel):
    title: str
    summary: str
    keywords: List[str] = Field(default_factory=list)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

######################################## EVENTS ########################################

### Create events
@app.post("/events", response_model=EventsInput)
def create_event(event: EventsInput, db: db_dependency):
    new_event = events.Events(
        title = event.title,
        summary=event.summary,
        keywords=event.keywords
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

## Delete events
@app.delete("/events/{event_id}")
def delete_event(event_id: str, db: db_dependency):
        delete = db.query(events.Events).filter_by(id=event_id).delete()
        db.commit()
        if delete == 0:
            raise HTTPException(status_code=404, detail="Event not found")
        else:
            return delete

## Read all events
@app.get("/events")
def read_events(db: db_dependency):
    ev = db.query(events.Events).all()
    return ev

### Read particular
@app.get("/events/{event_id}")
def read_event(event_id: str, db: db_dependency):
        ev = db.query(events.Events).filter(events.Events.id == event_id).first()
        return ev






######################################## USER ################################


### Add Person
@app.post("/person", response_model=Person)
async def create_person(data: PersonInput, db: db_dependency):
    
    new_user = users.User(
        name=data.name,
        email=data.email,
        hobbies=data.hobbies
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


#### READ Person
@app.get("/")
def get_people(db: db_dependency):
    users_list = db.query(users.User).all()
    return users_list
   
   

### DELETE Person
@app.delete("/person/{person_id}")
def delete_person(person_id: str, db: db_dependency):
    for index, person in enumerate(db.query(users.User)):
        if person_id == person.id:
            delt = db.query(users.User).filter_by(id=person_id).delete()
            db.commit()
            # db.refresh()
            return delt
    raise HTTPException(status_code=404, detail="Person not found")
 

### UPDATE Person ---- NEED TO DO
# @app.put("/person/{person_id}")
# def change_info(person_id: str, new_person: PersonUpdate):
#     for index, person in enumerate(people):
#         if person.id == person_id:
#             # for the updated person it'll dump the old stuff and change whatever's new basically
#             updated = person.model_copy(
#                 update=new_person.model_dump(exclude_unset=True)
#             )
#             people[index] = updated
#             return updated
#     raise HTTPException(status_code=404, detail="Person not found")

