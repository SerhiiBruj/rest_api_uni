from sqlalchemy.ext.asyncio import AsyncSession

from app.repository.book_repository import BookRepository


class BookService:

    def __init__(self):
        self.repository = BookRepository()

    async def get_books(
        self,
        db: AsyncSession,
        limit: int,
        offset: int
    ):

        return await self.repository.get_books(
            db,
            limit,
            offset
        )

    async def get_book(
        self,
        db: AsyncSession,
        book_id
    ):

        return await self.repository.get_book_by_id(
            db,
            book_id
        )

    async def create_book(
        self,
        db: AsyncSession,
        book_data
    ):

        return await self.repository.create_book(
            db,
            book_data
        )

    async def delete_book(
        self,
        db: AsyncSession,
        book_id
    ):

        return await self.repository.delete_book(
            db,
            book_id
        )