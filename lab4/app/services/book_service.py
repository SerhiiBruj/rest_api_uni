from app.repository.book_repository import BookRepository


class BookService:

    def __init__(self):
        self.repository = BookRepository()

    async def get_books(
        self,
        limit: int,
        offset: int
    ):

        return await self.repository.get_books(
            limit,
            offset
        )

    async def get_book(
        self,
        book_id: str
    ):

        return await self.repository.get_book_by_id(
            book_id
        )

    async def create_book(
        self,
        book_data
    ):

        return await self.repository.create_book(
            book_data
        )

    async def delete_book(
        self,
        book_id: str
    ):

        return await self.repository.delete_book(
            book_id
        )