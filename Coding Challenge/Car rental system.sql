create database carrentalsystem;
use carrentalsystem;

create table vehicle (
    vehicleid int primary key identity(1,1),
    make varchar(30),
    model varchar(30),
    year int,
    dailyrate decimal(10,2),
    status bit,
    passengercapacity int,
    enginecapacity int
);

create table customer (
    customerid int primary key identity(1,1),
    firstname varchar(45),
    lastname varchar(45),
    email varchar(30) unique,
    phonenumber varchar(20)
);


create table lease (
    leaseid int primary key identity(1,1),
    vehicleid int foreign key references vehicle(vehicleid),
    customerid int foreign key references customer(customerid),
    startdate date,
    enddate date,
    leasetype varchar(10) check (leasetype in ('daily', 'monthly'))
);


create table payment (
    paymentid int primary key identity(1,1),
    leaseid int foreign key references lease(leaseid),
    paymentdate date,
    amount decimal(10,2)
);



insert into vehicle (make, model, year, dailyrate, status, passengercapacity, enginecapacity) values
('toyota', 'camry', 2022, 50.00, 1, 4, 1450),
('honda', 'civic', 2023, 45.00, 1, 7, 1500),
('ford', 'focus', 2022, 48.00, 0, 4, 1400),
('nissan', 'altima', 2023, 52.00, 1, 7, 1200),
('chevrolet', 'malibu', 2022, 47.00, 1, 4, 1800),
('hyundai', 'sonata', 2023, 49.00, 0, 7, 1400),
('bmw', '3 series', 2023, 60.00, 1, 7, 2499),
('mercedes', 'c-class', 2022, 58.00, 1, 8, 2599),
('audi', 'a4', 2022, 55.00, 0, 4, 2500),
('lexus', 'es', 2023, 54.00, 1, 4, 2500);



insert into customer (firstname, lastname, email, phonenumber) values
('john', 'doe', 'johndoe@example.com', '555-555-5555'),
('jane', 'smith', 'janesmith@example.com', '555-123-4567'),
('robert', 'johnson', 'robert@example.com', '555-789-1234'),
('sarah', 'brown', 'sarah@example.com', '555-456-7890'),
('david', 'lee', 'david@example.com', '555-987-6543'),
('laura', 'hall', 'laura@example.com', '555-234-5678'),
('michael', 'davis', 'michael@example.com', '555-876-5432'),
('emma', 'wilson', 'emma@example.com', '555-432-1098'),
('william', 'taylor', 'william@example.com', '555-321-6547'),
('olivia', 'adams', 'olivia@example.com', '555-765-4321');



insert into lease (vehicleid, customerid, startdate, enddate, leasetype) values
(1, 1, '2023-01-01', '2023-01-05', 'daily'),
(2, 2, '2023-02-15', '2023-02-28', 'monthly'),
(3, 3, '2023-03-10', '2023-03-15', 'daily'),
(4, 4, '2023-04-20', '2023-04-30', 'monthly'),
(5, 5, '2023-05-05', '2023-05-10', 'daily'),
(4, 3, '2023-06-15', '2023-06-30', 'monthly'),
(7, 7, '2023-07-01', '2023-07-10', 'daily'),
(8, 8, '2023-08-12', '2023-08-15', 'monthly'),
(3, 3, '2023-09-07', '2023-09-10', 'daily'),
(10, 10, '2023-10-10', '2023-10-31', 'monthly');



insert into payment (leaseid, paymentdate, amount) values
(1, '2023-01-03', 200.00),
(2, '2023-02-20', 1000.00),
(3, '2023-03-12', 75.00),
(4, '2023-04-25', 900.00),
(5, '2023-05-07', 60.00),
(6, '2023-06-18', 1200.00),
(7, '2023-07-03', 40.00),
(8, '2023-08-14', 1100.00),
(9, '2023-09-09', 80.00),
(10, '2023-10-25', 1500.00);


select * from vehicle;
select * from customer;
select * from lease;
select * from payment;


--1. Update the daily rate for a Mercedes car to 68.
update vehicle 
set dailyrate = 68 
where make = 'mercedes';


--2. Delete a specific customer and all associated leases and payments.
delete from customer where customerid = 3;


--3. Rename the "paymentDate" column in the Payment table to "transactionDate".
exec sp_rename 'payment.paymentdate', 'transactiondate', 'column';


--4. Find a specific customer by email.
select * from customer where email = 'michael@example.com';


--5. Get active leases for a specific customer.
select * from lease where customerid = 5 and enddate >='2023-05-10' ;


--6. Find all payments made by a customer with a specific phone number.
select payment.* 
from payment 
join lease on payment.leaseid = lease.leaseid 
join customer on lease.customerid = customer.customerid 
where customer.phonenumber = '555-876-5432';


--7. Calculate the average daily rate of all available cars.
select avg(dailyrate) as avg_dailyrate from vehicle where status = 1;


--8. Find the car with the highest daily rate.
select * from vehicle where dailyrate = (select max(dailyrate) from vehicle);


--9. Retrieve all cars leased by a specific customer.
select v.* 
from vehicle v
join lease l on v.vehicleid = l.vehicleid
where l.customerid = 2;


--10. Find the details of the most recent lease.
select top 1* from lease order by startdate desc;


--11. List all payments made in the year 2023.
select * from payment where year(transactiondate) = 2023;


--12. Retrieve customers who have not made any payments.
select c.*  
from customer c  
left join lease l on c.customerid = l.customerid  
left join payment p on l.leaseid = p.leaseid  
where p.paymentid is null;


--13. Retrieve Car Details and Their Total Payments.
select v.*, sum(p.amount) as total_payments
from vehicle v
join lease l on v.vehicleid = l.vehicleid
join payment p on l.leaseid = p.leaseid
group by v.vehicleid, v.make, v.model, v.year, v.dailyrate, v.status, v.passengercapacity, v.enginecapacity;


--14. Calculate Total Payments for Each Customer.
select c.customerid, c.firstname, c.lastname, sum(p.amount) as total_payments
from customer c
join lease l on c.customerid = l.customerid
join payment p on l.leaseid = p.leaseid
group by c.customerid, c.firstname, c.lastname;


--15. List Car Details for Each Lease.
select l.leaseid, v.* 
from lease l
join vehicle v on l.vehicleid = v.vehicleid;


--16. Retrieve Details of Active Leases with Customer and Car Information.
select l.*, c.firstname, c.lastname, v.make, v.model, v.year 
from lease l
join customer c on l.customerid = c.customerid
join vehicle v on l.vehicleid = v.vehicleid
where l.enddate >='2023-10-31';


--17. Find the Customer Who Has Spent the Most on Leases.
select top 1 c.customerid, c.firstname, c.lastname 
from customer c 
join lease l on c.customerid = l.customerid 
join payment p on l.leaseid = p.leaseid 
group by c.customerid, c.firstname, c.lastname 
order by sum(p.amount) desc;


--18. List All Cars with Their Current Lease Information.
select v.*, l.leaseid, l.startdate, l.enddate, l.leasetype, l.customerid
from vehicle v
left join lease l on v.vehicleid = l.vehicleid;

