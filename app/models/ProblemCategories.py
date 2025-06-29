from pydantic import BaseModel

class ProblemCategories(BaseModel):
    problem_id: int
    category_id: int


    