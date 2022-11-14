from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt

from models import Users, User
from database import SessionLocal, engine, Base

SECRET_KEY = "hsafowhshfaownfoasfnouwtbg"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

Base.metadata.create_all(bind=engine)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")


app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_password_hash(password):
    return bcrypt_context.hash(password)


def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()

    if user and bcrypt_context.verify(password, user.hash_password):
        return user

    return False


def create_access_token(username: str, user_id: int, expire_delta: Optional[timedelta] = None):
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    payload = {
        "sub" : username,
        "id" : user_id,
        "exp" : expire
        }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


@app.post("/create/user")
async def create_user(new_user: User, db: Session = Depends(get_db)):
    user_model = Users()
    user_model.email = new_user.email
    user_model.username = new_user.username
    user_model.first_name = new_user.first_name
    user_model.last_name = new_user.last_name

    user_model.hash_password = get_password_hash(new_user.password)
    user_model.is_active = True

    db.add(user_model)
    db.commit()


@app.post("/token")
async def login_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)

    if user:
        return {"token" : create_access_token(user.username, user.id, expire_delta=timedelta(minutes=20))}

    raise HTTPException(status_code=404, detail="User not found.")
