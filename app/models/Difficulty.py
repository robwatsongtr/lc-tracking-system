from pydantic import BaseModel
from typing import Optional

class Difficulty(BaseModel):
    id: Optional[int] = None 
    diff_level: str

    