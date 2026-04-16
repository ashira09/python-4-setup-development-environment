from init_db import categoryCRUD, bookCRUD, engine
from sqlalchemy.orm import Session
from pprint import pp

print('Hello, World!')

with Session(engine) as session:
    books = bookCRUD.read_all_books(session)
    categories = categoryCRUD.read_all_categories(session)
    fiction_books = bookCRUD.read_all_books_by_category(1, session) # из таблицы Book
    fantasy_books = bookCRUD.read_all_books_by_category(2, session) # из таблицы Category
    # fiction_books = categoryCRUD.read_all_books_by_category(1, session) # из таблицы Category
    # fantasy_books = categoryCRUD.read_all_books_by_category(2, session) # из таблицы Category
    print('Добавленные книги: ', ', '.join(['"' + book.title + '"' for book in books]))
    print('Добавленные категории: ', ', '.join(['"' + category.title + '"' for category in categories]))
    print('Книги категории "Фантастика": ', ', '.join(['"' + fiction_book.title + '"' for fiction_book in fiction_books]))
    print('Книги категории "Фэнтези": ', ', '.join(['"' + fantasy_book.title + '"' for fantasy_book in fantasy_books]))