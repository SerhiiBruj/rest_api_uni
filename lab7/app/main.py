from fastapi import FastAPI
from app.api import books, auth

app = FastAPI(title="Library API")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(books.router, tags=["books"])