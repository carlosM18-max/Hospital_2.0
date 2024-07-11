from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class UserRolBase(BaseModel):
    usuario_ID: int
    rol_ID: int
    estatus: bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime
    

class UserRolCreate(UserRolBase):
    pass

class UserRolUpdate(UserRolBase):
    pass

class UserRol(UserRolBase):
    id: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True
        
# class UserLogin(BaseModel):
#     usuario: str
#     password: str

