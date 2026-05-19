from pymongo import MongoClient

DATABASE_URL = (
    "mongodb://mongo_admin:password@localhost:27017"
)

client = MongoClient(DATABASE_URL)

database = client.library

books_collection = database.books