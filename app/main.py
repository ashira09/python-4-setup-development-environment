from init_db import categoryCRUD, bookCRUD, SessionLocal
from sqlalchemy import text
from fastapi import FastAPI, HTTPException
from api.books import books_router
from api.categories import categories_router

print('Hello, World!')

with SessionLocal() as session:
    books = bookCRUD.read_all_books(session)
    categories = categoryCRUD.read_all_categories(session)
    fiction_books = bookCRUD.read_all_books_by_category(1, session) # из таблицы Book
    fantasy_books = bookCRUD.read_all_books_by_category(2, session) # из таблицы Book
    # fiction_books = categoryCRUD.read_all_books_by_category(1, session) # из таблицы Category
    # fantasy_books = categoryCRUD.read_all_books_by_category(2, session) # из таблицы Category
    print('Добавленные книги: ', ', '.join(['"' + book.title + '"' for book in books]))
    print('Добавленные категории: ', ', '.join(['"' + category.title + '"' for category in categories]))
    print('Книги категории "Фантастика": ', ', '.join(['"' + fiction_book.title + '"' for fiction_book in fiction_books]))
    print('Книги категории "Фэнтези": ', ', '.join(['"' + fantasy_book.title + '"' for fantasy_book in fantasy_books]))

app = FastAPI()

@app.get("/health")
async def check_health():
    try:
        with SessionLocal() as session:
            session.execute(text("SELECT 1"))
    except Exception:
        raise HTTPException(status_code=500, detail='Сервер не работоспособен')
    finally:
        raise HTTPException(status_code=200, detail='Сервер работоспособен')

app.include_router(books_router, prefix="/api")
app.include_router(categories_router, prefix="/api")