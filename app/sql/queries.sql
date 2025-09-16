/*
Useful queries 
*/

/* written order of clauses in queries */
SELECT columns_or_expressions
FROM table1
[JOIN table2 ON join_condition ...]
WHERE filter_conditions
GROUP BY columns
HAVING filter_on_aggregates
ORDER BY columns
LIMIT number OFFSET number;


SELECT 
    p.id, 
    p.leetcode_num, 
    p.problem_name, 
    p.approach_id, 
    p.diff_id, 
    a.approach_name AS approach_name,
    d.diff_level,
    STRING_AGG(c.category_name, ',') AS categories
FROM problems p
LEFT JOIN approaches a ON p.approach_id = a.id
LEFT JOIN difficulties d ON p.diff_id = d.id

/* SQL looks in problem_categories for all rows where problem_id matches.*/
LEFT JOIN problem_categories pc ON pc.problem_id = p.id

/*
For each of those intermediate rows, SQL pulls the actual 
category_name from categories. Now each problem row is 
duplicated once per category: one row per problem–category pair.
*/
LEFT JOIN categories c ON c.id = pc.category_id

WHERE d.diff_level = 'Medium'
GROUP BY 
    p.id, p.leetcode_num, p.problem_name, p.approach_id, 
    p.diff_id, a.approach_name, d.diff_level
;






