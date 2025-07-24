from pydantic import BaseModel
from typing import Optional, List
from .Category import Category

class Problem(BaseModel):
    id: Optional[int] = None
    leetcode_num: int
    problem_name: str
    problem_desc: str 
    approach_id: Optional[int] = None
    problem_solution: str
    diff_id: Optional[int] = None
    # input only POST insert into JOIN table
    category_ids: List[int] = []
    # output foreign fields for GET
    approach_name: Optional[str]
    diff_level: Optional[str]
    categories: List[Category] = []