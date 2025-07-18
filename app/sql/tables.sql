/* 
CONSTRAINT allows you to give a name (alias) to a constraint. Good for debugging. 
*/


CREATE TABLE problems (
    id SERIAL PRIMARY KEY,
    leetcode_num INTEGER,
    problem_name VARCHAR(100),
    problem_desc TEXT,
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

/*
INSERT INTO categories (category_name) 
VALUES ('Array'), ('String'), ('Hash Map'), ('Intervals');
*/
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) UNIQUE
);

/*
INSERT INTO approach (approach_name) 
VALUES ('Two-Pointer'), ('Sliding Window'), ('Frequendy Counter'), 
('Hash Map lookup'), ('Boyer-Moore'),('BFS');
*/
CREATE TABLE approaches (
    id SERIAL PRIMARY KEY,
    approach_name VARCHAR(100)
);

/*
INSERT INTO difficulty (diff_level) 
VALUES ('Easy'), ('Medium'), ('Hard');
*/
CREATE TABLE difficulties (
    id SERIAL PRIMARY KEY,
    diff_level VARCHAR(20) UNIQUE
);

-- problem_categories join table since many to many relationship
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