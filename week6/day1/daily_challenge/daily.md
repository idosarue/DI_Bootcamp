-- Database: Holywood

-- DROP DATABASE "Holywood";

-- CREATE DATABASE "Holywood"
--     WITH 
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_United States.1255'
--     LC_CTYPE = 'English_United States.1255'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;

-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- )

-- INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES
-- ('Matt','Damon','1970/10/08', 5),
-- ('George',' Clooney','1961/05/06', 2),
-- ('Scarlett ','Johansson','1984/11/22', 0),
-- ('Meryl','Streep','1949/06/22', 0);

SELECT COUNT(first_name) FROM actors;

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES (null,null,null,null)