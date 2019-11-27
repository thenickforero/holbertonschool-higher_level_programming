-- Script that creates the table unique_id on your MySQL server.
-- id = INT with default value of 1 and must be unique.
-- name = VARCHAR of length: 256.
CREATE TABLE IF NOT EXISTS unique_id
(id INT DEFAULT '1' UNIQUE, name VARCHAR(256));
