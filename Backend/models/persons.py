from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class user (Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(255))
    password = Column(LONGTEXT)
    created_at = Column(DateTime)
    estatus = Column(Boolean, default=False)
    persona_ID = Column(Integer)
    # Items = relationship("Item", back_populates="owner") # Llave foranea