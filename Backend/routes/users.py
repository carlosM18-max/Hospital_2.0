from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
import crud.users, config.db, schemas.users, models.users
from typing import List

user = APIRouter()

models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user.get("/users/", response_model=List[schemas.users.User], tags=["Usuarios"])
def read_user(skip: int = 0, limit: int = 0, db: Session = Depends(get_db)):
    db_users = crud.users.get_users(db = db, skip = skip, limit = limit)
    return db_users

@user.post("/users/{id}", response_model=schemas.users.User, tags=["Usuarios"])
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.users.get_user(db = db, id = id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user.post("/users/", response_model=schemas.users.User, tags=["Usuarios"])
def create_user(user: schemas.users.UserCreate, db: Session = Depends(get_db)):
    db_users = crud.users.get_user_by_usuario(db, usuario=user.usuario)
    if db_users:
        raise HTTPException(status_code=404, detail="Usuario existente, intenta nuevamente mas tarde...")
    return crud.users.create_user(db = db, user = user)

@user.put("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"])
def update_user(id: int, user: schemas.users.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.users.update_user(db = db, id = id, user = user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no existente, no esta actuaizado")
    return db_user

@user.delete("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"])
def delete_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.users.delete_user(db = db, id = id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Uusario no existe, no s epudo eliminar")
    return db_user