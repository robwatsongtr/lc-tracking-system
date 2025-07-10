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
    
@router.post("/", response_model=Approach)
async def create_approach(approach: Approach):
    try:
        return await approach_service.create_approach(approach)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
