from fastapi import APIRouter
from models.Category import Category

router = APIRouter(prefix="/categories", tags=["categories"])