from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from models.Category import Category
from fastapi.templating import Jinja2Templates
from services import category_service

router = APIRouter(prefix="/categories", tags=["Categories"])
templates = Jinja2Templates(directory="templates")

"""
Template / Form Endpoints 
"""
@router.get("/html", name="list_categories_html")
async def list_categories_html(request: Request):
    categories = await category_service.list_categories()

    return templates.TemplateResponse("categories_list.html", {
        "request": request,
        "categories": categories
    })


@router.post("/html/{category_id}", name="delete_category_post")
async def delete_category_post(request: Request, category_id: int):
    await category_service.delete_category_by_id(category_id)

    return RedirectResponse(
        url=request.url_for("list_categories_html"),
        status_code=303
    )

@router.get("/html/new", name="show_category_form")
async def show_category_form(request: Request):
    return templates.TemplateResponse("categories_form.html", {
        "request": request
    })
    
@router.post("/html", name="category_form_handler")
async def category_form_handler(request: Request):
    form_data = await request.form()
    data_dict = dict(form_data)

    category_to_insert = Category(**data_dict)
    await category_service.create_category(category_to_insert)

    return RedirectResponse(
        url=request.url_for("list_categories_html"),
        status_code=303
    )


"""
JSON Endpoints
"""

@router.get("/json", response_model=list[Category])
async def get_categories():
    return await category_service.list_categories()


@router.post("/json", response_model=Category)
async def create_category(category: Category):
    return await category_service.create_category(category)
 
    
@router.put("/json/{category_id}", response_model=Category)
async def update_category(category_id: int, category: Category): 
    return await category_service.update_category_by_id(category_id, category)

    
@router.delete("/json/{category_id}")
async def delete_category(category_id: int):
    return await category_service.delete_category_by_id(category_id)
