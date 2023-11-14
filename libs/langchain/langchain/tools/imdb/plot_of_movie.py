
from langchain.pydantic_v1 import BaseModel, Field
from imdb import Cinemagoer

from langchain.tools.base import BaseTool

class PlotOfMovieSchema(BaseModel):
    """Schema for the PlotOfMovie tool."""

    name: str = Field(
        description=(
            " Name of any movie that has been released for which you would like"
            " to find the plot of."
            " An example of an input would be:\n "
            " Despicable Me\n"
        )
    )

class PlotOfMovie(BaseTool):
    """Tool to find plot of a movie given its name."""

    name: str = "PlotOfMovie"
    description: str = (
        "Use this tool to retrieve a summary of the plot of a movie, given its IMDB movie ID."
    )

    def _run(self, movieId: str):
        ia = Cinemagoer()
        res_movie = ia.get_movie(movieId)

        return res_movie['plot']
