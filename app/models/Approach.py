from pydantic import BaseModel

class Approach(BaseModel):
    id: int
    approach_name: str