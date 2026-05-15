from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.schemas.book import (
    BookCreate,
    BookResponse
)

from app.services.book_service import BookService


router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

service = BookService()


@router.get(
    "/",
    response_model=list[BookResponse]
)
async def get_books(
    limit: int = 10,
    offset: int = 0,
    db: AsyncSession = Depends(get_db)
):

    return await service.get_books(
        db,
        limit,
        offset
    )


@router.get(
    "/{book_id}",
    response_model=BookResponse
)
async def get_book(
    book_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    book = await service.get_book(
        db,
        book_id
    )

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    return book


@router.post(
    "/",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_book(
    book: BookCreate,
    db: AsyncSession = Depends(get_db)
):

    return await service.create_book(
        db,
        book
    )


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_book(
    book_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    await service.delete_book(
        db,
        book_id
    )

    return