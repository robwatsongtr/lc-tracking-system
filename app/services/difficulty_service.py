from db import database
from models.Difficulty import Difficulty

async def list_difficulties() -> list[Difficulty]:
    query = """
        SELECT d.id, d.diff_level
        FROM difficulties d
    """
    rows = await database.fetch_all(query)
    response = [Difficulty(**row) for row in rows]

    return response