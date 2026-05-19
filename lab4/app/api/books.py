from flask import request
from flask_restful import Resource

from app.schemas.book import BookCreate
from app.services.book_service import BookService


service = BookService()


class BooksResource(Resource):

    def get(self):
        """
        Get all books
        ---
        tags:
          - Books

        parameters:
          - name: limit
            in: query
            type: integer
            required: false

          - name: offset
            in: query
            type: integer
            required: false

        responses:
          200:
            description: List of books
        """

        limit = int(request.args.get("limit", 10))
        offset = int(request.args.get("offset", 0))

        return service.get_books(
            limit,
            offset
        )

    def post(self):
        """
        Create book
        ---
        tags:
          - Books

        parameters:
          - in: body
            name: body
            schema:
              type: object
              properties:
                title:
                  type: string

                author:
                  type: string

                description:
                  type: string

                status:
                  type: string

                release_year:
                  type: integer

        responses:
          201:
            description: Book created
        """

        data = request.get_json()

        book = BookCreate(**data)

        return service.create_book(book), 201


class BookResource(Resource):

    def get(self, book_id):
        """
        Get book by ID
        ---
        tags:
          - Books

        parameters:
          - name: book_id
            in: path
            type: string
            required: true

        responses:
          200:
            description: Book found

          404:
            description: Book not found
        """

        book = service.get_book_sync(book_id)

        if not book:
            return {
                "message": "Book not found"
            }, 404

        return book

    def delete(self, book_id):
        """
        Delete book
        ---
        tags:
          - Books

        parameters:
          - name: book_id
            in: path
            type: string
            required: true

        responses:
          204:
            description: Book deleted
        """

        deleted = service.delete_book_sync(book_id)

        if not deleted:
            return {
                "message": "Book not found"
            }, 404

        return "", 204