from db import database
from models.Approach import Approach

async def list_approaches() -> list[Approach]:
    query = """
        SELECT  a.id, a.approach_name
        FROM approaches a
    """
    rows = await database.fetch_all(query)
    response = [Approach(**row) for row in rows]
    
    return response 

async def create_approach(approach: Approach) -> Approach:
    query = """
        INSERT INTO approaches (approach_name)
        VALUES (:approach_name)
        RETURNING id, approach_name 
    """
    row = await database.fetch_one(query, values=approach.model_dump(exclude_unset=True))
    return Approach(**row)