from fastapi import HTTPException

def not_found(todo_id: int):
    return HTTPException(status_code=404, detail=f"Todo with id:{todo_id} was not found.")