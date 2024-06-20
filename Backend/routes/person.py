from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

person = APIRouter()
persons = []

class model_person(BaseModel):
    id:int
    name:str
    last_f_name:str
    last_s_name:Optional[str]
    age: int
    birthday: datetime
    curp: str
    type_blood: str
    created_at: datetime = datetime.now()
    status: bool = False

# Principal route
@person.get("/")

def welcom():
    return "Bienvenido al API del sistema"

# Second route
@person.get("/person")

def get_person():
    return persons

@person.post("/person")

def save_person(data_person: model_person):
    persons.append(data_person)
    return "Datos guardados correectamente"