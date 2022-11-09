from enum import Enum
from pydantic import BaseModel
from uuid import UUID

class Directions(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"

class Book(BaseModel):
    id : UUID
    title : str
    author : str
    description : str
    rating : int