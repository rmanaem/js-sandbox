from fastapi import FastAPI
from typing import Optional
from models import Directions, Book

app = FastAPI()

BOOKS = []

@app.get("/")
async def get_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def get_book(book_id: str):
    return BOOKS[book_id]

@app.get("directions/{name}")
async def get_direction(name: Directions):
    if name == Directions.north:
        return {"Direction": name, "sub": 'Up'}
    if name == Directions.south:
        return {"Direction": name, "sub": 'Down'}
    if name == Directions.east:
        return {"Direction": name, "sub": 'Right'}
    if name == Directions.west:
        return {"Direction": name, "sub": 'Left'}

@app.get("/skip_book/")
async def skip_book(book_id: Optional[str]):
    if book_id:
        new_books = BOOKS.copy()
        del new_books[book_id]
        return new_books
    return BOOKS

@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book

@app.put("/{book_id}")
async def update_book(book_id: str, book_title: str, book_author: str):
    BOOKS[book_id] = {'title': book_title, 'author': book_author}
    return BOOKS[book_id]

@app.delete('/{book_id}')
async def delete_book(book_id):
    del BOOKS[book_id]
    return f'{book_id} has been deleted.'