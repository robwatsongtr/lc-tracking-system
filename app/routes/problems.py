from fastapi import APIRouter, Request, HTTPException, Query
from fastapi.responses import RedirectResponse
from models.Problem import Problem
from models.ProblemCreate import ProblemCreate
from models.ProblemUpdate import ProblemUpdate
from models.ProblemSearch import ProblemSearch
from fastapi.templating import Jinja2Templates
from services import problem_service
from services import approach_service
from services import category_service
from services import difficulty_service
from typing import Optional, List
import asyncpg

router = APIRouter(prefix="/problems", tags=["Problems"])
templates = Jinja2Templates(directory="templates")

"""
Template / Form Endpoints 
"""
@router.get("/html", name="list_problems_html")
async def list_problems_html(request: Request):
    problems = await problem_service.list_problems()

    return templates.TemplateResponse("problems_list.html", {
        "request": request,
        "problems": problems,
    })


@router.post("/html/{problem_id}/delete", name="delete_problem_post")
async def delete_problem_post(request: Request, problem_id: int):
    await problem_service.delete_problem_by_id(problem_id)

    return RedirectResponse(
        url=request.url_for("list_problems_html"),
        status_code=303
    )


@router.get("/html/new", name="show_problem_create_form")
async def show_problem_create_form(request: Request):
    approaches = await approach_service.list_approaches()
    categories = await category_service.list_categories()
    difficulties = await difficulty_service.list_difficulties()

    return templates.TemplateResponse("problem_create.html", {
        "request": request,
        "approaches": approaches,
        "categories": categories,
        "difficulties": difficulties
    })

@router.post("/html/create", name="problem_create_handler")
async def problem_create_handler(request: Request):
    try:    
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
    except asyncpg.exceptions.UniqueViolationError:
        raise HTTPException(
            status_code=400, 
            detail="LeetCode number already exists"
        )
    
@router.get("/html/{problem_id}/edit", name="show_problem_edit_form")
async def show_problem_edit_form(request: Request, problem_id: int):
    problem = await problem_service.get_problem_by_id(problem_id)
    approaches = await approach_service.list_approaches()
    categories = await category_service.list_categories()
    difficulties = await difficulty_service.list_difficulties()

    return templates.TemplateResponse("problem_edit.html", {
        "request": request,
        "problem": problem,
        "approaches": approaches,
        "categories": categories,
        "difficulties": difficulties
    })

@router.post("/html/{problem_id}/update", name="problem_edit_handler")
async def problem_edit_handler(request: Request, problem_id: int):
    try:
        form_data = await request.form()
        data_dict = dict(form_data)
        
        if "category_ids" in data_dict:
            data_dict["category_ids"] = [
                int(cid) for cid in form_data.getlist("category_ids")
            ]

        problem_to_update = ProblemUpdate(**data_dict)
        await problem_service.update_problem_by_id(problem_id, problem_to_update)

        return RedirectResponse(
            url=request.url_for("list_problems_html"),
            status_code=303
        )
    except asyncpg.exceptions.UniqueViolationError:
        raise HTTPException(
            status_code=400, 
            detail="LeetCode number already exists"
        )

@router.get("/html/search", name="show_problem_search_form")
async def show_problem_search_form(request: Request):
    approaches = await approach_service.list_approaches()
    categories = await category_service.list_categories()
    difficulties = await difficulty_service.list_difficulties()

    return templates.TemplateResponse("problem_search.html", {
        "request": request,
        "approaches": approaches,
        "categories": categories,
        "difficulties": difficulties
    })    

@router.get("/html/dosearch", name="problem_search_handler")
async def problem_search_handler(
    request: Request, 
    leetcode_num: Optional[str] = Query(None),
    problem_name: Optional[str] = Query(None),
    diff_id: Optional[str] = Query(None),
    category_ids: Optional[List[int]] = Query(None)
):
    
    search_params = ProblemSearch(
        leetcode_num=leetcode_num,
        problem_name=problem_name,
        diff_id=diff_id,
        category_ids=category_ids or []
    )

    print(search_params)


"""
JSON Endpoints 
"""
@router.get("/json", response_model=list[Problem])
async def get_problems_handler():
    return await problem_service.list_problems()


@router.get("/json/{problem_id}", response_model=Problem)
async def get_problem_by_id_handler(problem_id: int):
    return await problem_service.get_problem_by_id(problem_id)

    
@router.post("/json", response_model=Problem)
async def create_problem_handler(problem: ProblemCreate):
    try:
        return await problem_service.create_problem_with_categories(problem)
    except asyncpg.exceptions.UniqueViolationError:
        raise HTTPException(
            status_code=400, 
            detail="LeetCode number already exists"
        )


@router.put("/json/{problem_id}", response_model=Problem)
async def update_problem_handler(problem_id: int, problem: ProblemUpdate):
    try:
        return await problem_service.update_problem_by_id(problem_id, problem)
    except asyncpg.exceptions.UniqueViolationError:
        raise HTTPException(
            status_code=400, 
            detail="LeetCode number already exists"
        )


@router.delete("/json/{problem_id}")
async def delete_problem_handler(problem_id: int):
    return await problem_service.delete_problem_by_id(problem_id)


