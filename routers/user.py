from fastapi import APIRouter, Depends, HTTPException, status
from routers.schemas import ShowUser, User
from sqlalchemy.orm import Session
from routers.database import get_db
from repository import user


Router = APIRouter(prefix="/user", tags=["Users"])


@Router.post("/", response_model=ShowUser)
def creat_user(request: User, db: Session = Depends(get_db)):
    return user.creat(request, db)


@Router.get("/{id}", response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_id(id, db)
