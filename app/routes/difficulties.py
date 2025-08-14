from fastapi import APIRouter
from models.Difficulty import Difficulty
from services import difficulty_service

router = APIRouter(prefix="/difficulties", tags=["Difficulties"])

@router.get("/json", response_model=list[Difficulty])
async def get_difficulties_handler():
    return await difficulty_service.list_difficulties()

