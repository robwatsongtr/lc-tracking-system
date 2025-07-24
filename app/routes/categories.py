from fastapi import APIRouter
from models.Category import Category
from services import category_service

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=list[Category])
async def get_categories_handler():
    return await category_service.list_categories()


@router.post("/", response_model=Category)
async def create_category_handler(category: Category):
    return await category_service.create_category(category)
 
    
@router.put("/{category_id}", response_model=Category)
async def update_category_handler(category_id: int, category: Category): 
    return await category_service.update_category_by_id(category_id, category)

    
@router.delete("/{category_id}")
async def delete_category_handler(category_id: int):
    return await category_service.delete_category_by_id(category_id)
