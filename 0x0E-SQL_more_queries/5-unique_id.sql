-- A script that creates the table unique_id,
-- id is unique and has default value 1
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
