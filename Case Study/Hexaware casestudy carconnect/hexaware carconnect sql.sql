create database car;

use car;

CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(20),
    Address VARCHAR(255),
    Username VARCHAR(50),
    Password VARCHAR(100),
    RegistrationDate DATE
);

CREATE TABLE Vehicle (
    VehicleID INT PRIMARY KEY,
    Model VARCHAR(50),
    Make VARCHAR(50),
    Year INT,
    Color VARCHAR(30),
    RegistrationNumber VARCHAR(50),
    Availability BIT,
    DailyRate DECIMAL(10, 2)
);

CREATE TABLE Reservation (
    ReservationID INT PRIMARY KEY,
    CustomerID INT,
    VehicleID INT,
    StartDate DATE,
    EndDate DATE,
    TotalCost DECIMAL(10, 2),
    Status VARCHAR(20)
);

CREATE TABLE Admin (
    AdminID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(20),
    Username VARCHAR(50),
    Password VARCHAR(100),
    Role VARCHAR(50),
    JoinDate DATE
);


select * from Customer;
select * from Vehicle;
select * from Reservation;
select * from admins;



