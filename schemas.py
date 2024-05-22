from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    title: str
    body: str


class BlogUpdate(Blog):
    title: Optional[str] = None
    body: Optional[str] = None
