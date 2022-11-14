import sys
sys.path.append("..")

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from models import Todos, Todo, Base
from database import engine, SessionLocal
from .auth import get_current_user, get_user_exception


router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not found"}}
)

Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/")
async def read_all(db: Session = Depends(get_db)):
    return db.query(Todos).all()


@router.get("/{todo_id}")
async def read_todo(todo_id: int, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()

    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("id")).first()
    if todo_model:
        return todo_model

    raise todo_not_found_exception(todo_id)


@router.get("/user")
async def read_all_by_user(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user:
        return db.query(Todos).filter(Todos.owner_id == user.get("id")).all()

    raise get_user_exception()


@router.post("/")
async def create_todo(todo: Todo, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    
    todo_model = Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    todo_model.owner_id = user.get("id")

    db.add(todo_model)
    db.commit()

    return successful_response(201)

@router.put("/{todo_id}")
async def update_todo(todo_id: int, todo: Todo, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    
    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("id")).first()
    if todo_model:
        todo_model.title = todo.title
        todo_model.description = todo.description
        todo_model.priority = todo.priority
        todo_model.complete = todo.complete

        db.add(todo_model)
        db.commit()

        return successful_response(204)
    
    raise todo_not_found_exception(todo_id)
    
    
@router.delete("/{todo_id}")
async def delete_todo(todo_id: int, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception() 

    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("id")).first()
    if todo_model:
        db.query(Todos).filter(Todos.id == todo_id).delete()
        db.commit()

        return successful_response(204)

    raise todo_not_found_exception(todo_id)


# Exceptions
def todo_not_found_exception(todo_id: int):
    return HTTPException(status_code=404, detail=f"Todo with id:{todo_id} was not found.")

def successful_response(status_code: int):
    return {
        "status": status_code,
        "transaction": "Successful"
    }