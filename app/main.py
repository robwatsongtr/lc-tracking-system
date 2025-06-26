from fastapi import FastAPI
from app.db import database
from contextlib import asynccontextmanager
from app.routes import problems

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    try:
        yield
    finally:
        await database.disconnect()

# Swagger UI at http://localhost:8000/docs
app = FastAPI(
    lifespan=lifespan, 
    title="Leetcode Problem Tracker API", 
)

app.include_router(problems.router)