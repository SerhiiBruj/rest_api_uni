from app.db.mongo import books_collection
from bson import ObjectId

class BookRepository:

    async def get_all(self, skip: int, limit: int):
        cursor = books_collection.find().skip(skip).limit(limit)
        books = await cursor.to_list(length=limit)

        result = []

        for b in books:
            result.append({
                "id": str(b["_id"]),
                "title": b.get("title", ""),
                "author": b.get("author", "")
            })

        return result
    async def get_by_id(self, book_id: str):
        book = await books_collection.find_one({"_id": ObjectId(book_id)})
        if not book:
            return None

        return {
            "id": str(book["_id"]),
            "title": book["title"],
            "author": book["author"]
        }

    async def create(self, data: dict):
        result = await books_collection.insert_one(data)

        created = await books_collection.find_one(
            {"_id": result.inserted_id}
        )

        return {
            "id": str(created["_id"]),
            "title": created["title"],
            "author": created["author"]
        }

    async def delete(self, book_id: str):
        result = await books_collection.delete_one({"_id": ObjectId(book_id)})
        return result.deleted_count > 0