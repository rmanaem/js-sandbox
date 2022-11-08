from fastapi import FastAPI
from typing import Optional
from models import Directions

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'},
}

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

@app.get("/skip_book")
async def skip_book(book_id: Optional[str]):
    if book_id:
        new_books = BOOKS.copy()
        del new_books[book_id]
        return new_books