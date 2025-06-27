from pydantic import BaseModel
from typing import Optional

class Problem(BaseModel):
    id: int
    lc_num: int
    problem_name: str
    problem_desc: str 
    approach_id: Optional[int] = None
    problem_solution: str
    diff_id: Optional[int] = None

class Category(BaseModel):
    id: int
    category_name: str

class Approach(BaseModel):
    id: int
    approach_name: str

class Difficulty(BaseModel):
    id: int
    diff_level: str

class ProblemCategories(BaseModel):
    problem_id: int
    category_id: int