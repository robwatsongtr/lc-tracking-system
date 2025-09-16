/* 
CSV import staging table.
Spreadsheet was normalized to this table and the decision was made to have two category columns
There could be more, I would just do more inserts into the join table. 
*/

CREATE TABLE staging_problems (
    leetcode_num INTEGER UNIQUE,
    diff_level VARCHAR(20),
    category_1 VARCHAR(100),
    category_2 VARCHAR(100),
    approach_name VARCHAR(100),
    problem_name VARCHAR(100),
    problem_solution TEXT
);

/*
Assuming approaches and difficulties are already populated and you can join them by name:
*/
INSERT INTO problems (leetcode_num, problem_name, approach_id, problem_solution, diff_id)
SELECT
    s.leetcode_num,
    s.problem_name,
    a.id AS approach_id,
    s.problem_solution,
    d.id AS diff_id
FROM staging_problems s
LEFT JOIN approaches a ON s.approach_name = a.approach_name
LEFT JOIN difficulties d ON s.diff_level = d.diff_level;


/*
Insert into problem_categories for category_1
You're joining from problem table to staging problems table by leetcode_num natural key
*/
INSERT INTO problem_categories (problem_id, category_id)
SELECT
    p.id AS problem_id,
    c.id AS category_id
FROM staging_problems s
JOIN problems p ON p.leetcode_num = s.leetcode_num   -- link to newly inserted problem
JOIN categories c ON s.category_1 = c.category_name
WHERE s.category_1 IS NOT NULL;


/*
Insert into problem_categories for category_2
*/
INSERT INTO problem_categories (problem_id, category_id)
SELECT
    p.id AS problem_id,
    c.id AS category_id
FROM staging_problems s
JOIN problems p ON p.leetcode_num = s.leetcode_num
JOIN categories c ON s.category_2 = c.category_name
WHERE s.category_2 IS NOT NULL;
