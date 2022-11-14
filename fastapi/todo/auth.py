from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from models import Users, User
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


app = FastAPI()


def get_password_hash(password):
    return bcrypt_context.hash(password)


@app.post("/create/user")
async def create_user(new_user: User):
    user_model = Users()
    user_model.email = new_user.email
    user_model.username = new_user.username
    user_model.first_name = new_user.first_name
    user_model.last_name = new_user.last_name

    user_model.hash_password = get_password_hash(new_user.password)
    user_model.is_active = True

    return user_model

