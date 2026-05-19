from app.repository.book_repository import BookRepository


class BookService:

    def __init__(self):
        self.repository = BookRepository()

    def get_books(
        self,
        limit,
        offset
    ):

        return self.repository.get_books(
            limit,
            offset
        )

    def get_book(
        self,
        book_id
    ):

        return self.repository.get_book_by_id(
            book_id
        )

    def create_book(
        self,
        book_data
    ):

        return self.repository.create_book(
            book_data
        )

    def delete_book(
        self,
        book_id
    ):

        return self.repository.delete_book(
            book_id
        )