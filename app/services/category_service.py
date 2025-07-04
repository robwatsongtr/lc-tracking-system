from db import database
from models.Category import Category

async def list_categories() -> list[Category]:
    query = """
        SELECT  c.id, c.category_name
        FROM categories c
    """
    rows = await database.fetch_all(query)
    response = [Category(**row) for row in rows]

    return response
