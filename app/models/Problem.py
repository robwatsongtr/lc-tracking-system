from typing import Optional, List
from pydantic import BaseModel, Field 
from .Category import Category

class Problem(BaseModel):
    id: int
    leetcode_num: Optional[int] = None
    problem_name: Optional[str] = None
    problem_desc: Optional[str] = None 
    approach_id: Optional[int] = None
    problem_solution: Optional[str] = None
    diff_id: Optional[int] = None

    approach_name: Optional[str] = None
    diff_level: Optional[str] = None
    categories: List[Category] = Field(default_factory=list)
