from fastapi import APIRouter, HTTPException
from models.Category import Category
from services import category_service

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("/", response_model=list[Category])
async def get_categories():
    try:
        return await category_service.list_categories()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", response_model=Category)
async def create_category(category: Category):
    try:
        return await category_service.create_category(category)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/{category_id}", response_model=Category)
async def update_category(category_id: int, category: Category):
    try:
        return await category_service.update_category_by_id(category_id, category)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/{category_id}")
async def delete_category(category_id: int):
    try:
        return await category_service.delete_category_by_id(category_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
