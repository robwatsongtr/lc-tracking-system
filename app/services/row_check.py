from db import database

async def row_exists(model_id: int, table_name: str) -> bool:
    values = { "id": model_id}
    query = f'SELECT id from {table_name} WHERE id = :id'
    row = await database.fetch_one(query=query, values=values)

    return row is not None 
