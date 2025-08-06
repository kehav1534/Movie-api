from pydantic import BaseModel
from datetime import date
from typing import Optional
class Movie(BaseModel):
    mid : str
    title : str
    rating: float
    release_date : str
    lang: list
    duration : int
    genres: list
    cast : list
    dsc : str
    country: str
    is_adult : bool
    poster_url : str
    trailer_url : Optional[str]
    
class MovieOptional(BaseModel):
    title : Optional[str]
    rating: Optional[float]
    duration : Optional[int]
    poster_url : Optional[str]
    trailer_url : Optional[str]
   
class User(BaseModel):
    name : Optional[str]
    email : str
    pwd : str

class HistoryData(BaseModel):
    mid : str
    wd : float   # watched duration
    
class UserHistory(BaseModel):
    email : str
    data : list[HistoryData]