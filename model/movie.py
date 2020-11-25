from typing import Optional
from pydantic import BaseModel


class Movie(BaseModel):
    name: str
    imdb_score: str
    director: str
    popularity: str
    genre : list
    id: Optional[int] = 0

class RemoveMovie(BaseModel):
    id: int