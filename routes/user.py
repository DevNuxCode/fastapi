from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import User as UserModel  # Modelo SQLAlchemy
from schemas.user import User as UserSchema  # Esquema Pydantic
from database import SessionLocal
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

# Ruta para obtener todos los usuarios (GET)
@router.get("/users/", response_model=List[UserSchema])  # <-- Usa List[UserSchema] para devolver una lista
def read_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()  # Obtiene todos los usuarios de la base de datos
    return users

@router.get("/users/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=UserSchema)
def update_user(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted"}