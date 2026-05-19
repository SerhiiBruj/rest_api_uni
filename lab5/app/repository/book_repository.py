from pydantic_mongo import PydanticObjectId

from app.core.database import books_collection


class BookRepository:

    def get_books(
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

        for book in cursor:

            book["id"] = str(book["_id"])

            del book["_id"]

            books.append(book)

        return books

    def get_book_by_id(
        self,
        book_id: str
    ):

        book = books_collection.find_one({
            "_id": PydanticObjectId(book_id)
        })

        if not book:
            return None

        book["id"] = str(book["_id"])

        del book["_id"]

        return book

    def create_book(
        self,
        book_data
    ):

        data = book_data.model_dump()

        result = books_collection.insert_one(data)

        created_book = books_collection.find_one({
            "_id": result.inserted_id
        })

        created_book["id"] = str(created_book["_id"])

        del created_book["_id"]

        return created_book

    def delete_book(
        self,
        book_id: str
    ):

        response = books_collection.delete_one({
            "_id": PydanticObjectId(book_id)
        })

        return response.deleted_count > 0