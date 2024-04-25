import uuid

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas import (
    Movie,
    CreateMovieRequest,
    CreateMovieResponse,
    UpdateMovieRequest,
    UpdateMovieResponse,
    DeleteMovieResponse,
)


movies: list[Movie] = [
    Movie(movie_id=uuid.uuid4(), name="Spider-Man", year=2002),
    Movie(movie_id=uuid.uuid4(), name="Thor: Ragnarok", year=2017),
    Movie(movie_id=uuid.uuid4(), name="Iron Man", year=2008),
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/movies")
async def get_movies() -> list[Movie]:
    return movies


@app.post("/movies")
async def create_movie(new_movie: CreateMovieRequest) -> CreateMovieResponse:
    new_uuid = uuid.uuid4()
    movies.append(Movie(movie_id=new_uuid, name=new_movie.name, year=new_movie.year))
    return CreateMovieResponse(id=new_uuid)


@app.put("/movies/{movie_id}")
async def update_movie(
    movie_id: uuid.UUID, updated_movie: UpdateMovieRequest
) -> UpdateMovieResponse:
    for movie in movies:
        if movie_id == movie.movie_id:
            movie.name = updated_movie.name
            movie.year = updated_movie.year

    return UpdateMovieResponse(success=True)


@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: uuid.UUID) -> DeleteMovieResponse:
    for movie in movies:
        if movie_id == movie.movie_id:
            movies.remove(movie)

    return DeleteMovieResponse(success=True)
