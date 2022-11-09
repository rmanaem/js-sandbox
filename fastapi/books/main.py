from fastapi import FastAPI, HTTPException, Request, status, Form, Header
from starlette.responses import JSONResponse
from typing import Optional
from uuid import UUID

from models import Directions, Book, BookNoRating
from utils import not_found

class NegativeNumberException(Exception):
    def __init__(self, books_to_return):
        self.books_to_return = books_to_return


app = FastAPI()


@app.exception_handler(NegativeNumberException)
async def negative_number_exception_handler(request: Request, exception: NegativeNumberException):
    return JSONResponse(
        status_code=418,
        content={"message": f'Negative number of books do not exist.'}
    )


BOOKS = [
    Book(id="71f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 1",
                  author="Author 1",
                  description="Description 1",
                  rating=60),
    Book(id="21f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 2",
                  author="Author 2",
                  description="Description 2",
                  rating=70),
    Book(id="31f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 3",
                  author="Author 3",
                  description="Description 3",
                  rating=80),
    Book(id="41f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 4",
                  author="Author 4",
                  description="Description 4",
                  rating=90)
]


@app.get("/")
async def read_all_books():
    return BOOKS


@app.get("/book/{book_id}")
async def read_book(book_id : UUID):
    for b in BOOKS:
        if b.id == book_id:
            return b

    raise not_found(book_id)


@app.get("/book/rating/{book_id}", response_model=BookNoRating)
async def read_book_no_rating(book_id: UUID):
    for b in BOOKS:
        if b.id == book_id:
            return b

    raise not_found(book_id)


@app.get("/header")
async def read_header(header: Optional[str] = Header(None)):
    return {"header": header}


@app.get("/books/")
async def read_books(books_to_return: Optional[int] = None):
    if books_to_return and books_to_return < 0:
        raise NegativeNumberException(books_to_return)
    
    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 0
        new_books = []
        while i < books_to_return:
            new_books.append(BOOKS[i])
            i += 1
        return new_books

    return BOOKS


@app.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    BOOKS.append(book)
    return book


@app.post("/books/login")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username, "password": password}


@app.put("/{book_id}")
async def update_book(book_id: UUID, book: Book):
    i = 0
    for b in BOOKS:
        if b.id == book_id:
            BOOKS[i] = book
            return BOOKS[i]
        i += 1

    raise not_found(book_id)


@app.delete('/{book_id}')
async def delete_book(book_id: UUID):
    i = 0
    for b in BOOKS:
        if b.id == book_id:
            del BOOKS[i]
            return f'Book with id:{book_id} has been deleted.'
            
    raise not_found(book_id)


@app.get("directions/{name}")
async def read_direction(name: Directions):
    if name == Directions.north:
        return {"Direction": name, "sub": 'Up'}
    if name == Directions.south:
        return {"Direction": name, "sub": 'Down'}
    if name == Directions.east:
        return {"Direction": name, "sub": 'Right'}
    if name == Directions.west:
        return {"Direction": name, "sub": 'Left'}


    