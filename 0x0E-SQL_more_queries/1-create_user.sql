-- Script that creates the MySQL server user:
-- user_0d_1 with all privileges and certain password.
CREATE USER user_0d_1@localhost
IDENTIFIED BY 'user_0d_1_pwd';
-- all databases . all tables
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
