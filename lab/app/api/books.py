from flask import request
from flask_restful import Resource

from app.auth.dependencies import get_current_user
from app.schemas.book import BookCreate
from app.services.book_service import BookService


service = BookService()


class BooksResource(Resource):

    def get(self):
        """
        Get all books (protected)
        ---
        tags:
          - Books
        """

        user = get_current_user()
        if not user:
            return {"message": "Unauthorized"}, 401

        limit = int(request.args.get("limit", 10))
        offset = int(request.args.get("offset", 0))

        return service.get_books(limit, offset)

    def post(self):
        """
        Create book (protected)
        ---
        tags:
          - Books
        """

        user = get_current_user()
        if not user:
            return {"message": "Unauthorized"}, 401

        data = request.get_json()

        book = BookCreate(**data)

        return service.create_book(book), 201


class BookResource(Resource):

    def get(self, book_id):
        """
        Get book by ID (protected)
        ---
        tags:
          - Books
        """

        # 🔐 JWT CHECK
        user = get_current_user()
        if not user:
            return {"message": "Unauthorized"}, 401

        book = service.get_book(book_id)

        if not book:
            return {"message": "Book not found"}, 404

        return book

    def delete(self, book_id):
        """
        Delete book (protected)
        ---
        tags:
          - Books
        """

        user = get_current_user()
        if not user:
            return {"message": "Unauthorized"}, 401

        deleted = service.delete_book(book_id)

        if not deleted:
            return {"message": "Book not found"}, 404

        return "", 204