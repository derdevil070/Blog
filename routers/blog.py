from fastapi import APIRouter, Depends, status, Response
from routers.schemas import ShowBlog, Blog, BlogUpdate
from typing import List
from sqlalchemy.orm import Session
from routers.database import get_db
from repository import blog

Router = APIRouter(prefix="/blog", tags=["Blogs"])


@Router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)


@Router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destory(id: int, db: Session = Depends(get_db)):
    return blog.delete(id, db)


@Router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: BlogUpdate, db: Session = Depends(get_db)):
    return blog.update(id, request, db)


@Router.get("/", response_model=List[ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)


@Router.get("/{id}", status_code=200, response_model=ShowBlog)
def show(id: int, response: Response, db: Session = Depends(get_db)):
    return blog.get(id, db, response)
