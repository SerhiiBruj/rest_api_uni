from fastapi import FastAPI

from app.api.books import router as books_router

from app.core.database import (
    engine,
    Base
)


app = FastAPI(
    title="Library API"
)


@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(books_router)