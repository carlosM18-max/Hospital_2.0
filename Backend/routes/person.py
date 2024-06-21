from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

person = APIRouter()
persons: List[BaseModel] = []

class model_person(BaseModel):
    id: int
    name: str
    last_f_name: str
    last_s_name: Optional[str]
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

# Get route
@person.get("/person")
def get_person():
    return persons

# Post route
@person.post("/person")
def save_person(data_person: model_person):
    persons.append(data_person)
    return "Datos guardados correctamente"

# Post route
@person.post("/person{id}")
def get_person(id: int):
    for person in persons:
        if person.id == id:
            return person
    return "Datos guardados correctamente"

# Tarea PUT y DELETE

# Put route
@person.put("/person/{id}")
def update_person(id: int, persona: model_person):
   for index,person in enumerate(persons):
       if person.id == id:
           persona.id = id
           persons[index]
           return "Datos actualizados correctamente"

# Delete route
@person.delete("/person/{id}")
def delete_person(id: int, persona: model_person):
   for index,person in enumerate(persons):
       if person.id == id:
           persona.id = id
           del persons[index]
           return "Datos eliminados correctamente"