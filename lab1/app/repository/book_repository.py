from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.books_data import Book


class BookRepository:

    async def get_books(
        self,
        db: AsyncSession,
        limit: int,
        offset: int
    ):

        query = (
            select(Book)
            .limit(limit)
            .offset(offset)
        )

        result = await db.execute(query)

        return result.scalars().all()

    async def get_book_by_id(
        self,
        db: AsyncSession,
        book_id
    ):

        query = select(Book).where(Book.id == book_id)

        result = await db.execute(query)

        return result.scalar_one_or_none()

    async def create_book(
        self,
        db: AsyncSession,
        book_data
    ):

        book = Book(**book_data.model_dump())

        db.add(book)

        await db.commit()

        await db.refresh(book)

        return book

    async def delete_book(
        self,
        db: AsyncSession,
        book_id
    ):

        book = await self.get_book_by_id(db, book_id)

        if not book:
            return False

        await db.delete(book)

        await db.commit()

        return True