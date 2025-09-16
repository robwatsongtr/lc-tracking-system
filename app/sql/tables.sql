/* 
App tables
*/

CREATE TABLE problems (
    id SERIAL PRIMARY KEY,
    leetcode_num INTEGER,
    problem_name VARCHAR(100),
    approach_id INTEGER,
    problem_solution TEXT, 
    diff_id INTEGER,
    CONSTRAINT fk_approach
        FOREIGN KEY (approach_id)
        REFERENCES approaches (id)
        ON DELETE SET NULL,
    CONSTRAINT fk_difficulty
        FOREIGN KEY (diff_id)
        REFERENCES difficulties (id)
        ON DELETE SET NULL
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category_name VARCHAR(100)
);

CREATE TABLE approaches (
    id SERIAL PRIMARY KEY,
    approach_name VARCHAR(100)
);

CREATE TABLE difficulties (
    id SERIAL PRIMARY KEY,
    diff_level VARCHAR(20)
);

CREATE TABLE problem_categories (
    problem_id INTEGER,
    category_id INTEGER,
    PRIMARY KEY (problem_id, category_id),
    CONSTRAINT fk_problem
        FOREIGN KEY (problem_id)
        REFERENCES problems (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_category
        FOREIGN KEY (category_id)
        REFERENCES categories (id)
        ON DELETE CASCADE
);

