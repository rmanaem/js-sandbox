from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
from database import engine, SessionLocal
from utils import not_found


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


@app.get("/todo/{todo_id}")
async def read_todo(todo_id: int, db:Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if todo_model:
        return todo_model
    raise not_found(todo_id)