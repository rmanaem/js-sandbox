from fastapi import FastAPI
from typing import Optional
from uuid import UUID
from models import Directions, Book

app = FastAPI()

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
async def get_all_books():
    return BOOKS

@app.get("/book/{book_id}")
async def get_book(book_id : UUID):
    for b in BOOKS:
        if b.id == book_id:
            return b
    return f'Book by id:{book_id} was not found.'
        

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
async def update_book(book_id: UUID, book: Book):
    i = 0
    for b in BOOKS:
        if b.id == book_id:
            BOOKS[i] = book
            return BOOKS[i]
        i += 1            
    return f'Book by id:{book_id} was not found'

@app.delete('/{book_id}')
async def delete_book(book_id):
    del BOOKS[book_id]
    return f'{book_id} has been deleted.'