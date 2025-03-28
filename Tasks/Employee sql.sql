create database employee;
use employee;

CREATE TABLE Employeestable (
    EmployeeID INT PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Salary DECIMAL(5,2),
    Department NVARCHAR(50)
);
INSERT INTO Employeestable (EmployeeID, FirstName, LastName, Salary, Department)  
VALUES  
(1, 'ram', 'kishore', 14000.00, 'IT'),  
(2, 'anoop', 'kumar', 15000.00, 'IT'),  
(3, 'kamalesh', 'yadhav', 13000.00, 'AI'),  
(4, 'hariz', 'kumar', 19000.00, 'AI');  
SELECT 
    LastName + ' ' + FirstName AS FullName 
FROM Employees;

SELECT * FROM Employeestable;

insert into Employeestable (EmployeeID, FirstName, LastName, Salary, Department) values(5,'kishore','michawm',20000.00,'AI');
select*from Employeestable;
sp_help

