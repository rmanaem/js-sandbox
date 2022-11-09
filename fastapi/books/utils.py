from uuid import UUID
from fastapi import HTTPException

def not_found(book_id: UUID):
    return HTTPException(status_code=404, detail=f'Book with id:{book_id} was not found')