from pydantic import BaseModel
from datetime import date
from typing import Optional
class Movie(BaseModel):
    mid : str
    title : str
    rating: float
    lang: list
    release_date : str
    duration : int
    genres: list
    cast : list
    dsc : str
    country: str
    is_adult : bool
    poster_url : str
    trailer_url : Optional[str]
    
class MovieUpdate(BaseModel):
    mid : str
    title : str
    rating: float
    lang : list
    duration : int
    genres : list
    dsc : str
    poster_url : str
    trailer_url : str
   
