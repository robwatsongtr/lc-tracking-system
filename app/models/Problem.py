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