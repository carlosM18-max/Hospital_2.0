from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class UserRol(Base):
    __tablename__ = "users_roles"

    usuario_ID = Column(Integer, ForeignKey("users.id"), primary_key=True)
    rol_ID = Column(Integer, ForeignKey("roles.id"))
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    #items = relationship("Item", back_populates="owner") Clave Foranea

    # Relación con la tabla User
    user = relationship("User", back_populates="user_roles")

    # Relación con la tabla Roles
    rol = relationship("Roles", back_populates="user_roles")