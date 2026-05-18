from pydantic_mongo import PydanticObjectId

from app.core.database import books_collection


class BookRepository:

    async def get_books(
        self,
        limit: int,
        offset: int
    ):

        cursor = (
            books_collection
            .find({})
            .skip(offset)
            .limit(limit)
        )

        books = []

        async for book in cursor:
            book["id"] = book["_id"]
            books.append(book)

        return books

    async def get_book_by_id(
        self,
        book_id: str
    ):

        book = await books_collection.find_one({
            "_id": PydanticObjectId(book_id)
        })

        if not book:
            return None

        book["id"] = book["_id"]

        return book

    async def create_book(
        self,
        book_data
    ):

        data = book_data.model_dump()

        result = await books_collection.insert_one(data)

        created_book = await books_collection.find_one({
            "_id": result.inserted_id
        })

        created_book["id"] = created_book["_id"]

        return created_book

    async def delete_book(
        self,
        book_id: str
    ):

        response = await books_collection.delete_one({
            "_id": PydanticObjectId(book_id)
        })

        return response.deleted_count > 0