from pydantic import BaseModel
from typing import Optional


class Book(BaseModel): 
  id: Optional[int]
  title: str
  author: str
  publisher: str
  published_date: str
  page_count: int
  language: str

class BookUpdateModel(BaseModel): 
  title: str
  author: str
  publisher: str
  page_count: int
  language: str


