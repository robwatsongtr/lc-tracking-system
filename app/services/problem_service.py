from db import database
from models.Problem import Problem
from models.ProblemUpdate import ProblemUpdate
from models.ProblemCreate import ProblemCreate
import json
from .utils import row_exists
from .utils import build_sql_set_clause
from .utils import build_search_query
from .utils import clean_values
from fastapi import HTTPException

async def list_problems() -> list[Problem]:
    query = """
        SELECT 
            p.id,
            p.leetcode_num,
            p.problem_name,
            p.approach_id,
            p.problem_solution,
            p.diff_id,
            a.approach_name AS approach_name,
            d.diff_level AS diff_level,
            COALESCE(
                json_agg(
                    DISTINCT jsonb_build_object(
                        'id', c.id, 'category_name', c.category_name
                    )
                )
                FILTER (WHERE c.id IS NOT NULL),
                CAST('[]' AS json)
            ) AS categories
        FROM problems p
        LEFT JOIN approaches a ON p.approach_id = a.id
        LEFT JOIN difficulties d ON p.diff_id = d.id
        LEFT JOIN problem_categories pc ON pc.problem_id = p.id
        LEFT JOIN categories c ON c.id = pc.category_id
        GROUP BY 
            p.id, p.leetcode_num, p.approach_id, p.problem_solution,
            p.diff_id, a.approach_name, d.diff_level
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

async def get_problem_by_id(problem_id: int) -> Problem:
    values={ "id": problem_id }
    query = """
           SELECT 
            p.id,
            p.leetcode_num,
            p.problem_name,
            p.approach_id,
            p.problem_solution,
            p.diff_id,
            a.approach_name AS approach_name,
            d.diff_level AS diff_level,
            COALESCE(
                json_agg(
                    DISTINCT jsonb_build_object(
                        'id', c.id, 'category_name', c.category_name
                    )
                )
                FILTER (WHERE c.id IS NOT NULL),
                CAST('[]' AS json)
            ) AS categories
        FROM problems p
        LEFT JOIN approaches a ON p.approach_id = a.id
        LEFT JOIN difficulties d ON p.diff_id = d.id
        LEFT JOIN problem_categories pc ON pc.problem_id = p.id
        LEFT JOIN categories c ON c.id = pc.category_id
        WHERE p.id = :id
        GROUP BY 
            p.id, p.leetcode_num, p.approach_id, p.problem_solution,
            p.diff_id, a.approach_name, d.diff_level    
    """
    row = await database.fetch_one(query=query, values=values)
    if row is None:
        raise HTTPException(
                status_code=404, detail=f"Problem with id {problem_id} not found")
    
    row_dict = dict(row)
    row_dict['categories'] = json.loads(row_dict['categories'])
    
    return Problem(**row_dict) 
    
async def create_problem_with_categories(problem: ProblemCreate) -> Problem:
    values = problem.model_dump(exclude={"category_ids"}, exclude_unset=True)
    query = """
        INSERT INTO problems (
            leetcode_num,
            problem_name,
            approach_id,
            problem_solution,
            diff_id   
        )
        VALUES (
            :leetcode_num,
            :problem_name,
            :approach_id,
            :problem_solution,
            :diff_id
        )
        RETURNING id 
    """
    row = await database.fetch_one(query, values=values)
    problem_id = row["id"]

    # fill the problem_categories join table 
    if problem.category_ids:
        category_inserts = [
            { "problem_id" : problem_id, "category_id" : category_id }
            for category_id in problem.category_ids
        ]
        await database.execute_many(
            """
            INSERT INTO problem_categories (problem_id, category_id)
            VALUES (:problem_id, :category_id)
            """,
            category_inserts
        )
  
    return await get_problem_by_id(problem_id)

async def update_problem_by_id(problem_id: int, problem: ProblemUpdate) -> Problem:
    values = problem.model_dump(exclude={"category_ids"}, exclude_unset=True)
    if not values:
        raise HTTPException(status_code=400, detail="No fields provided to update")
    # transfer the provided id into values 
    values['id'] = problem_id 
    set_clause_str = build_sql_set_clause(values)

    query = f"""
        UPDATE problems
        SET {set_clause_str}
        WHERE id = :id
    """
    # Before running UPDATE, check if row exists
    exists = await row_exists(problem_id, 'problems')
    if not exists:
        raise HTTPException(status_code=404, 
            detail="Problem with id {problem_id} not found"
        )
    
    await database.execute(query=query, values=values)

    # handling the problem_categories join table 
    if problem.category_ids is not None:
        # clear existing relationships
        delete_old_ids_query = """
            DELETE FROM problem_categories WHERE problem_id = :problem_id
        """
        old_ids = { "problem_id" : problem_id }
        await database.execute(query=delete_old_ids_query, values=old_ids)
    
        # Insert new relationships if provided
        if problem.category_ids:
            category_inserts = [
                { "problem_id" : problem_id, "category_id" : category_id }
                for category_id in problem.category_ids
            ]
            await database.execute_many(
                """
                INSERT INTO problem_categories (problem_id, category_id)
                VALUES (:problem_id, :category_id)
                """,
                category_inserts
            )

    return await get_problem_by_id(problem_id)


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

async def search_problems(search_params: Problem):
    values = search_params.model_dump()
    # print(f'model dumped values: {values}')

    # only keys with real values are kept 
    cleaned_values = clean_values(values)
    #print(f'cleaned values: {cleaned_values}')

    search_query_str = build_search_query(cleaned_values)
    # print(f'search query string: {search_query_str}')

    query = f'{search_query_str}'
    rows = await database.fetch_all(query, values=cleaned_values)

    response = []
    for row in rows:
        row_dict = dict(row)
        row_dict['categories'] = json.loads(row_dict['categories'])
        response.append(Problem(**row_dict))

    return response
