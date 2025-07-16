from db import database
from models.Approach import Approach
from fastapi import HTTPException

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
    values = approach.model_dump(exclude_unset=True)
    row = await database.fetch_one(query, values=values)
    response = Approach(**row)

    return response 


async def update_approach_by_id(approach_id: int, approach: Approach) -> Approach:
    values = approach.model_dump(exclude_unset=True)
    values['id'] = approach_id
    if not values:
        raise HTTPException(status_code=400, detail="No fields provided to update")

    query = """
        UPDATE approaches
        SET approach_name = :approach_name
        WHERE id = :id
        RETURNING id, approach_name
    """
    row = await database.fetch_one(query=query, values=values)
    if row is None:
        raise HTTPException(
            status_code=404, detail=f"Approach with id {approach_id} not found"
        )
    response = Approach(**row) 

    return response 

async def delete_approach_by_id(approach_id: int) -> dict:
    values={ "id": approach_id }
    query = """
        DELETE FROM approaches 
        WHERE id = :id 
    """
    row = await database.fetch_one(query=query, values=values)

    if row is None:
        raise HTTPException(status_code=404, 
            detail=f"Approach with id {approach_id} not found"
        )
       
    
    response = { "message": f"Item {approach_id} deleted successfully" }

    return response 
