from db import database
from models.Problem import Problem
import json
from .utils import row_exists
from .utils import build_sql_set_clause
from fastapi import HTTPException

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
        JOIN approaches a ON p.approach_id = a.id
        JOIN difficulties d ON p.diff_id = d.id
        LEFT JOIN problem_categories pc ON pc.problem_id = p.id
        LEFT JOIN categories c ON c.id = pc.category_id
        GROUP BY 
            p.id, p.leetcode_num, p.problem_desc, p.approach_id, 
            p.problem_solution, p.diff_id, a.approach_name, d.diff_level
    """
    rows = await database.fetch_all(query)
    response = []
    for row in rows:
        # convert row into standard dict 
        row_dict = dict(row)
        # Parse the JSON string into a Python list
        row_dict['categories'] = json.loads(row_dict['categories'])
        # repack row back into a Pyndantic dict
        response.append(Problem(**row_dict))
    return response

async def create_problem(problem: Problem) -> Problem:
    values = problem.model_dump(exclude_unset=True)
    query = """
        INSERT INTO problems (
            leetcode_num,
            problem_name,
            problem_desc,
            approach_id,
            problem_solution,
            diff_id   
        )
        VALUES (
            :leetcode_num,
            :problem_name,
            :problem_desc,
            :approach_id,
            :problem_solution,
            :diff_id
        )
        RETURNING 
            id, 
            leetcode_num,
            problem_name,
            problem_desc,
            approach_id,
            problem_solution,
            diff_id   
    """
    row = await database.fetch_one(query, values=values)

    return Problem(**row)


async def update_problem_by_id(problem_id: int, problem: Problem) -> Problem:
    values = problem.model_dump(exclude_unset=True)
    if not values:
        raise HTTPException(status_code=400, detail="No fields provided to update")
    
    values['id'] = problem_id
    set_clause_str = build_sql_set_clause(values)
    
    query = f"""
        UPDATE problems
        SET {set_clause_str}
        WHERE id = :id
        RETURNING
            id, 
            leetcode_num,
            problem_name,
            problem_desc,
            approach_id,
            problem_solution,
            diff_id   
    """
    row = await database.fetch_one(query=query, values=values)
    if row is None:
        raise HTTPException(
            status_code=404, detail=f"Problem with id {problem_id} not found"
        )
    
    return Problem(**row)


async def delete_problem_by_id(problem_id: int) -> dict:
    exists = await row_exists(problem_id, 'problems')
    if not exists:
        raise HTTPException(status_code=404, 
            detail=f"Problem with id {problem_id} not found"
        )

    values={ "id": problem_id }
    query = """
        DELETE FROM problems WHERE id = :id 
    """
    await database.execute(query=query, values=values)  
    response = { "message": f"Item {problem_id} deleted successfully" }

    return response 

