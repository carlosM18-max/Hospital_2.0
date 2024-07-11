import models.users
import schemas.users
from sqlalchemy.orm import Session
import models, schemas

def get_user(db: Session, id: int):
    return db.query(models.users.User).filter(models.users.User.id == id).first()

def get_user_by_usuario(db: Session, usuario: str):
    return db.query(models.users.User).filter(models.users.User.usuario == usuario).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.users.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.users.UserCreate):
    db_user = models.users.User(persona_ID=user.persona_ID, name_user=user.nombre_usuario, email_elect = user.correo_electronico, password = user.contrasena, number_phone = user.numero_telefonico, status = user.estatus, Fecha_Registro=user.Fecha_Registro, Fecha_Actualizacion=user.Fecha_Actualizacion )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, id: int, user: schemas.users.UserUpdate):
    db_user = db.query(models.users.User).filter(models.users.User.id == id).first()
    if db_user:
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, id: int):
    db_user = db.query(models.users.User).filter(models.users.User.id == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user