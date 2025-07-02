from pydantic import BaseModel
from typing import Optional, List
from .Category import Category

class Problem(BaseModel):
    id: int
    leetcode_num: int
    problem_name: str
    problem_desc: str 
    approach_id: Optional[int] = None
    problem_solution: str
    diff_id: Optional[int] = None
    # foreign fields 
    approach_name: Optional[str]
    diff_level: Optional[str]
    categories: List[Category]  