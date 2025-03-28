create database cartoon;
use cartoon;

create table organization (
    organizationid int primary key,
    organizationname varchar(255) not null
);

create table series (
    seriesid int primary key,
    seriesname varchar(255) not null,
    organizationid int,
    trp decimal(3,1),
    noofviews int,
    foreign key (organizationid) references organization(organizationid) on delete cascade
);

create table cartoons (
    cartoonid int primary key,
    cartoonname varchar(255) not null,
    seriesid int,
    foreign key (seriesid) references series(seriesid) on delete cascade
);

INSERT INTO organization (organizationid, organizationname) VALUES  
(1, 'Disney'),  
(2, 'Nickelodeon'),  
(3, 'Cartoon Network'),  
(4, 'Marvel Studios'),  
(5, 'Pixar Animation');

INSERT INTO series (seriesid, seriesname, organizationid, trp, noofviews) VALUES  
(101, 'Mickey Mouse Clubhouse', 1, 8.5, 5000000),  
(102, 'SpongeBob SquarePants', 2, 9.2, 7000000),  
(103, 'Tom and Jerry', 3, 9.5, 8500000),  
(104, 'Avengers Assemble', 4, 8.8, 6000000),  
(105, 'Toy Story Toons', 5, 7.9, 4000000);

INSERT INTO cartoons (cartoonid, cartoonname, seriesid) VALUES  
(1001, 'Mickey Mouse', 101),  
(1002, 'SpongeBob', 102),  
(1003, 'Jerry', 103),  
(1004, 'Iron Man', 104),  
(1005, 'Woody', 105);

--1) Filter the series on the basis of TRP (e.g., TRP greater than 9.0)
select * from series where trp > 9.0;

--2) Sort series name on the basis of TRP
select * from series order by trp desc;

--3) Filter out the most popular cartoon character
select c.cartoonname, s.seriesname, s.trp 
from cartoons c 
join series s on c.seriesid = s.seriesid
where s.trp = (select max(trp) from series);

--4) Most watched series (series with the highest number of views)
select * from series where noofviews = (select max(noofviews) from series);