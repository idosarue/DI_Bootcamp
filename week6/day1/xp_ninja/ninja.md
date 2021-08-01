-- Database: bootcam

-- DROP DATABASE bootcam;

-- CREATE DATABASE bootcam
--     WITH 
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_United States.1255'
--     LC_CTYPE = 'English_United States.1255'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;

SELECT first_name, last_name FROM students ORDER BY last_name ASC LIMIT 4;

SELECT first_name, last_name, birth_date FROM students ORDER BY birth_date DESC LIMIT 1
