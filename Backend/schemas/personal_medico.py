from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from models.personal_medico import EnumTipoPersonal, EnumEstatus

class PersonalMedicoBase(BaseModel):
    Persona_ID: int
    Departamento_ID: Optional[int] = None
    Cedula_Profesional: str
    Tipo: EnumTipoPersonal
    Especialidad: Optional[str] = None
    Fecha_Registro: datetime
    Fecha_Contratacion: datetime
    Fecha_Termino_Contrato: Optional[datetime] = None
    Salario: Decimal
    Estatus: EnumEstatus
    Fecha_Actualizacion: Optional[datetime] = None
    
class PersonalMedicoCreate(PersonalMedicoBase):
    pass

class PersonalMedicoUpdate(PersonalMedicoBase):
    pass

class PersonalMedico(PersonalMedicoBase):
    Persona_ID: int

    class Config:
        from_attributes = True
