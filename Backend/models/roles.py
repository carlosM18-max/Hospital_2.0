from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(255))
    Descripcion = Column(String(255))
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    #items = relationship("Item", back_populates="owner")
    
    # Relación con la tabla UserRol
    user_roles = relationship("UserRol", back_populates="rol")