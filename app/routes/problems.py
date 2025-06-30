from fastapi import APIRouter
from models.Problem import Problem
from services import problem_service

router = APIRouter(prefix="/problems", tags=["problems"])

@router.get("/", response_model=list[Problem])
async def get_problems():
    return problem_service.list_problems()