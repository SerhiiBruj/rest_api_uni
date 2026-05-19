from app.repository.book_repo import BookRepository

class BookService:
    def __init__(self):
        self.repo = BookRepository()

    async def list_books(self, skip, limit):
        return await self.repo.get_all(skip, limit)

    async def get_book(self, book_id):
        return await self.repo.get_by_id(book_id)

    async def create_book(self, book):
        data = book.model_dump()  
        return await self.repo.create(data)

    async def delete_book(self, book_id):
        return await self.repo.delete(book_id)