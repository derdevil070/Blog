from fastapi import FastAPI
import routers.models as models
from routers.database import engine
from routers import authentication, blog, user


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.Router)
app.include_router(blog.Router)
app.include_router(user.Router)
