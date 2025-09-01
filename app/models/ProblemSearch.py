from pydantic import BaseModel, Field, field_validator
from typing import Optional, List

class ProblemSearch(BaseModel):
    leetcode_num: Optional[int] = None
    problem_name: Optional[str] = None
    approach_id: Optional[int] = None
    diff_id: Optional[int] = None
    category_ids: Optional[List[int]] = Field(default_factory=list)

    @field_validator('leetcode_num', 'approach_id', 'diff_id', mode="before")
    def empty_str_to_none(cls, value):
        return None if value == "" else value
    
    