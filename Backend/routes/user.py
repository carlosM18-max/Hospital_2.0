from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

user = APIRouter()
users: List[BaseModel] = []

class model_user(BaseModel):
    id: int
    user: str
    password: str
    persona_ID: int
    status: bool = False
    created_at: datetime = datetime.now()
    
# Get route
@user.get("/user")
def get_user():
    return users

# Post route
@user.post("/user")
def save_user(data_user: model_user):
    users.append(data_user)
    return "Datos guardados correctamente"

# Post route
@user.post("/user{id}")
def get_user(id: int):
    for user in users:
        if user.id == id:
            return user
    return "Datos guardados correctamente"

# Put route
@user.put("/user/{id}")
def update_user(id: int, usuarios: model_user):
   for index,user in enumerate(users):
       if user.id == id:
           usuarios.id = id
           users[index]
           return "Datos actualizados correctamente"

# Delete route
@user.delete("/user/{id}")
def delete_user(id: int, usuarios: model_user):
   for index,user in enumerate(users):
       if user.id == id:
           usuarios.id = id
           del users[index]
           return "Datos eliminados correctamente"