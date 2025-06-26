from pydantic import BaseModel

class Problem(BaseModel):
    id: int
    lc_num: int
    problem_name: str
    problem_solution: str
    category_id: int
    approach_id: int 
