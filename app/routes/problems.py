from fastapi import APIRouter
from models.Problem import Problem
from models.ProblemCreate import ProblemCreate
from models.ProblemUpdate import ProblemUpdate
from services import problem_service

router = APIRouter(prefix="/problems", tags=["Problems"])

@router.get("/", response_model=list[Problem])
async def get_problems_handler():
    return await problem_service.list_problems()
    
@router.post("/", response_model=Problem)
async def create_problem_handler(problem: ProblemCreate):
    return await problem_service.create_problem_with_categories(problem)

@router.put("/{problem_id}", response_model=Problem)
async def update_problem_handler(problem_id: int, problem: ProblemUpdate):
    return await problem_service.update_problem_by_id(problem_id, problem)

@router.delete("/{problem_id}")
async def delete_problem_handler(problem_id: int):
    return await problem_service.delete_problem_by_id(problem_id)


