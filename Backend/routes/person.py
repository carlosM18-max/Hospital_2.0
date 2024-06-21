from fastapi import APIRouter, HTTPException
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

# Tarea PUT y DELETE

# Put route
@person.put("/person/{id}")
def update_person(id: int, persona: model_person):
    # Validamos si el id está dentro de la lista persons
    if id >= len(persons) or id < 0:
        # Si el id es mayor o igual a la longitud de la lista o es negativo, lanzara un error
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    # Se actualizara la persona si el id esta en la lista persons
    persons[id] = persona
    return "Datos actualizados correctamente"

# Delete route
@person.delete("/person/{id}")
def delete_person(id: int):
    # Validamos si el id está dentro de la lista persons
    if id >= len(persons) or id < 0:
        # Si el id es mayor o igual a la longitud de la lista o es negativo, lanzara un error
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    # Se eliminara la persona si el id esta en la lista persons
    del persons[id]
    return "Datos eliminados correctamente"