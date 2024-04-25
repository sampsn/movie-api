from uuid import UUID

from pydantic import BaseModel


class BaseMovie(BaseModel):
    name: str
    year: int


class CreateMovieRequest(BaseMovie):
    pass


class UpdateMovieRequest(BaseMovie):
    pass


class Movie(BaseMovie):
    movie_id: UUID


class CreateMovieResponse(BaseModel):
    id: UUID


class UpdateMovieResponse(BaseModel):
    success: bool


class DeleteMovieResponse(BaseModel):
    success: bool
