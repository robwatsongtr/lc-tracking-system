from pydantic import BaseModel
from typing import Optional

class Approach(BaseModel):
    id: Optional[int] = None
    approach_name: str