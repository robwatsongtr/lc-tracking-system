from fastapi import FastAPI
from app.db import database
from contextlib import asynccontextmanager
from app.routes import problems

# To connect to psql in docker:
# docker exec -it fastapi-postgres-docker-db-1 psql -U fastapi_user -d fastapi_db


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