from typing import List, Optional, Annotated
from uuid import uuid4
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .models import users



app = FastAPI()
users.Base.metadata.create_all(bind=engine)
########## CLASSES


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

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


## DB FOR NOW
people = []

### CREATE
# @app.post("/person", response_model=Person)
# def create_person(data: PersonInput):
#     newPerson = Person(
#         id = str(uuid4()),
#         **data.model_dump()
#         )
#     people.append(newPerson)
#     return newPerson


### actual connection to DB
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



#### READ
@app.get("/")
def get_people(db: db_dependency):
    users_list = db.query(users.User).all()
    return users_list
    

### UPDATE
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


### DELETE
@app.delete("/person/{person_id}")
def delete_person(person_id: str):
    for index, person in enumerate(people):
        if person_id == person.id:
            delt = people.pop(index)
            return delt
    raise HTTPException(status_code=404, detail="Person not found")
