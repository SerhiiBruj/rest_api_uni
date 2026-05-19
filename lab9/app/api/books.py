from fastapi import APIRouter, Query
from app.services.book_service import BookService
from app.core.security import get_current_user
from fastapi import Depends
from app.schemas.book import BookCreate, BookResponse
router = APIRouter()
service = BookService()
from app.core.deps import rate_limited


@router.get("/books")
async def get_books(
    skip: int = 0,
    limit: int = 10,
    _: None = Depends(rate_limited),
    user: str = Depends(get_current_user)
):
    return await service.list_books(skip, limit)

@router.get("/books/{book_id}")
async def get_book(
    book_id: str,
    _: None = Depends(rate_limited)
):
    return await service.get_book(book_id)


@router.post("/books", response_model=BookResponse)
async def create_book(book: BookCreate):
    return await service.create_book(book)


@router.delete("/books/{book_id}")
async def delete_book(book_id: str, user: str = Depends(get_current_user)):
    return await service.delete_book(book_id)