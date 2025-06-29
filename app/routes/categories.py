from fastapi import APIRouter
from app.models.Category import Category

router = APIRouter(prefix="/categories", tags=["categories"])