from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from models.Problem import Problem
from models.ProblemCreate import ProblemCreate
from models.ProblemUpdate import ProblemUpdate
from fastapi.templating import Jinja2Templates
from services import problem_service
from services import approach_service
from services import category_service
from services import difficulty_service


router = APIRouter(prefix="/problems", tags=["Problems"])
templates = Jinja2Templates(directory="templates")

"""
Template / Form endponts 
"""
@router.get("/html", name="list_problems_html")
async def list_problems_html(request: Request):
    problems = await problem_service.list_problems()

    return templates.TemplateResponse("problems_list.html", {
        "request": request,
        "problems": problems,
    })


@router.post("/html/{problem_id}", name="form_delete_problem")
async def form_delete_problem(request: Request, problem_id: int):
    await problem_service.delete_problem_by_id(problem_id)

    return RedirectResponse(
        url=request.url_for("list_problems_html"),
        status_code=303
    )


@router.get("/html/new", name="show_problem_form")
async def show_problem_form(request: Request):
    approaches = await approach_service.list_approaches()
    categories = await category_service.list_categories()
    difficulties = await difficulty_service.list_difficulties()

    return templates.TemplateResponse("problems_form.html", {
        "request": request,
        "approaches": approaches,
        "categories": categories,
        "difficulties": difficulties
    })

@router.post("/html", name="problem_form_handler")
async def problem_form_handler(request: Request):
    form_data = await request.form()
    data_dict = dict(form_data)
    if "category_ids" in data_dict:
        data_dict["category_ids"] = [
            int(cid) for cid in form_data.getlist("category_ids")
        ]

    problem_to_insert = ProblemCreate(**data_dict)
    await problem_service.create_problem_with_categories(problem_to_insert)

    return RedirectResponse(
        url=request.url_for("list_problems_html"),
        status_code=303
    )


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


