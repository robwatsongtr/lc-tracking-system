from fastapi import APIRouter
from models.Approach import Approach

router = APIRouter(prefix="/approaches", tags=["approaches"])