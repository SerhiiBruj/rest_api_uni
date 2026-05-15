from typing import Optional
from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from app.schemas.book import (
    BookCreate,
    BookResponse,
    BookStatus
)

from app.services.book_service import BookService


router = APIRouter(prefix="/books", tags=["Books"])

service = BookService()


@router.get("/", response_model=list[BookResponse])
async def get_books(
    status_filter: Optional[BookStatus] = None,
    author: Optional[str] = None,
    sort_by: Optional[str] = None
):
    return await service.get_books(
        status=status_filter,
        author=author,
        sort_by=sort_by
    )


@router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: UUID):

    book = await service.get_book(book_id)

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
async def create_book(book: BookCreate):

    return await service.create_book(book)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: UUID):

    await service.delete_book(book_id)

    return