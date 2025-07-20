from fastapi import APIRouter, HTTPException
from models.Approach import Approach
from services import approach_service

router = APIRouter(prefix="/approaches", tags=["approaches"])

@router.get("/", response_model=list[Approach])
async def get_approaches():
    return await approach_service.list_approaches()
    
   
@router.post("/", response_model=Approach)
async def create_approach(approach: Approach):
    return await approach_service.create_approach(approach)

    
@router.put("/{approach_id}", response_model=Approach)
async def update_approach(approach_id: int, approach: Approach):
    return await approach_service.update_approach_by_id(approach_id, approach)

    
@router.delete("/{approach_id}")
async def delete_approach(approach_id: int):
    return await approach_service.delete_approach_by_id(approach_id)


    

    
    
