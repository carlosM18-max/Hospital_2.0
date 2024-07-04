from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    usuario: str
    password: str
    created_at: datetime
    estatus: bool
    persona_ID: int
    
class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int
    # owner_ID: int
    class Config:
        orm_mode = True
        
