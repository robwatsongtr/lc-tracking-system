/* 
CONSTRAINT allows you to give a name (alias) to a constraint. Good for debugging. 
*/

/* 
CSV import staging table
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

/*
INSERT INTO categories (category_name) 
VALUES ('Array'), ('String'), ('Hash Map'), ('Intervals');
*/
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category_name VARCHAR(100)
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
    diff_level VARCHAR(20)
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


