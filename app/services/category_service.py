from db import database
from models.Category import Category
from fastapi import HTTPException
from .row_check import row_exists

async def list_categories() -> list[Category]:
    query = """
        SELECT  c.id, c.category_name
        FROM categories c
    """
    rows = await database.fetch_all(query)
    response = [Category(**row) for row in rows]

    return response


async def create_category(category: Category) -> Category:
    query = """
        INSERT INTO categories (category_name)
        VALUES (:category_name)
        RETURNING id, category_name
    """
    values = category.model_dump(exclude_unset=True)
    row = await database.fetch_one(query, values=values)

    return Category(**row)


async def update_category_by_id(category_id: int, category: Category) -> Category:
    values = category.model_dump(exclude_unset=True)
    values['id'] = category_id
    if not values:
        raise HTTPException(status_code=400, detail="No fields provided to update")
    query = """
        UPDATE categories
        SET category_name = :category_name
        WHERE id = :id
        RETURNING id, category_name
    """
    row = await database.fetch_one(query=query, values=values)
    if row is None:
        raise HTTPException(
            status_code=404, detail=f"Category with id {category_id} not found"
        )
   
    return Category(**row)


async def delete_category_by_id(category_id: int) -> dict:
    exists = await row_exists(category_id, 'categories')
    if not exists:
        raise HTTPException(status_code=404, 
            detail=f"Category with id {category_id} not found"
        )

    values={ "id": category_id }
    query = """
        DELETE FROM categories WHERE id = :id 
    """
    await database.execute(query=query, values=values)  
    response = { "message": f"Item {category_id} deleted successfully" }

    return response 