from pydantic import BaseModel
from typing import Optional, List

class ProblemUpdate(BaseModel):
    leetcode_num: Optional[int] = None
    problem_name: Optional[str] = None
    approach_id: Optional[int] = None
    problem_solution: Optional[str] = None
    diff_id: Optional[int] = None
    category_ids: Optional[List[int]] = None
