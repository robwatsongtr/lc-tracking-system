from fastapi import APIRouter
from app.models.Approach import Appproach

router = APIRouter(prefix="/approaches", tags=["approaches"])