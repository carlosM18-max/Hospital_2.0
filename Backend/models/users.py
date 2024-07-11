from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    Persona_ID = Column(Integer, ForeignKey("persons.id"))
    Nombre_Usuario = Column(String(255))
    Correo_Electronico = Column(String(255))
    Contrasena = Column(String(255))
    Numero_Telefonico = Column(String(255))
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    #items = relationship("Item", back_populates="owner") Clave Foranea
    
    # Relación con la tabla Person
    persona = relationship("Person", back_populates="users")

    # Relación inversa con la tabla UserRol
    user_roles = relationship("UserRol", back_populates="user")