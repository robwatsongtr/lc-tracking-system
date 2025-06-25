from fastapi import FastAPI
from databases import Database
import os
from contextlib import asynccontextmanager

DATABASE_URL = os.getenv("DATABASE_URL")
database = Database(DATABASE_URL)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    try:
        yield
    finally:
        await database.disconnect()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    query = "SELECT now()"
    current_time = await database.fetch_val(query)
    return {"message": "Hello, FastAPI with Postgres!", "time": str(current_time)}
