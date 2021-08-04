create table orders (ID serial primary key, order_date date not null);

 create table items (ID serial primary key, order_id smallint, name varchar(50), qty smallint not null, price real not null, foreign key (order_id) references orders(ID));

create or replace function total_price (OI integer) returns integer as $total$ begin return(select sum(price * qty) from items where items.order_id = OI); end; $total$ language plpgsql;

create table users (user_name varchar(20) not null primary key, address varchar(20) not null);

insert into users (user_name, address) values ('lalabear', 'tel-aviv');

 alter table orders add column user_name varchar(20);

 alter table orders add foreign key (user_name) references users (user_name);

create or replace function total_price_user (UN varchar(20)) returns integer as $total$ declare user_id integer; value integer; begin user_id := (select id from orders where orders.user_name = UN); value := (select sum(price * qty) from items where items.order_id = user_id); return value; end; $total$ language plpgsql;