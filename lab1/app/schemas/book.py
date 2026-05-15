from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from uuid import UUID


class BookStatus(str, Enum):
    AVAILABLE = "available"
    BORROWED = "borrowed"


class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    author: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    status: BookStatus
    release_year: int = Field(..., ge=0, le=2100)


class BookResponse(BookCreate):
    id: UUID