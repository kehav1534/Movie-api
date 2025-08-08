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
            return movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found.")
        

@movie_router.get('/sh', status_code=status.HTTP_200_OK)
async def get_movie(q:str=None) -> Movie | List[Movie]:
    if not q:
        return movie_data[:5]        #Here return top trending shows...
    for movie in movie_data:
        if q.lower() in movie['title'].lower():
            return movie
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"'{q}' Not Found.")

@movie_router.get('/filter', status_code=status.HTTP_200_OK)
async def genre_lang_filter(genre:list = Query(default=[]), lang: list=Query(default=[]))->List[Movie]:
    mov = []
    if genre and lang:
        for movie in movie_data:
            if any(m in movie['lang'] for m in lang) and any(m in movie['genres'] for m in genre) and len(mov) < 20:
                mov.append(movie)
    
    elif genre or lang:
        for movie in movie_data:
            if any(m in movie['lang'] for m in lang) or any(m in movie['genres'] for m in genre) and len(mov) < 20:
                mov.append(movie)
    
    else:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='No movie found as per your match...')
    
    return sorted(mov, key=lambda x: x['rating'])
        

@movie_router.post("/sh", status_code=status.HTTP_202_ACCEPTED)
async def add_movie(data:Movie)-> bool:
    movie_data.append(data.model_dump())
    return True

@movie_router.patch("/sh", status_code=status.HTTP_202_ACCEPTED)
async def add_movie(data:MovieUpdate)-> Movie:
    dt = data.model_dump().copy()
    for movie in movie_data:
        if dt['mid'] == movie['mid']:
            for key in dt.keys():
                movie[key]= dt[key]
            return movie
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Show Not found in DataBase.")


@movie_router.delete("/m/{mid}", status_code=status.HTTP_200_OK) 
async def remove_show(mid: str)-> bool:
    for show in movie_data: 
        if mid == show['mid']:
            movie_data.remove(show)
            return True
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Show Not Found.")