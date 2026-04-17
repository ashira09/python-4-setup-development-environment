from fastapi import APIRouter, HTTPException, Query, Depends
from typing import Annotated

from sqlalchemy.exc import IntegrityError
from db.crud import UndefinedObjectException
from main import bookCRUD
from sqlalchemy.orm import Session
from schemas import BookResponse, CreateBook, UpdateBook
from init_db import get_session

books_router = APIRouter()

@books_router.get("/books")
async def get_book_list(category_ids: Annotated[list[int] | None, Query()] = None, session: Session = Depends(get_session)) -> Annotated[list[BookResponse] | None, Query()]:
    all_pydantic_books = list()
    if category_ids is None:
        all_orm_books = bookCRUD.read_all_books(session=session)
        for book in all_orm_books:
            all_pydantic_books.append(BookResponse.model_validate(book))
    else:
        for category_id in category_ids:
            all_orm_books = bookCRUD.read_all_books_by_category(category_id=category_id, session=session)
            for book in all_orm_books:
                all_pydantic_books.append(BookResponse.model_validate(book))
    return all_pydantic_books

@books_router.get("/books/{id}")
async def get_book(id: int, session: Session = Depends(get_session)) -> BookResponse:
    try:
        category = bookCRUD.read_book(id=id, session=session)
    except UndefinedObjectException as e:
        raise HTTPException(status_code=404, detail=e.message)
    return BookResponse.model_validate(category)

@books_router.post("/books/create-book", status_code=201)
async def create_book(create_book_params: CreateBook, session: Session = Depends(get_session)):
    try:
        book = bookCRUD.create_book(
            title=create_book_params.title, 
            description=create_book_params.description,
            price=create_book_params.price,
            url=create_book_params.url,
            category_id=create_book_params.category_id,
            session=session
        )
        session.commit()
    except IntegrityError as e:
        raise HTTPException(status_code=422, detail='ID категории не существует')
    return BookResponse.model_validate(book)

@books_router.delete("/books/delete-book/{id}", status_code=201)
async def delete_book(id: int, session: Session = Depends(get_session)):
    try:
        book = bookCRUD.delete_book(
            id=id,
            session=session
        )
        session.commit()
    except UndefinedObjectException as e:
        raise HTTPException(status_code=404, detail=e.message)
    return BookResponse.model_validate(book)

@books_router.put("/books/update-book/{id}", status_code=201)
async def update_book(id: int, update_book_params: UpdateBook, session: Session = Depends(get_session)):
    try:
        book = bookCRUD.update_book(
            id=id,
            title=update_book_params.title,
            description=update_book_params.description,
            price=update_book_params.price,
            url=update_book_params.url,
            category_id=update_book_params.category_id,
            session=session
        )
        session.commit()
    except UndefinedObjectException as e:
        raise HTTPException(status_code=404, detail=e.message)
    except IntegrityError as e:
        raise HTTPException(status_code=422, detail='ID категории не существует')
    return BookResponse.model_validate(book)
