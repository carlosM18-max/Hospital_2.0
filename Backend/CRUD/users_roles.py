import models.roles
import models.users_roles
import schemas.users_roles
from sqlalchemy.orm import Session
import models, schemas

def get_user_rol(db: Session, id: int):
    return db.query(models.users_roles.UserRol).filter(models.users_roles.UserRol.id == id).first()

def get_user_by_rol(db: Session, person: str):
    return db.query(models.users_roles.UserRol).filter(models.users_roles.UserRol.usuario_ID == person).first()

def get_users_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.users_roles.UserRol).offset(skip).limit(limit).all()

def create_user_rol(db: Session, user_rol: schemas.users_roles.UserRolCreate):
    db_user_rol = models.users_roles.UserRol(usuario_ID=user_rol.usuario_ID, rol_ID=user_rol.rol_ID, Fecha_Registro=user_rol.Fecha_Registro, Fecha_Actualizacion=user_rol.Fecha_Actualizacion)
    db.add(db_user_rol)
    db.commit()
    db.refresh(db_user_rol)
    return db_user_rol

def update_user_rol(db: Session, id: int, user_rol: schemas.users_roles.UserRolUpdate):
    db_user_rol = db.query(models.users_roles.UserRol).filter(models.users_roles.UserRol.id == id).first()
    if db_user_rol:
        for var, value in vars(user_rol).items():
            setattr(db_user_rol, var, value) if value else None
        db.commit()
        db.refresh(db_user_rol)
    return db_user_rol

def delete_user_rol(db: Session, id: int):
    db_user_rol = db.query(models.users_roles.UserRol).filter(models.users_roles.UserRol.id == id).first()
    if db_user_rol:
        db.delete(db_user_rol)
        db.commit()
    return db_user_rol