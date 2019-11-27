-- Script that creates the table id_not_null on your MySQL server.
-- id = INT with default value of 1.
-- name = VARCHAR of length: 256.
CREATE TABLE IF NOT EXISTS id_not_null
(id INT DEFAULT '1', name VARCHAR(256));
