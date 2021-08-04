# Basic Select Statement 
# 1
select first_name as "First Name", last_name as "Last Name" from employees;
# 2
 select distinct department_id from employees;
#3
select * from employees order by first_name desc;
#4
select first_name, last_name, salary, salary * 0.15 as "PF" from employees;
#5
 select employee_id, first_name, last_name, salary from employees order by salary;
#6
select sum(salary) from employees;
#7
select min(salary), max(salary) from employees;
#8
select avg(salary) from employees;
#9
 select count(first_name) from employees;
#10
 select upper(first_name) from employees;
#11
select substring(first_name, 1, 3) from employees;
#12
select concat(first_name, ' ', last_name) as fullname from employees;
#13
select concat(first_name, ' ', last_name) as fullname, length(concat(first_name, last_name))  from employees;
#14
select first_name  from employees where first_name ~ '[0-9]';
#15
 select * from employees limit 10;

#Restricting And Sorting
#1
select first_name, last_name, salary from employees where salary between 10000 and 15000;
#2
 select hire_date from employees where extract(year from hire_date) = '1987';
#3
 select first_name from employees where first_name ilike '%e%' and first_name ilike '%c%';
#4
select employees.last_name, jobs.job_title from employees inner join jobs on employees.job_id = jobs.job_id where jobs.job_title not in('Programmer','Shipping Clerk') and employees.salary not in (4500, 10000, 15000);
#5
select first_name, last_name from employees where length(last_name) = 6;
#6
 select last_name from employees where last_name like '__e%';
#7
select job_title from jobs;
select distinct job_title from employees inner join jobs on employees.job_id =jobs.job_id;
#8
select * from employees where upper(last_name) in ('Blake', 'JONES', 'SCOTT', 'KING', 'FORD');