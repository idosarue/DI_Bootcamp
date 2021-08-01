
-- Database: public

-- DROP DATABASE public;

-- CREATE DATABASE public
--     WITH 
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_United States.1255'
--     LC_CTYPE = 'English_United States.1255'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;

-- CREATE TABLE items(
-- 	item_name VARCHAR (20) NOT NULL,
-- 	price smallint NOT NULL
-- )
-- INSERT INTO items (item_name, price)
-- VALUES ('Fan', 80)

-- CREATE TABLE customers (
-- 	first_name VARCHAR (10) NOT NULL,
-- 	last_name VARCHAR (10) NOT NULL
-- )

-- INSERT INTO customers (first_name, last_name)
-- VALUES 
-- ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson');

ALTER TABLE customers ADD COLUMN id SERIAL PRIMARY KEY;

SELECT * FROM items;

SELECT * FROM items WHERE price > 80;

SELECT * FROM items WHERE price <= 300;

SELECT * FROM customers WHERE last_name = 'Smith';

SELECT * FROM customers WHERE last_name = 'Jones';

SELECT * FROM customers WHERE last_name != 'Scott';