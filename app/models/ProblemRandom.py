from pydantic import BaseModel, Field, field_validator
from typing import Optional, List

class ProblemRandom(BaseModel):
    diff_id: Optional[int] = None
    category_ids: Optional[List[int]] = Field(default_factory=list)
    limit: Optional[int] = None

    # @field_validator('leetcode_num', 'approach_id', 'diff_id', mode="before")
    # def empty_str_to_none(cls, value):
    #     return None if value == "" else value