create database hospital_management;
use hospital_management;



CREATE TABLE Patient (
    patientId INT PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    dateOfBirth DATE,
    gender VARCHAR(10),
    contactNumber VARCHAR(15),
    address VARCHAR(100)
);


CREATE TABLE Doctor (
    doctorId INT PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    specialization VARCHAR(100),
    contactNumber VARCHAR(15)
);


CREATE TABLE Appointment (
    appointmentId INT IDENTITY(1,1) PRIMARY KEY, 
    patientId INT,
    doctorId INT,
    appointmentDate DATE,
    description VARCHAR(255),
    FOREIGN KEY (patientId) REFERENCES Patient(patientId),
    FOREIGN KEY (doctorId) REFERENCES Doctor(doctorId)
);




INSERT INTO Patient (patientId, firstName, lastName, dateOfBirth, gender, contactNumber, address)
VALUES
(1, 'Arvind', 'Reddy', '1985-03-20', 'Male', '9876543210', 'Hyderabad, Telangana'),
(2, 'Priya', 'Kumar', '1990-07-15', 'Female', '9876543211', 'Chennai, Tamil Nadu'),
(3, 'Suresh', 'Nair', '1983-06-18', 'Male', '9876543212', 'Coimbatore, Tamil Nadu'),
(4, 'Lakshmi', 'Sundaram', '1992-10-30', 'Female', '9876543213', 'Bangalore, Karnataka'),
(5, 'Rajesh', 'Pillai', '1987-11-02', 'Male', '9876543214', 'Madurai, Tamil Nadu'),
(6, 'Meena', 'Iyer', '1986-05-25', 'Female', '9876543215', 'Chennai, Tamil Nadu'),
(7, 'Vijay', 'Subramani', '1991-12-22', 'Male', '9876543216', 'Hyderabad, Telangana'),
(8, 'Deepa', 'Menon', '1984-09-14', 'Female', '9876543217', 'Kochi, Kerala'),
(9, 'Hari', 'Mohan', '1993-01-17', 'Male', '9876543218', 'Bangalore, Karnataka'),
(10, 'Nisha', 'Ravi', '1989-08-11', 'Female', '9876543219', 'Chennai, Tamil Nadu');

INSERT INTO Doctor (doctorId, firstName, lastName, specialization, contactNumber)
VALUES
(1, 'Dr. Ravi', 'Kumar', 'Cardiology', '9876543220'),
(2, 'Dr. Priya', 'Nair', 'Neurology', '9876543221'),
(3, 'Dr. Siva', 'Reddy', 'Orthopedics', '9876543222'),
(4, 'Dr. Geetha', 'Subramani', 'Pediatrics', '9876543223'),
(5, 'Dr. Arun', 'Iyer', 'Dermatology', '9876543224'),
(6, 'Dr. Lakshmi', 'Ravi', 'General Medicine', '9876543225'),
(7, 'Dr. Kumar', 'Menon', 'Obstetrics & Gynecology', '9876543226'),
(8, 'Dr. Anjali', 'Sundaram', 'ENT', '9876543227'),
(9, 'Dr. Hari', 'Pillai', 'Gastroenterology', '9876543228'),
(10, 'Dr. Vijay', 'Mohan', 'Dentistry', '9876543229');


INSERT INTO Appointment (patientId, doctorId, appointmentDate, description)
VALUES
(1, 1, '2025-04-18', 'Cardiology consultation'),
(2, 2, '2025-04-19', 'Neurology consultation'),
(3, 3, '2025-04-20', 'Orthopedic checkup'),
(4, 4, '2025-04-21', 'Pediatric checkup'),
(5, 5, '2025-04-22', 'Skin checkup'),
(6, 6, '2025-04-23', 'General checkup'),
(7, 7, '2025-04-24', 'Obstetrics & Gynecology consultation'),
(8, 8, '2025-04-25', 'ENT checkup'),
(9, 9, '2025-04-26', 'Gastroenterology consultation'),
(10, 10, '2025-04-27', 'Dental consultation');



select * from Patient;
select * from Doctor;
select * from Appointment;