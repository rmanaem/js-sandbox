import sys
sys.path.append("..")

from fastapi import Depends, APIRouter
from models import Users
from database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .auth import get_current_user, get_user_exception, get_password_hash, get_db


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)


Base.metadata.create_all(bind=engine)


@router.get("/")
async def read_all(db: Session = Depends(get_db)):
    return db.query(Users).all()


@router.get("/user/{user_id}")
async def user_by_path(user_id: str, db: Session = Depends(get_db)):
    user_model = db.query(Users).filter(Users.id == user_id).first()
    if user_model:
        return user_model

    return f"User id:{user_id} is invalid"


