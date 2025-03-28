--Write a query to list all system databases available in MS SQL Server.
select * from sys.databases;

--Write a query to retrieve the physical file locations (MDF & LDF) of a database named "CompanyDB".
create database companydb;
use companydb
select name,physical_name,type_desc
from sys.master_files where database_id=db_id('companydb');

-- Write a query to create a database "HRDB" with the following specifications:
create database hrdb;
use hrdb

-- Rename "HRDB" to "EmployeeDB" using SQL commands.
alter database hrdb modify name= EmployeeDB;

--Drop the database "EmployeeDB" from the system.
drop database EmployeeDB;

--Write a query to display all supported data types in MS SQL Server.
select name from sys.types;

--Create a table "Employees" with the following fields:
create table employee(
EmpID int Primary Key,

EmpName varchar(100) Not Null,

JoinDate Date Not Null,

Salary Decimal(10,2)
);

--Add a new column "Department" (VARCHAR(50)) to the "Employees" table.
alter table employee add Department varchar(50);

--Rename the table "Employees" to "Staff".
exec sp_rename 'employee','staff';

--Drop the table "Staff" from the database.
drop table staff;
