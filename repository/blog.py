from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session
import routers.models as models
from routers.schemas import ShowBlog, Blog, BlogUpdate


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: Blog, db: Session):
    new_blog = models.Blog(
        title=request.title, body=request.body, user_id=request.user_id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(db: Session, id: int):
    blog = (
        db.query(models.Blog)
        .filter(models.Blog.id == id)
        .delete(synchronize_session=False)
    )
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
    db.commit()
    return "Done"


def update(id: int, request: BlogUpdate, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    for key, value in request.model_dump().items():
        setattr(blog, key, value)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
    db.commit()
    return "update"


def get(id: int, db: Session, response: Response):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Blog with the id {id} is not avalilable"}
    return blog
