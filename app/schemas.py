from pydantic import BaseModel
from typing import List

class GetBookList(BaseModel):
    category_id: int

class CreateBook(BaseModel):
    title: str
    description: str
    price: float
    url: str
    category_id: int

class UpdateBook(CreateBook):
    book_id: int

class DeleteBook(BaseModel):


