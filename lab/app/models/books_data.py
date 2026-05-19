from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.core.database import Base


class Book(Base):

    __tablename__ = "books"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    title = Column(String(255), nullable=False)

    author = Column(String(255), nullable=False)

    description = Column(String(1000))

    status = Column(String(50), nullable=False)

    release_year = Column(Integer, nullable=False)