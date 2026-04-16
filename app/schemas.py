from pydantic import BaseModel
from typing import List

class FilterBookList(BaseModel):
    category_ids: List[int]

class CreateBook(BaseModel):
    title: str
    description: str
    price: float
    url: str
    category_id: int

class UpdateBook(CreateBook):
    book_id: int

class DeleteBook(BaseModel):
    book_id: int

class CreateCategory(BaseModel):
    title: str

class UpdateCategory(CreateCategory):
    category_id: int

class DeleteCategory(BaseModel):
    category_id: int