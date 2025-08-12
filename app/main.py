from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from db import database
from contextlib import asynccontextmanager
from routes import problems
from routes import approaches
from routes import categories
from routes import home 

# To connect to psql in docker:
# docker exec -it lc-tracking-system-db-1 psql -U fastapi_user -d fastapi_db

templates = Jinja2Templates(directory="templates")

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
app.include_router(approaches.router)
app.include_router(categories.router)
app.include_router(home.router)