from pydantic import BaseModel, Field
from typing import Optional, List

class ProblemCreate(BaseModel):
    leetcode_num: int
    problem_name: str
    problem_desc: Optional[str] = None
    approach_id: Optional[int] = None
    problem_solution: Optional[str] = None
    diff_id: Optional[int] = None
    category_ids: Optional[List[int]] = Field(default_factory=list)
