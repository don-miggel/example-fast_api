from sqlalchemy.orm import Session
import app.models as models
from app.schemas import UserOut, UserCreate
from fastapi import status, Depends, APIRouter, HTTPException, Response
from app.database import get_db
from typing import List
from app.utils import hash_passw


router = APIRouter(
    prefix="/users",
    tags=['User']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    hashed_passw = hash_passw(user.password)
    new_user.password = hashed_passw
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/{id}", response_model=UserOut)
def get_usr_by_id(id: int,db: Session = Depends(get_db) ):

    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Post with {id} ID was not found !")
    return user

@router.get("/", response_model=List[UserOut])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    print(users)
    return users

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def del_user(id: int, db: Session = Depends(get_db)):

    deleted_user =  db.query(models.User).filter(models.User.id == id)

    if not deleted_user.first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Post with {id} ID was not found !")

    deleted_user.delete(synchronize_session= False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
