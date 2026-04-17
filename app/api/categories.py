from fastapi import APIRouter, HTTPException, Query, Depends
from typing import Annotated

from sqlalchemy.exc import IntegrityError
from db.crud import UndefinedObjectException
from main import categoryCRUD
from sqlalchemy.orm import Session
from schemas import CategoryResponse, CreateCategory, UpdateCategory
from init_db import get_session

categories_router = APIRouter()

@categories_router.get("/categories")
async def get_category_list(session: Session = Depends(get_session)) -> list[CategoryResponse]:
    all_pydantic_categories = list()
    all_orm_categories = categoryCRUD.read_all_categories(session=session)
    for category in all_orm_categories:
        all_pydantic_categories.append(CategoryResponse.model_validate(category))
    return all_pydantic_categories

@categories_router.get("/categories/{id}")
async def get_category(id: int, session: Session = Depends(get_session)) -> CategoryResponse:
    try:
        category = categoryCRUD.read_category(id=id, session=session)
    except UndefinedObjectException as e:
        raise HTTPException(status_code=404, detail=e.message)
    return CategoryResponse.model_validate(category)

@categories_router.post("/categories/create-category")
async def create_category(create_category_params: CreateCategory, session: Session = Depends(get_session)):
    category = categoryCRUD.create_category(
        title=create_category_params.title,
        session=session
    )
    session.commit()
    return CategoryResponse.model_validate(category)

@categories_router.delete("/categories/delete-category/{id}")
async def delete_category(id: int, session: Session = Depends(get_session)):
    try:
        category = categoryCRUD.delete_category(
            id=id,
            session=session
        )
        session.commit()
    except UndefinedObjectException as e:
        raise HTTPException(status_code=404, detail=e.message)
    except IntegrityError as e:
        raise HTTPException(status_code=409, detail="Категория связана с книгами")
    return CategoryResponse.model_validate(category)

@categories_router.put("/categories/update-category/{id}")
async def update_category(id: int, update_category_params: UpdateCategory, session: Session = Depends(get_session)):
    try:
        category = categoryCRUD.update_category(
            id=id,
            title=update_category_params.title,
            session=session
        )
        session.commit()
    except UndefinedObjectException as e:
        raise HTTPException(status_code=404, detail=e.message)
    return CategoryResponse.model_validate(category)
