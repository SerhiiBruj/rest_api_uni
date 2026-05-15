from app.models.books_data import books_db


class BookRepository:

    async def get_all_books(self):
        return books_db

    async def get_book_by_id(self, book_id):
        for book in books_db:
            if book["id"] == book_id:
                return book
        return None

    async def add_book(self, book_data):
        books_db.append(book_data)
        return book_data

    async def delete_book(self, book_id):
        for book in books_db:
            if book["id"] == book_id:
                books_db.remove(book)
                return True
        return False