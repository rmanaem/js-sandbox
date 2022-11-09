from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class Book(BaseModel):
    id : UUID
    title : str = Field(min_length=1)
    author : str = Field(min_length=1, max_length=100)
    description : Optional[str] = Field(title="Description of the book", min_length=1, max_length=100)
    rating : int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            "example" : {
                "id" : "b365f3ec-82cb-440b-b77c-e4fe7dfffc25",
                "title": "Computer Science Pro",
                "author": "Codingwithroby",
                "description": "A very nice description of a book",
                "rating": 75
            }
        }


class BookNoRating(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str
    description: Optional[str] = Field(None, title="Description of the book", min_length=1, max_length=100)
    

class Directions(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"