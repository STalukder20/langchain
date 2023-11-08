
from langchain.pydantic_v1 import BaseModel, Field
from imdb import Cinemagoer

from libs.langchain.langchain.tools.base import BaseTool

class CastOfMovieSchema(BaseModel):
    """Schema for the CastOfMovie tool."""

    name: str = Field(
        description=(
            " Name of any movie that has been released for which you would like"
            " to find cast information of."
            " An example would be:\n "
            " Despicable Me\n"
        )
    )

class CastOfMovie(BaseTool):
    """Tool to find cast of a movie given its name."""

    name: str = "CastOfMovie"
    description: str = (
        "Use this tool to retrieve a list of cast members for a movie, given its title."
    )

    def _run(self, movieId: str):
        ia = Cinemagoer()
        res_movie = ia.get_movie(movieId)

        return res_movie['cast']
