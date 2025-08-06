from fastapi import FastAPI
from src.movie.routes import movie_router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Initializing the API server...")
    yield
    print("API server being closed...")

version = "v1"
app = FastAPI(title="Movie API",
              description= "A movie api for general use for all.",
              version= version,
              lifespan=lifespan)

app.include_router(movie_router, prefix=f"/api/{version}/app", tags=["movie"])