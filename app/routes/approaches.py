from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from models.Approach import Approach
from fastapi.templating import Jinja2Templates
from services import approach_service

router = APIRouter(prefix="/approaches", tags=["Approaches"])
templates = Jinja2Templates(directory="templates")

"""
Template / Form Endpoints 
"""
@router.get("/html", name="list_approaches_html")
async def list_approaches_html(request: Request):
    approaches = await approach_service.list_approaches()

    return templates.TemplateResponse("approaches_list.html", {
        "request": request,
        "approaches": approaches
    })


@router.post("/html/{approach_id}", name="delete_approach_post")
async def delete_approach_post(request: Request, approach_id: int):
    await approach_service.delete_approach_by_id(approach_id)

    return RedirectResponse(
        url=request.url_for("list_approaches_html"),
        status_code=303
    )


@router.get("/html/new", name="show_approach_form")
async def show_approach_form(request: Request):
    return templates.TemplateResponse("approaches_form.html", {
        "request": request
    })


@router.post("/html", name="approach_form_handler")
async def approach_form_handler(request: Request):
    form_data = await request.form()
    data_dict = dict(form_data)

    approach_to_insert = Approach(**data_dict)
    await approach_service.create_approach(approach_to_insert)

    return RedirectResponse(
        url=request.url_for("list_approaches_html"),
        status_code=303
    )


"""
JSON Endpoints
"""
@router.get("/json", response_model=list[Approach])
async def get_approaches():
    return await approach_service.list_approaches()
    
   
@router.post("/json", response_model=Approach)
async def create_approach(approach: Approach):
    return await approach_service.create_approach(approach)

    
@router.put("/json/{approach_id}", response_model=Approach)
async def update_approach(approach_id: int, approach: Approach):
    return await approach_service.update_approach_by_id(approach_id, approach)

    
@router.delete("/json/{approach_id}")
async def delete_approach(approach_id: int):
    return await approach_service.delete_approach_by_id(approach_id)


    

    
    
