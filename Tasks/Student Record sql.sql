--
create database studentrecords;
use master;

--
alter database studentrecords modify name = universityrecords;
use master;

--
drop database universityrecords;

--
create database studenttable
use studenttable;
go


create table student(
 stuid int primary key,
 name varchar(50),
 age int,
 email varchar(100));

 select * from student;

 exec sp_rename 'student','universitytable';
 select * from universitytable;

 use  universitytable;

 INSERT INTO universitytable (stuid, name, age, email)
VALUES
(1, 'John Doe', 20, 'johndoe@example.com'),
(2, 'Jane Smith', 22, 'janesmith@example.com'),
(3, 'Michael Johnson', 21, 'michaelj@example.com'),
(4, 'Emily Davis', 23, 'emilydavis@example.com'),
(5, 'Daniel Lee', 24, 'daniellee@example.com');

update universitytable set email='harii13.gmail.com' where stuid=2;

DELETE FROM universitytable
WHERE stuid = 5;

SELECT name, email
FROM universitytable;

SELECT * FROM dbo.universitytable;


SELECT * FROM universitytable WHERE age > 18;

SELECT * FROM universitytable WHERE department = 'Computer Science';

SELECT * FROM universitytable WHERE age IN ('22', '24');

SELECT DISTINCT age FROM universitytable;
