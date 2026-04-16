from sqlalchemy.orm import Session
from db.models import Book
from db.models import Category
from sqlalchemy import select

class BookCRUD:
    def create_book(self, title: str, description: str, price: float, url: str, category_id: int, session: Session):
        book = Book(
            title = title,
            description = description,
            price = price,
            url = url,
            category_id = category_id
        )
        session.add(book)
        return book

    def read_book(self, id: int, session: Session):
        books = select(Book).where(Book.id == id)
        book = session.scalars(books).first()
        if book is not None:
            return book
        else:
            raise Exception("Книга не найдена!")
    
    def update_book(self, id: int, title: str, description: str, price: float, url: str, category_id: int, session: Session):
        book = self.read_book(id, session)
        book.title = title
        book.description = description
        book.price = price
        book.url = url
        book.category_id = category_id
        session.add(book)
        return book

    def delete_book(self, id: int, session: Session):
        book = self.read_book(id, session)
        session.delete(book)

    def read_all_books(self, session: Session):
        books = select(Book)
        books = session.scalars(books).fetchall()
        return books
    
    def read_all_books_by_category(self, category_id: int, session: Session):
        books = select(Book).where(Book.category_id == category_id)
        books = session.scalars(books).fetchall()
        return books

class CategoryCRUD:
    def create_category(self, title: str, session: Session):
        category = Category(
            title = title
        )
        session.add(category)
        return category

    def read_category(self, id: int, session: Session):
        categories = select(Category).where(Category.id == id)
        category = session.scalars(categories).first()
        if category is not None:
            return category
        else:
            raise Exception("Категория не найдена!")
    
    def update_category(self, id: int, title: str, session: Session):
        category = self.read_category(id, session)
        category.title = title
        session.add(category)
        return category

    def delete_category(self, id: int, session: Session):
        category = self.read_category(id, session)
        session.delete(category)

    def read_all_categories(self, session: Session):
        categories = select(Category)
        categories = session.scalars(categories).fetchall()
        return categories
    
    def read_all_books_by_category(self, category_id: int, session):
        category = self.read_category(category_id, session)
        return category.books