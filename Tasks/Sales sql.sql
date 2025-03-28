--Write a query to list all system databases in SQL Server.
select * from sys.databases;


--Identify the physical database files (MDF, LDF) of a user-defined database named "SalesDB" using a SQL query.
 create database salesdb;
 USE SalesDB;
GO
SELECT name AS LogicalName, physical_name AS PhysicalFilePath, type_desc AS FileType
FROM sys.master_files
WHERE database_id = DB_ID('SalesDB');


--Create a user-defined database named "InventoryDB" with a primary data file of 5MB and a log file of 2MB.
create database inventorydb;
use inventorydb

--Rename the database "InventoryDB" to "StockDB" using a SQL query.
alter database inventorydb modify name=Stockdb;
use Stockdb

--Drop the database "StockDB" using a SQL query.
drop database Stockdb;

--Write a query to display all available data types in SQL Server
select name from sys.types;

--create a table "Products" with the following columns:
CREATE TABLE Products1 (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50) NOT NULL,
    Price DECIMAL(10,2),
    StockQuantity INT DEFAULT 0
);

--Modify the "Products" table to add a new column Category (VARCHAR(30)).
ALTER TABLE Products1 ADD Category VARCHAR(30);

--Rename the table "Products" to "Inventory"
exec sp_rename 'Products1','Inventory';

--Drop the "Inventory" table from the database.
drop table inventory;

--Identify and list the system databases available in SQL Server. Provide a brief description of each.
select * from sys.databases;

--Write a query to display all database files (MDF, LDF, NDF) for a specific database.
USE SalesDB1;  -- Replace with the actual database name
GO
SELECT name AS LogicalName, physical_name AS FilePath, type_desc AS FileType
FROM sys.master_files
WHERE database_id = DB_ID('salesdb1');


--Create a new user-defined database named SalesDB with a primary data file of 10MB and a log file of 5MB.
create database SalesDB
 ON primary
(  
    NAME = 'SalesDB_Data',  
    FILENAME = 'D:\ms\SalesDB_Data.mdf',  
    SIZE = 10MB,  
    MAXSIZE = 100MB,  
    FILEGROWTH = 10MB  
)  
LOG ON  
(  
    NAME = 'SalesDB_Log',  
    FILENAME = 'D:\ms\SalesDB_Data.ldf',  
    SIZE = 5MB,  
    MAXSIZE = 50MB,  
    FILEGROWTH = 5MB  
);


--Rename the database SalesDB to RetailDB using an SQL query.
ALTER DATABASE SalesDB MODIFY NAME = RetailDB;

--Drop the RetailDB database safely, ensuring that no active connections exist before deletion.
ALTER DATABASE RetailDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
DROP DATABASE RetailDB;

print 'hello';