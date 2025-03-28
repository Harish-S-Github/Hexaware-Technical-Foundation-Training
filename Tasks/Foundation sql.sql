create database foundation;
go

create table professor(
profid int,
profname varchar(50),
dept varchar(20),
subhandle varchar(80),
);

insert into professor(profid,profname,dept,subhandle)values(1,'ram','cse','database'),(2,'dham','aids','maths'),(3,'govind','it','english');

create table student(
studid int,
studname varchar(50),
dept varchar(20),
markoverallpercent int,
);

insert into student(studid,studname,dept,markoverallpercent)values(1,'abi','cse',88),(2,'ravi','cse',85),(3,'kishore','eee',70);

SELECT s.studid, s.studname, s.dept, s.markoverallpercent, 
       p.profid, p.profname, p.subhandle
FROM student s
INNER JOIN professor p ON s.dept = p.dept;



SELECT s.studid, s.studname, s.dept, s.markoverallpercent, 
       p.profid, p.profname, p.subhandle
FROM student s
LEFT JOIN professor p ON s.dept = p.dept;


SELECT s.studid, s.studname, s.dept, p.profid, p.profname, p.subhandle
FROM student s
RIGHT JOIN professor p ON s.dept = p.dept;


SELECT s.studid, s.studname, s.dept, p.profid, p.profname, p.subhandle
FROM student s
FULL JOIN professor p ON s.dept = p.dept;


SELECT s.studid, s.studname, s.dept AS student_dept, 
       p.profid, p.profname, p.subhandle, p.dept AS professor_dept
FROM student s
CROSS JOIN professor p;



select * from professor;
select * from student;


--Find the Average Student Marks Per Department

SELECT p.dept, p.profname, AVG(s.markoverallpercent) AS avg_marks
FROM student s
INNER JOIN professor p ON s.dept = p.dept
GROUP BY p.dept, p.profname;

--HAVING filters groups where the average mark is greater than 80.

SELECT p.dept, p.profname, AVG(s.markoverallpercent) AS avg_marks
FROM student s
INNER JOIN professor p ON s.dept = p.dept
GROUP BY p.dept, p.profname
HAVING AVG(s.markoverallpercent) > 80;

--Count Students Per Professor, Per Department, and Overall

SELECT p.dept, p.profname, COUNT(s.studid) AS student_count
FROM student s
LEFT JOIN professor p ON s.dept = p.dept
GROUP BY GROUPING SETS (
    (p.dept),  -- Students per professor
    (p.profname),              -- Students per department
    (p.dept, p.profname),
	()                 -- Total students
);




SELECT studid, studname, dept, 
       (SELECT AVG(markoverallpercent) FROM student WHERE dept = s.dept) AS avg_marks
FROM student s;


SELECT studname, markoverallpercent 
FROM student
WHERE markoverallpercent = (SELECT MAX(markoverallpercent) FROM student);

SELECT studid, studname, dept, markoverallpercent
FROM student s1
WHERE markoverallpercent = (
    SELECT MAX(markoverallpercent) 
    FROM student s2 
    WHERE s1.dept = s2.dept
);
