from pydantic import BaseModel
from typing import Optional, List
from .Category import Category

class Problem(BaseModel):
    id: Optional[int] = None
    leetcode_num: Optional[int] = None
    problem_name: Optional[str] = None
    problem_desc: Optional[str] = None 
    approach_id: Optional[int] = None
    problem_solution: Optional[str] = None
    diff_id: Optional[int] = None

    # input only POST insert into JOIN table
    category_ids: Optional[List[int]] = []

    # output foreign fields for GET
    approach_name: Optional[str]
    diff_level: Optional[str]
    categories: List[Category] = []