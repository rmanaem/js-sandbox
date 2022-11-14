import sys
sys.path.append("..")

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import engine, SessionLocal, Base
from models import Users, UserVerification
from .auth import get_current_user, get_user_exception, get_password_hash, get_db, bcrypt_context
from .todos import successful_response


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
async def user_by_path(user_id: int, db: Session = Depends(get_db)):
    user_model = db.query(Users).filter(Users.id == user_id).first()
    if user_model:
        return user_model

    return f"User id:{user_id} is invalid"


@router.get("/user/")
async def user_by_query(user_id: int, db: Session = Depends(get_db)):
    user_model = db.query(Users).filter(Users.id == user_id).first()
    if user_model:
        return user_model

    return f"User id:{user_id} is invalid"


@router.put("/user/password")
async def user_password_change(user_verification: UserVerification, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user:
        user_model = db.query(Users).filter(Users.id == user.get("id")).first()
        if user_model:
            if user_verification.username == user_model.username and bcrypt_context.verify(user_verification.password, user_model.hash_password):
                user_model.hash_password = get_password_hash(user_verification.new_password)

                db.add(user_model)
                db.commit()

                return successful_response(204)

        else:
            return "Invalid user or request"
    
    raise get_user_exception()
    