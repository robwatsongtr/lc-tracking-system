from fastapi import APIRouter
from app.db import database
from app.models.problem import Problem

router = APIRouter(prefix="/problems", tags=["problems"])

@router.get("/", response_model=list[Problem])
async def get_problems():
    query = "SELECT id, lc_num, problem_name, problem_solution FROM problems"
    rows = await database.fetch_all(query)
    return [Problem(**row) for row in rows]
