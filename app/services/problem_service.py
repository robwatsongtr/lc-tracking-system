from db import database
from models.Problem import Problem
import json

# 'Read'
async def list_problems() -> list[Problem]:
    query = """
        SELECT 
            p.id,
            p.leetcode_num,
            p.problem_name,
            p.problem_desc,
            p.approach_id,
            p.problem_solution,
            p.diff_id,
            a.approach_name AS approach_name,
            d.diff_level AS diff_level,
            COALESCE(
                json_agg(DISTINCT jsonb_build_object('id', c.id, 'category_name', c.category_name))
                FILTER (WHERE c.id IS NOT NULL),
                CAST('[]' AS json)
            ) AS categories
        FROM problems p
        JOIN approach a ON p.approach_id = a.id
        JOIN difficulty d ON p.diff_id = d.id
        LEFT JOIN problem_categories pc ON pc.problem_id = p.id
        LEFT JOIN categories c ON c.id = pc.category_id
        GROUP BY 
            p.id, p.leetcode_num, p.problem_desc, p.approach_id, 
            p.problem_solution, p.diff_id, a.approach_name, d.diff_level
    """
    rows = await database.fetch_all(query)
    result = []
    for row in rows:
        row_dict = dict(row)
        # Parse the JSON string into a Python list
        row_dict['categories'] = json.loads(row_dict['categories'])
        result.append(Problem(**row_dict))
    return result

# 'Create'

# 'Update'

# 'Delete' 

