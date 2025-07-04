from fastapi import APIRouter, HTTPException
from models.Problem import Problem
from services import problem_service

router = APIRouter(prefix="/problems", tags=["problems"])

@router.get("/", response_model=list[Problem])
async def get_problems():
    try:
        return await problem_service.list_problems()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))