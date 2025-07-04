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