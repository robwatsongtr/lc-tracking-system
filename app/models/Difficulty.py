from pydantic import BaseModel

class Difficulty(BaseModel):
    id: int
    diff_level: str

    