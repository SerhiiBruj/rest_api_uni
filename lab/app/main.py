from flask import Flask
from flask_restful import Api
from flasgger import Swagger

from app.api.books import BooksResource, BookResource
from app.auth.router import LoginResource, RefreshResource

app = Flask(__name__)
api = Api(app)

# Swagger UI
swagger = Swagger(app)

# BOOKS
api.add_resource(BooksResource, "/books")
api.add_resource(BookResource, "/books/<string:book_id>")

# AUTH
api.add_resource(LoginResource, "/auth/login")
api.add_resource(RefreshResource, "/auth/refresh")


if __name__ == "__main__":
    app.run(debug=True)