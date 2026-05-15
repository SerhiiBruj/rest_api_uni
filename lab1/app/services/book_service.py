from uuid import uuid4

from app.repository.book_repository import BookRepository


class BookService:

    def __init__(self):
        self.repository = BookRepository()

    async def get_books(
        self,
        status=None,
        author=None,
        sort_by=None
    ):
        books = await self.repository.get_all_books()

        if status:
            books = [
                book for book in books
                if book["status"] == status
            ]

        if author:
            books = [
                book for book in books
                if author.lower() in book["author"].lower()
            ]

        if sort_by == "title":
            books.sort(key=lambda x: x["title"])

        elif sort_by == "release_year":
            books.sort(key=lambda x: x["release_year"])

        return books

    async def get_book(self, book_id):
        return await self.repository.get_book_by_id(book_id)

    async def create_book(self, book_data):
        new_book = {
            "id": uuid4(),
            **book_data.model_dump()
        }

        return await self.repository.add_book(new_book)

    async def delete_book(self, book_id):
        return await self.repository.delete_book(book_id)