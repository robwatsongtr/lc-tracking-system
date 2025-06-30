from db import database
from models.Problem import Problem

# 'Read'
async def list_problems() -> list[Problem]:
    query = """
        SELECT id, lc_num, problem_name, problem_desc, problem_solution
        FROM problems
    """
    rows = await database.fetch_all(query)
    # The ** is used to unpack a dictionary into keyword arguments.
    return [Problem(**row) for row in rows]

# 'Create'

# 'Update'

# 'Delete' 

