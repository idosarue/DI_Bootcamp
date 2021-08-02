# exercise 1
#1.1 
public=# select * from items order by price asc;
#1.2
select * from items where price >= 80 order by price asc;
#1.3
select first_name, last_name from customers order by first_name limit 3;
#1.4
select last_name from customers order by last_name desc;

#2
create table purchases (customer_id int, item_id int, foreign key (customer_id) references customers(id), foreign key (item_id) references items(item_id))
#2.1
it works because there isn't a constraint
#2.2
INSERT INTO purchases (customer_id, item_id) VALUES ((SELECT id FROM customers WHERE first_name = 'Scott'), (SELECT id FROM items WHERE item_name = 'Small desk'));
INSERT INTO purchases (customer_id, item_id) VALUES ((SELECT id FROM customers WHERE first_name = 'Greg'), (SELECT id FROM items WHERE item_name = 'Fan'));
 INSERT INTO purchases (customer_id, item_id) VALUES ((SELECT id FROM customers WHERE first_name = 'Sandra'), (SELECT id FROM items WHERE item_name = 'Large desk'));
 INSERT INTO purchases (customer_id, item_id) VALUES ((SELECT id FROM customers WHERE first_name = 'Melanie'), (SELECT id FROM items WHERE item_name = 'chair'));
 INSERT INTO purchases (customer_id, item_id) VALUES ((SELECT id FROM customers WHERE first_name = 'Trevor'), (SELECT id FROM items WHERE item_name = 'chair'));
#3
#3.1
 select * from purchases;, not useful we don't know who purchased what
#3.2
select customers.first_name, customers.last_name, purchases.customer_id, purchases.item_id FROM customers INNER JOIN purchases ON customers.id = purchases.customer_id;
#3.3
select customers.first_name, customers.last_name, purchases.customer_id, purchases.item_id FROM customers INNER JOIN purchases ON customers.id = purchases.customer_id where id = 4;
#3.4
select customers.first_name, customers.last_name, purchases.customer_id, purchases.item_id FROM customers INNER JOIN purchases ON customers.id = purchases.customer_id where item_id = 1 or item_id = 2;
# 4
insert into items(item_name, price) values ('Hard drive', 500);
INSERT INTO purchases (customer_id, item_id) VALUES ((SELECT id FROM customers WHERE first_name = 'Scott'), (SELECT id FROM items WHERE item_name = 'Hard drive'));
#5
#5.1
select customers.first_name FROM customers INNER JOIN purchases ON customers.id = purchases.customer_id;
#5.2
select customers.last_name FROM customers INNER JOIN purchases ON customers.id = purchases.customer_id;
#5.3
select item_name FROM items INNER JOIN purchases ON items.id = purchases.customer_id;

# exercise 2

select * from customer;

select first_name, last_name from customer as full_name;

select * from customer order by first_name desc;

select distinct create_date from customer;

-- Write a query to get the 
-- film ID, title, description, year of release and 
-- rental rate in ascending order according to their rental rate.

select film_id, title, description, release_year, rental_rate from film order by rental_rate;

-- Write a query to get the address, and the phone number of all 
-- customers living in the Texas district, these details
-- can be found in the “address” table.

select address, phone from address where district = 'Texas';

select * from film where film_id = 15 or film_id = 150;

select film_id, title, description, length, rental_rate from film where title = 'Forest Gump';
-- select title from film;
select film_id, title, description, length, rental_rate from film where title ilike 'fo%';

select title , rental_rate from film order by rental_rate limit 20;
select title , rental_rate from film order by rental_rate offset 10 rows fetch next 10 rows only;

-- Write a query which will join the data in the customer table and the
-- payment table. You want to get
-- the amount and the date of every payment made
-- by a customer, ordered by their id (from 1 to…).

select customer.customer_id, customer.first_name, payment.amount, payment.payment_date
from customer 
inner join payment on payment.customer_id = customer.customer_id order by customer_id;

-- select film.film_id, film.title, inventory.film_id
-- from film
-- inner join inventory on inventory.film_id = film.film_id;

select title, film_id from film where film_id not in (select film_id from inventory);


select city.city, city.country_id, country.country, country.country_id
from city
inner join country on country.country_id = city.country_id;

select customer.first_name, customer.last_name, payment.customer_id, payment.amount, payment.payment_date, payment.staff_id
from customer
inner join payment on payment.customer_id = customer.customer_id order by payment.staff_id;
