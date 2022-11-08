from fastapi import FastAPI

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'},
}

@app.get("/")
async def read_books():
    return BOOKS

@app.get("/books/{book_id}")
async def get_book(book_id: str):
    return BOOKS[book_id]
     