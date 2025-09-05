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

def build_search_query(values: dict) -> str:
    filters_arr = []

    for key in values:
        if key == "problem_name":
            # partial string match with ILIKE
            filters_arr.append(f" AND {key} ILIKE '%' || :{key} || '%'")
        elif key == "category_ids":
            filters_arr.append(f' AND pc.category_id = ANY(:category_ids)')
        else:
            filters_arr.append(f" AND {key} = :{key}")

    filters = " ".join(filters_arr)

    query = f"""
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
        WHERE 1 = 1 
            {filters}
        GROUP BY 
            p.id, p.leetcode_num, p.approach_id, p.problem_solution,
            p.diff_id, a.approach_name, d.diff_level    
    """
    
    return query 

def clean_values(values: dict) -> dict:
    cleaned_values = {}
    for key, value in values.items():
        # strip empty string, none or empty list keys
        if value not in ("", None, []):
            cleaned_values[key] = value

    return cleaned_values
