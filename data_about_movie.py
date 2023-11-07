from typing import Optional, Type

from langchain.pydantic_v1 import BaseModel, Field

from libs.langchain.langchain.tools.base import BaseTool

class DataAboutMovie(BaseTool)
    name: str = "DataAboutMovie"
    description: str = (
        "Use this tool to find general information about a movie."
    )

    # def _run(self, movie):

