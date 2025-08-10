from fastapi import APIRouter
from models.Approach import Approach
from services import approach_service

router = APIRouter(prefix="/approaches", tags=["Approaches"])

@router.get("/json", response_model=list[Approach])
async def get_approaches_handler():
    return await approach_service.list_approaches()
    
   
@router.post("/json", response_model=Approach)
async def create_approach_handler(approach: Approach):
    return await approach_service.create_approach(approach)

    
@router.put("/json/{approach_id}", response_model=Approach)
async def update_approach_handler(approach_id: int, approach: Approach):
    return await approach_service.update_approach_by_id(approach_id, approach)

    
@router.delete("/json/{approach_id}")
async def delete_approach_handler(approach_id: int):
    return await approach_service.delete_approach_by_id(approach_id)


    

    
    
