from fastapi import FastAPI

from models import Base
from database import engine
from routers import auth, todos
from company import companyapis


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(
    companyapis.router, 
    prefix="/companyapis", 
    tags=["companyapis"], 
    responses={418: {"description": "Internal use only"}})