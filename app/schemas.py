from pydantic import BaseModel, ConfigDict

class Book(BaseModel):
    title: str
    description: str
    price: float
    url: str
    category_id: int

class CreateBook(Book):
    pass

class UpdateBook(Book):
    pass

class BookResponse(Book):
    id: int | None
    model_config = ConfigDict(from_attributes=True)

class Category(BaseModel):
    title: str

class CreateCategory(Category):
    pass

class UpdateCategory(Category):
    pass

class CategoryResponse(Category):
    id: int | None
    model_config = ConfigDict(from_attributes=True)