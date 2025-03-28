create database tuesday;
use tuesday;

create table employee(
EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
Name VARCHAR(100)NOT NULL,
Age INT,
Department VARCHAR(50),
Salary DECIMAL(10,2)
);

insert into employee(Name,age,Department,Salary)
VALUES 
('Arun', 30, 'IT', 60000.00),
('Kumar', 28, 'HR', 55000.00),
('Meena', 35, 'Finance', 75000.00),
('Lakshmi', 26, 'Marketing', 50000.00),
('Ravi', 40, 'Operations', 80000.00);

select *  from employee;

update employee set Salary=salary*1.10 where Department='HR';

delete from employee where Department='IT';

insert into employee(Name,age,Department,Salary)values('Harish',22,'Developer',50000.00);

update employee set Department='Senior staff' where salary>50000.00;

delete from employee where age>60;

select name,salary from employee;

select * from employee 
where Department='hr' and salary>50000.00;

select * from employee order by salary desc;

select * from employee where age>30;

select * from employee where Department ='hr' 
OR department = 'Senior Staff';

SELECT * FROM employee  
WHERE Salary BETWEEN 30000 AND 60000;

SELECT * FROM employee  
WHERE Name LIKE 'A%';

SELECT * FROM employee  
WHERE Department <> 'IT';

SELECT * FROM employee  
WHERE Department IN ('Sales', 'Marketing');

SELECT DISTINCT Department FROM employee;

SELECT EmployeeID AS ID, Name, Salary AS "Monthly Income"  
FROM employee;

SELECT * FROM employee  
WHERE Name LIKE '%John%'  
AND Salary > 40000;
