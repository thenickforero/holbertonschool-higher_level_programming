-- Script that creates the database hbtn_0d_usa and the table states
-- in the database hbtn_0d_usa on your MySQL server.
-- id = INT auto generated not null which is primary key and must be unique.
-- name = VARCHAR not null of length: 256.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
