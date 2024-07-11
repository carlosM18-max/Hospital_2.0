from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.users_roles, config.db, schemas.users_roles, models.users_roles
from typing import List

users_roles = APIRouter()

models.persons.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@users_roles.get("/users_roles/", response_model=List[schemas.users_roles.UserRol], tags=["Usuario_Roles"])
def read_user_rol(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_user_rol= crud.users_roles.get_users_roles(db=db, skip=skip, limit=limit)
    return db_user_rol

@users_roles.post("/users_roles/{id}", response_model=schemas.users_roles.UserRol, tags=["Usuario_Roles"])
def read_user_rol(id: int, db: Session = Depends(get_db)):
    db_user_rol= crud.users_roles.get_user_rol(db=db, id=id)
    if db_user_rol is None:
        raise HTTPException(status_code=404, detail="Usuario con rol no encontrado")
    return db_user_rol

@users_roles.post("/users_roles/", response_model=schemas.users_roles.UserRol, tags=["Usuario_Roles"])
def create_user_rol(users_roles: schemas.users_roles.UserRolCreate, db: Session = Depends(get_db)):
    db_user_rol = crud.users_roles.get_user_by_rol(db, users_roles=users_roles.usuario_ID)
    if db_user_rol:
        raise HTTPException(status_code=400, detail="Usuario con rol existente intenta nuevamente")
    return crud.users_roles.create_user_rol(db=db,  users_roles=users_roles)

@users_roles.put("/users_roles/{id}", response_model=schemas.users_roles.UserRol, tags=["Usuario_Roles"])
def update_user_rol(id: int,  users_role: schemas.users_roles.UserRolUpdate, db: Session = Depends(get_db)):
    db_user_rol = crud.users_roles.update_user_rol(db=db, id=id, users_role=users_role)
    if db_user_rol is None:
        raise HTTPException(status_code=404, detail="Usuario con rol no existente, no actualizado")
    return db_user_rol

@users_roles.delete("/users_roles/{id}", response_model=schemas.users_roles.UserRol, tags=["Usuario_Roles"])
def delete_user_rol(id: int, db: Session = Depends(get_db)):
    db_user_rol = crud.users_roles.delete_user_rol(db=db, id=id)
    if db_user_rol is None:
        raise HTTPException(status_code=404, detail="Usuario con rol no existente, no se pudo eliminar")
    return db_user_rol