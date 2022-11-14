from fastapi import FastAPI, Depends

from models import Base
from database import engine
from routers import auth, todos, users
from company import companyapis, dependencies


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(
    companyapis.router, 
    prefix="/companyapis", 
    tags=["companyapis"],
    dependencies=[Depends(dependencies.get_token_header)],
    responses={418: {"description": "Internal use only"}})
app.include_router(users.router)