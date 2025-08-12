from fastapi import APIRouter, Request
from models.Problem import Problem
from models.ProblemCreate import ProblemCreate
from models.ProblemUpdate import ProblemUpdate
from fastapi.templating import Jinja2Templates
from services import problem_service
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/problems", tags=["Problems"])
templates = Jinja2Templates(directory="templates")



"""
Template / Form endponts 
"""
@router.get("/html", response_class=HTMLResponse)
async def get_problems_handler_html(request: Request):
    problems = await problem_service.list_problems()
    return templates.TemplateResponse("problems_list.html", {
        "request": request,
        "problems": problems,
    })

@router.get("/form")
async def create_problem_form_handler(request: Request):
    form_data = await request.form()
    data_dict = dict(form_data)

    


"""
JSON Endponts 
"""
@router.get("/json", response_model=list[Problem])
async def get_problems_handler():
    return await problem_service.list_problems()


@router.get("/json/{problem_id}", response_model=Problem)
async def get_problem_by_id_handler(problem_id: int):
    return await problem_service.get_problem_by_id(problem_id)

    
@router.post("/json", response_model=Problem)
async def create_problem_handler(problem: ProblemCreate):
    return await problem_service.create_problem_with_categories(problem)


@router.put("/json/{problem_id}", response_model=Problem)
async def update_problem_handler(problem_id: int, problem: ProblemUpdate):
    return await problem_service.update_problem_by_id(problem_id, problem)


@router.delete("/json/{problem_id}")
async def delete_problem_handler(problem_id: int):
    return await problem_service.delete_problem_by_id(problem_id)


