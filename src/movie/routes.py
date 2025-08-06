from fastapi import APIRouter, status, Query
from fastapi.exceptions import HTTPException
from src.movie.schemas import *
from datetime import date
from typing import Optional, List
from src.movie.data import movie_data

movie_router = APIRouter()
@movie_router.get('/sh/{movie_id}', status_code=status.HTTP_200_OK)
async def get_movie(movie_id:str=None) -> Movie:
    for movie in movie_data:
        if movie['mid'] == movie_id:
            return movie_id
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found.")
        

@movie_router.get('/sh', status_code=status.HTTP_200_OK)
async def get_movie(q:str=None) -> Movie | List[Movie]:
    if not q:
        return movie_data[:5]        #Here return top trending shows...
    for movie in movie_data:
        if q.lower() in movie['title'].lower():
            return movie
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"'{q}' Not Found.")

@movie_router.get('/sh/of/g', status_code=status.HTTP_200_OK)
async def genre_lang_filter(genre:list = Query(default=[]), lang: list=Query(default=[]))->List[Movie]:
    mov = []
    if genre or lang:
        for movie in movie_data:
            if any(m in movie['lang'] for m in lang) and any(m in movie['genres'] for m in genre) and len(mov) < 20:
                mov.append(movie)
                
        return sorted(mov, key=lambda x: x["rating"])
    
    if not mov:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='No movie found as per your match...')
        

@movie_router.post("/m/add", status_code=status.HTTP_202_ACCEPTED)
async def add_movie(movie_data:Movie)-> bool:
    return True

@movie_router.delete("/m/{movie_id}", status_code=status.HTTP_200_OK) 
async def remove_show(movie_id: str)-> bool:
    return True