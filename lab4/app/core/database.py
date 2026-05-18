import motor.motor_asyncio

DATABASE_URL = (
    "mongodb://mongo_admin:password@localhost:27017"
)

client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL
)

database = client.library

books_collection = database.books