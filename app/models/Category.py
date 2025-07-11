from pydantic import BaseModel
from typing import Optional

class Category(BaseModel):
    id: Optional[int] = None 
    category_name: str