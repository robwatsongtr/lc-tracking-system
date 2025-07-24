from db import database

async def row_exists(model_id: int, table_name: str) -> bool:
    values = { "id": model_id}
    query = f'SELECT id from {table_name} WHERE id = :id'
    row = await database.fetch_one(query=query, values=values)

    return row is not None 

def build_sql_set_clause(values: dict) -> str:
    set_clauses_list = []
    for key in values:
        if key != "id":
            set_clauses_list.append(f"{key} = :{key}")

    return ", ".join(set_clauses_list)
