from fastapi import APIRouter, HTTPException
from models.Approach import Approach
from services import approach_service

router = APIRouter(prefix="/approaches", tags=["approaches"])

@router.get("/", response_model=list[Approach])
async def get_approaches():
    try:
        return await approach_service.list_approaches()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))