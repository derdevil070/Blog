from pydantic import BaseModel
from typing import Optional
from typing import List


class Blog(BaseModel):
    title: str
    body: str
    user_id: int

    class Config:
        orm_mode = True


class BlogUpdate(Blog):
    title: Optional[str] = None
    body: Optional[str] = None


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: Optional[List[Blog]] = None

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    creator: Optional[ShowUser] = None

    class Config:
        orm_mode = True


class Loging(BaseModel):
    username: str
    password: str


class TokenData(BaseModel):
    username: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str
