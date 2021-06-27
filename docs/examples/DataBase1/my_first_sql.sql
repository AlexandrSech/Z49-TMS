--select * from sqlite_master

-- это комментарий однострочный

/*
это
многострочный комментарий
 */

--будьте аккуратны в консоли
--если у вас будет несолько запросов - выпадет ошибка, если не ставить после каждого запроса ;

--например
select * from sqlite_master;

select master.name from sqlite_master as master;

-- для этого выделите именно тот запрос который вам нужен и выполните его

--создание таблицы
create table my_first_table
(
    id int,
    first_name varchar(255),
    last_name varchar(255)
);


--получение всех полей таблицы
select * from my_first_table;

--получение всех полей записей по конкретному условию
-- примечание: там где мы указываем таблицу пос ее имени мы можем указать as и
-- какой-нибудь короткий удобный псевдоним для удобной работы с его значениями
-- конкретно в этом запросе
select mft.*
from my_first_table as mft
where mft.last_name == 'Sech';


--вставка значений
insert into my_first_table values (1, 'Alex', 'Sech');


--вставим еще пару значений
insert into my_first_table values (2, 'Alex2', 'Sech');
insert into my_first_table values (3, 'Alex3', 'Sech');
insert into my_first_table values (4, 'Alex4', 'Sech2');


--изменение значений
update my_first_table
set last_name = 'SECH'
where last_name == 'Sech';


--удаление значений
delete from my_first_table
where id == 3;
