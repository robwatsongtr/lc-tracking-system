from pydantic import BaseModel

class Category(BaseModel):
    id: int
    category_name: str