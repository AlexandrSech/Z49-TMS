create database homework15

use homework15 
drop table Products

create table Products(
id int primary key identity(1,1),
name varchar(30),
cost int,
summarity int,
comment varchar(max)
)



insert into Products(name, cost, summarity, comment) 
values (
'apple', 30, 2000, 'red and green apples'
)

insert into Products(name, cost, summarity, comment) 
values (
'orange', 50, 1500, 'oranges from Florida'
)

insert into Products(name, cost, summarity, comment) 
values (
'pear', 70, 2500, 'hanging pear can not be eaten'
)

insert into Products(name, cost, summarity, comment) 
values (
'watermelon', 300, 100, 'watermelon is berry'
)


select * from Products