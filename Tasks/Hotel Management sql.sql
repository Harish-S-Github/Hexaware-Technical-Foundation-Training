create database hotel_management;
use hotel_management;

create table hotels (
    hotelid int primary key,
    name varchar(255),
    location varchar(255),
    rating decimal(2,1)
);

create table rooms (
    roomid int primary key,
    hotelid int,
    roomnumber varchar(50),
    roomtype varchar(50),
    pricepernight decimal(10,2),
    available bit,
    foreign key (hotelid) references hotels(hotelid)
);

create table guests (
    guestid int primary key,
    fullname varchar(255),
    email varchar(255) unique,
    phonenumber varchar(20) unique,
    checkindate datetime,
    checkoutdate datetime
);

create table bookings (
    bookingid int primary key,
    guestid int,
    roomid int,
    bookingdate datetime,
    totalamount decimal(10,2),
    status varchar(50),
    foreign key (guestid) references guests(guestid),
    foreign key (roomid) references rooms(roomid)
);

create table payments (
    paymentid int primary key,
    bookingid int,
    amountpaid decimal(10,2),
    paymentdate datetime,
    paymentmethod varchar(50),
    foreign key (bookingid) references bookings(bookingid)
);

create table events (
    eventid int primary key,
    hotelid int,
    eventname varchar(255),
    eventdate datetime,
    venue varchar(255),
    foreign key (hotelid) references hotels(hotelid)
);

create table eventparticipants (
    participantid int primary key,
    participantname varchar(255),
    participanttype varchar(50),
    eventid int,
    foreign key (eventid) references events(eventid)
);



insert into hotels (hotelid, name, location, rating) values
(1, 'chennai grand', 'chennai', 4.5),
(2, 'madurai residency', 'madurai', 4.2),
(3, 'coimbatore inn', 'coimbatore', 4.7),
(4, 'trichy palace', 'trichy', 4.3),
(5, 'salem stay', 'salem', 4.1),
(6, 'vellore towers', 'vellore', 4.6);


insert into rooms (roomid, hotelid, roomnumber, roomtype, pricepernight, available) values
(1, 1, '101', 'single', 1500.00, 1),
(2, 1, '102', 'double', 2500.00, 1),
(3, 2, '201', 'suite', 4000.00, 0),
(4, 3, '301', 'single', 1800.00, 1),
(5, 4, '401', 'double', 2700.00, 1),
(6, 5, '501', 'suite', 5000.00, 0),


insert into guests (guestid, fullname, email, phonenumber, checkindate, checkoutdate) values
(1, 'arun', 'arun@gmail.com', '9876543210', '2025-03-20 14:00:00', '2025-03-22 12:00:00'),
(2, 'bala', 'bala@gmail.com', '9865321470', '2025-03-21 15:30:00', '2025-03-23 11:00:00'),
(3, 'chitra', 'chitra@gmail.com', '9954123678', '2025-03-22 13:00:00', '2025-03-24 10:00:00'),
(4, 'devi', 'devi@gmail.com', '9786542315', '2025-03-23 12:30:00', '2025-03-25 09:00:00'),
(5, 'elango', 'elango@gmail.com', '9674125896', '2025-03-24 16:00:00', '2025-03-26 12:00:00'),
(6, 'farooq', 'farooq@gmail.com', '9965478213', '2025-03-25 11:45:00', '2025-03-27 08:00:00');


insert into bookings (bookingid, guestid, roomid, bookingdate, totalamount, status) values
(1, 1, 1, '2025-03-18 10:00:00', 3000.00, 'confirmed'),
(2, 2, 2, '2025-03-19 12:30:00', 5000.00, 'checked out'),
(3, 3, 3, '2025-03-20 14:15:00', 8000.00, 'cancelled'),
(4, 4, 4, '2025-03-21 16:00:00', 3600.00, 'confirmed'),
(5, 5, 5, '2025-03-22 09:30:00', 5400.00, 'confirmed'),
(6, 6, 6, '2025-03-23 11:00:00', 10000.00, 'checked out');


insert into payments (paymentid, bookingid, amountpaid, paymentdate, paymentmethod) values
(1, 1, 3000.00, '2025-03-18 12:00:00', 'credit card'),
(2, 2, 5000.00, '2025-03-19 13:00:00', 'cash'),
(3, 3, 8000.00, '2025-03-20 15:00:00', 'upi'),
(4, 4, 3600.00, '2025-03-21 17:00:00', 'debit card'),
(5, 5, 5400.00, '2025-03-22 10:00:00', 'credit card'),
(6, 6, 10000.00, '2025-03-23 12:00:00', 'net banking');


insert into events (eventid, hotelid, eventname, eventdate, venue) values
(1, 1, 'marriage', '2025-04-10 18:00:00', 'banquet hall'),
(2, 2, 'conference', '2025-04-12 10:00:00', 'conference hall'),
(3, 3, 'music night', '2025-04-15 19:00:00', 'open ground'),
(4, 4, 'meeting', '2025-04-18 09:00:00', 'meeting room'),
(5, 5, 'birthday', '2025-04-20 17:00:00', 'ballroom'),
(6, 6, 'fundraiser', '2025-04-25 20:00:00', 'banquet hall');


insert into eventparticipants (participantid, participantname, participanttype, eventid) values
(1, 'gopal', 'guest', 1),
(2, 'hari', 'guest', 2),
(3, 'ilango', 'guest', 3),
(4, 'jagan', 'guest', 4),
(5, 'kumar', 'guest', 5),
(6, 'lakshmi', 'guest', 6);

select * from rooms
where available=1;


create procedure get_event_participants
    @eventid int
as
begin
    select participantname 
    from eventparticipants 
    where eventid = @eventid;
end;

exec get_event_participants @eventid = 1;

create procedure update_hotel_info
    @hotelid int,
    @new_name varchar(255),
    @new_location varchar(255)
as
begin
    update hotels
    set name = @new_name, location = @new_location
    where hotelid = @hotelid;
end;
exec update_hotel_info @hotelid = 1, @new_name = 'chennai royal', @new_location = 'chennai central';

select * from rooms;

select h.hotelid, h.name, sum(b.totalamount) as total_revenue
from hotels h, rooms r, bookings b
where h.hotelid = r.hotelid and r.roomid = b.roomid and b.status = 'confirmed'
group by h.hotelid, h.name;


select * from rooms  
where roomid not in (select roomid from bookings);

select 
    format(paymentdate, 'yyyy-MM') as year_month, 
    sum(amountpaid) as total_payments
from payments
group by format(paymentdate, 'yyyy-MM')
order by year_month;


select distinct roomtype 
from rooms 
where pricepernight between 50 and 150 or pricepernight > 300;

--11
select r.roomid, r.roomnumber, r.roomtype, g.fullname 
from rooms r 
join bookings b on r.roomid = b.roomid 
join guests g on b.guestid = g.guestid 
where b.status = 'confirmed';


create procedure get_total_participants
    @cityname varchar(255)
as
begin
    select count(ep.participantid) as total_participants
    from eventparticipants ep
    join events e on ep.eventid = e.eventid
    join hotels h on e.hotelid = h.hotelid
    where h.location = @cityname;
end;
exec get_total_participants @cityname = 'chennai';

select distinct roomtype  
from rooms  
where hotelid = 1;

select * from guests  
where guestid not in (select guestid from bookings);

select r.roomnumber, r.roomtype, g.fullname  
from bookings b  
join rooms r on b.roomid = r.roomid  
join guests g on b.guestid = g.guestid;

select h.hotelid, h.name, count(r.roomid) as available_rooms  
from hotels h  
join rooms r on h.hotelid = r.hotelid  
where r.available = 1  
group by h.hotelid, h.name;

select r1.roomid as room1, r2.roomid as room2, r1.hotelid, r1.roomtype  
from rooms r1  
join rooms r2 on r1.hotelid = r2.hotelid and r1.roomtype = r2.roomtype and r1.roomid < r2.roomid;

select h.name as hotel_name, e.eventname  
from hotels h  
cross join events e;

select top 1 h.hotelid, h.name, count(b.bookingid) as total_bookings  
from hotels h  
join rooms r on h.hotelid = r.hotelid  
join bookings b on r.roomid = b.roomid  
group by h.hotelid, h.name  
order by total_bookings desc;
