from fastapi import APIRouter, HTTPException
from models.Problem import Problem
from services import problem_service

router = APIRouter(prefix="/problems", tags=["Problems"])

@router.get("/", response_model=list[Problem])
async def get_problems():
    return await problem_service.list_problems()
    
@router.post("/", response_model=Problem)
async def create_problem(problem: Problem):
    return await problem_service.create_problem(problem)

@router.put("/{problem_id}", response_model=Problem)
async def update_problem(problem_id: int, problem: Problem):
    return await problem_service.update_problem_by_id(problem_id, problem)

@router.delete("/{problem_id}")
async def delete_problem(problem_id: int):
    return await problem_service.delete_problem_by_id(problem_id)


