from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    persona_ID: int
    nombre_usuario: str
    correo_electronico: str
    contrasena: str
    numero_telefonico: str
    estatus: bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime


class UserCreate(UserBase):
    usuario: str

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True
        
# class UserLogin(BaseModel):
#     usuario: str
#     password: str

