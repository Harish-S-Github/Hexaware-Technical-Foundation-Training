-- Create the database
create database petcare;
go

use petcare;
go

-- Create Pets table
create table pets (
    petid int primary key identity(1,1),
    name varchar(100) not null,
    age int not null,
    breed varchar(100) not null,
    type varchar(50) not null,
    availableforadoption bit not null
);

-- Create Shelters table
create table shelters (
    shelterid int primary key identity(1,1),
    name varchar(100) not null,
    location varchar(255) not null
);

-- Create Donations table
create table donations (
    donationid int primary key identity(1,1),
    donorname varchar(100) not null,
    donationtype varchar(50) not null,  -- e.g., Money, Food, Supplies
    donationamount decimal(10,2) null,
    donationitem varchar(255) null,
    donationdate datetime not null default getdate()
);

-- Create AdoptionEvents table
create table adoptionevents (
    eventid int primary key identity(1,1),
    eventname varchar(100) not null,
    eventdate datetime not null,
    location varchar(255) not null
);

-- Create Participants table
create table participants (
    participantid int primary key identity(1,1),
    participantname varchar(100) not null,
    participanttype varchar(50) not null,  -- e.g., Volunteer, Adopter
    eventid int not null,
    foreign key (eventid) references adoptionevents(eventid) on delete cascade
);
insert into pets (name, age, breed, type, availableforadoption) values  
('mani', 2, 'rajapalayam', 'dog', 1),  
('kavi', 3, 'spitz', 'dog', 1),  
('selvi', 1, 'persian', 'cat', 1),  
('murugan', 5, 'siamese', 'cat', 0),  
('muthu', 4, 'golden retriever', 'dog', 1),  
('latha', 2, 'parrot', 'bird', 1);

insert into shelters (name, location) values  
('thangam pet home', 'chennai'),  
('suba animal care', 'madurai'),  
('arul pet shelter', 'coimbatore'),  
('siva pet rescue', 'trichy'),  
('kumar shelter', 'salem'),  
('bala stray care', 'vellore');

insert into donations (donorname, donationtype, donationamount, donationitem, donationdate) values  
('karunakaran', 'money', 5000, null, '2025-03-01'),  
('mangai', 'food', null, 'dog food', '2025-03-05'),  
('sundar', 'money', 2000, null, '2025-03-10'),  
('vasanthi', 'medicine', null, 'pet vaccines', '2025-03-12'),  
('aravind', 'money', 3000, null, '2025-03-15'),  
('lakshmi', 'blankets', null, 'pet blankets', '2025-03-18');

insert into adoptionevents (eventname, eventdate, location) values  
('puppy love fest', '2025-04-10', 'chennai'),  
('home for paws', '2025-04-12', 'madurai'),  
('furry friends fair', '2025-04-15', 'coimbatore'),  
('adopt a buddy', '2025-04-18', 'trichy'),  
('pawfect match', '2025-04-20', 'salem'),  
('forever home fest', '2025-04-22', 'vellore');

insert into participants (participantname, participanttype, eventid) values  
('rajan', 'guest', 1),  
('shiva', 'volunteer', 2),  
('priya', 'guest', 3),  
('sathya', 'sponsor', 4),  
('devi', 'volunteer', 5),  
('mohan', 'guest', 6);


select name, age, breed, type  
from pets  
where availableforadoption = 1;


select participantname, participanttype  
from participants  
where eventid = 1;

create procedure update_shelter  
    @shelterid int,  
    @newname varchar(100),  
    @newlocation varchar(255)  
as  
begin  
    update shelters  
    set name = @newname, location = @newlocation  
    where shelterid = @shelterid;  
end;
exec update_shelter 1, 'lakshan illam', 'Karur';

select s.name, sum(d.donationamount)  as totaldonation
from shelters s  
join donations d on s.shelterid = d.donationid 
group by s.name;


select name, age, breed, type  
from pets  
where availableforadoption=1;

select 
    year(donationdate) as year,  
    month(donationdate) as month,  
    sum(donationamount) as total_donations  
from donations  
group by year(donationdate), month(donationdate)  
order by year(donationdate), month(donationdate);

select distinct name,breed,age from pets where age between 1 and 3 or age>5;

select p.name as pet_name, p.breed, p.type, s.name as shelter_name, s.location  
from pets p  
join shelters s on p.petid = s.shelterid  
where p.availableforadoption = 1;

select e.location, count(p.participantid) as total_participants
from participants p
join adoptionevents e on p.eventid = e.eventid
where e.location = 'coimbatore'
group by e.location;

select distinct breed from pets
where age between 1 and 5;

select * from pets
where availableforadoption = 1;

select p.name as pet_name, pa.participantname as adopter_name
from pets p
join participants pa on p.petid = pa.participantid
where p.availableforadoption = 0;

select s.name as shelter_name, count(p.petid) as available_pets
from shelters s
join pets p on s.shelterid = p.petid
where p.availableforadoption = 1
group by s.name;

select p1.name as pet1, p2.name as pet2, p1.breed, s.name as shelter_name
from pets p1
join pets p2 on p1.breed = p2.breed and p1.petid < p2.petid
join shelters s on p1.petid = s.shelterid;

select s.name as shelter_name, e.eventname
from shelters s
cross join adoptionevents e;

select s.name as shelter_name, count(*) as total_adoptions
from shelters s
join pets p on s.shelterid = p.petid
where p.availableforadoption = 0
group by s.name
order by total_adoptions desc;

create trigger update_adoption_status
on participants
after insert
as
begin
    update pets
    set availableforadoption = 0
    where petid in (select participantid from inserted);
end;

alter table participants
add constraint unique_adoption unique (participantid);

