#exercise 1:
# 1
select name from language;
# 2
select film.title, film.description, language.name from film inner join language on language.language_id = film.language_id;
select film.title, film.description, language.name from film left outer join language on language.language_id = film.language_id;
select film.title, film.description, language.name from film right outer join language on film.language_id = language.language_id;
select film.title, film.description, language.name from full outer join language on film.language_id = language.language_id;
select film.title, film.description, language.name from language full outer join language on language.language_id = film.language_id;
select film.title, film.description, language.name from language full outer join film on language.language_id = film.language_id offset 1000;
#3
insert into new_film (name) values ('Shrek'),('Forest Gump'), ('Lion King');
#4
create table customer_review (review_id serial primary key not null,film_id smallint references new_film(id) on delete cascade,language_id smallint references language(language_id) on delete cascade, title varchar(20) not null, score smallint not null, check (score between 1 and 10), review_text text not null, last_update date not null);
#5
insert into customer_review (film_id, language_id, title, score, review_text, last_update) values (3, 1, 'lion king review', 8, 'gooood','2021/08/03');
insert into customer_review (film_id, language_id, title, score, review_text, last_update) values (1, 1, 'Shrek review', 8, 'gooood','2021/08/03');
#6
dvdrental=# delete from new_film where name = 'Shrek';
DELETE 1
dvdrental=# select * from customer_review;
 review_id | film_id | language_id |      title       | score | review_text | last_update
-----------+---------+-------------+------------------+-------+-------------+-------------
         2 |       3 |           1 | lion king review |     8 | gooood      | 2021-08-03
# exercise 2
# 1
 update film set language_id = 3 where title like'A%';
# 2
Foreign-key constraints:
    "customer_address_id_fkey" FOREIGN KEY (address_id) REFERENCES address(address_id) ON UPDATE CASCADE ON DELETE RESTRICT
Referenced by:
    TABLE "payment" CONSTRAINT "payment_customer_id_fkey" FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON UPDATE CASCADE ON DELETE RESTRICT
    TABLE "rental" CONSTRAINT "rental_customer_id_fkey" FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON UPDATE CASCADE ON DELETE RESTRICT

when we insert into the costumer table it changes(updates) the payment and rental tables;
# 3
 drop table customer_review;
it's an easy step, the table does not affect other tables.
#4
select count(rental_date) from rental where return_date is null;
#5
 select payment.amount, rental.rental_id from payment inner join rental on rental.rental_id = payment.rental_id where rental.return_date is null order by amount desc limit 30;
#6
#1
select film.title, film.film_id, film_actor.film_id from film inner join film_actor on film.film_id = film_actor.actor_id where film.description like '%Sumo%' and film_actor.actor_id = 1;
#2
select film.title, film_category.film_id, film_category.category_id from film inner join film_category on film.film_id = film_category.film_id where film.length < 60 and film.rating = 'R' and film_category.category_id = 6;
#3
select film.title from film join inventory on film.film_id = inventory.film_id join rental on inventory.inventory_id = rental.inventory_id join customer on rental.customer_id = customer.customer_id where customer.first_name = 'Matthew' and rental.return_date between '2005/07/28' and '2005/08/01' and film.rental_rate > 4;
#4
select film.title from film join inventory on film.film_id = inventory.film_id join rental on inventory.inventory_id = rental.inventory_id join customer on rental.customer_id = customer.customer_id where film.description like '%Boat%'  and customer.first_name = 'Matthew' and customer.last_name = 'Mahan'  and film.replacement_cost > 18 ;