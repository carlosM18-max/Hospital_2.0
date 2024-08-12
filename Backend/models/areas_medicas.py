from sqlalchemy import Column, Integer, String, Text, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
import enum
from datetime import datetime

Base = declarative_base()

class EstatusEnum(str, enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"

class AreaMedica(Base):
    __tablename__ = "tbc_areas_medicas"

    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Nombre = Column(String(150), nullable=False)
    Descripcion = Column(Text)
    Estatus = Column(Enum(EstatusEnum), default=EstatusEnum.Activo)
    Fecha_Registro = Column(DateTime, nullable=False, default=datetime.utcnow)
    Fecha_Actualizacion = Column(DateTime, default=None)

    def __repr__(self):
        return f"<AreaMedica(ID={self.ID}, Nombre='{self.Nombre}', Estatus='{self.Estatus}')>"