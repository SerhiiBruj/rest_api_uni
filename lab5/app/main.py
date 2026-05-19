from flask import Flask
from flask_restful import Api
from flasgger import Swagger

from app.api.books import (
    BooksResource,
    BookResource
)

app = Flask(__name__)

api = Api(app)

swagger = Swagger(app)

api.add_resource(
    BooksResource,
    "/books"
)

api.add_resource(
    BookResource,
    "/books/<string:book_id>"
)

if __name__ == "__main__":
    app.run(debug=True)