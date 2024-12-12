-- Active: 1734007905334@@127.0.0.1@3306@transport_ms
-- 1. Create User Table
CREATE TABLE User (
    User_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100) UNIQUE,
    Phone_Number VARCHAR(15),
    Address TEXT,
    Role ENUM('Driver', 'Passenger', 'Admin') NOT NULL,
    Password VARCHAR(100)
);

-- Insert Dummy Data into User Table
INSERT INTO User (Name, Email, Phone_Number, Address, Role, Password) VALUES
('Hakim Uddin', 'hakim@example.com', '01710000003', 'Dhaka, Bangladesh', 'Driver', 'admin123'),
('Jabbar Khan', 'jabbar@example.com', '01710000006', 'Chittagong, Bangladesh', 'Driver', 'driver123');
SELECT * from user;
-- 2. Create Passenger Table
CREATE TABLE Passenger (
    Passenger_ID INT PRIMARY KEY,
    Membership_Status ENUM('Regular', 'VIP') NOT NULL,
    Preferred_Payment_Method VARCHAR(50),
    FOREIGN KEY (Passenger_ID) REFERENCES User(User_ID)
);

-- Insert Dummy Data into Passenger Table
INSERT INTO Passenger (Passenger_ID, Membership_Status, Preferred_Payment_Method) VALUES
(1, 'Regular', 'Online'),
(3, 'VIP', 'Credit Card'),
(5, 'Regular', 'Cash'),
(4, 'VIP', 'Online'),
(2, 'Regular', 'Credit Card');
select * from passenger;

-- 3. Create Driver Table
CREATE TABLE Driver (
    Driver_ID INT PRIMARY KEY,
    License_Number VARCHAR(20),
    Rating FLOAT,
    Experience INT,
    Assigned_Vehicle INT,
    FOREIGN KEY (Driver_ID) REFERENCES User(User_ID)
);
select * from driver;

-- Insert Dummy Data into Driver Table
INSERT INTO Driver (Driver_ID, License_Number, Rating, Experience, Assigned_Vehicle) VALUES
(6, 'D12345', 4.5, 5, 1),
(7, 'D67890', 4.8, 8, 3);

-- 4. Create Admin Table
CREATE TABLE Admin (
    Admin_ID INT PRIMARY KEY,
    Access_Level ENUM('Super', 'Regional') NOT NULL,
    FOREIGN KEY (Admin_ID) REFERENCES User(User_ID)
);

-- Insert Dummy Data into Admin Table
INSERT INTO Admin (Admin_ID, Access_Level) VALUES
(1, 'Super');


-- 5. Create Vehicle Table
CREATE TABLE Vehicle (
    Vehicle_ID INT AUTO_INCREMENT PRIMARY KEY,
    Vehicle_Type ENUM('Bus', 'Taxi', 'Truck') NOT NULL,
    Registration_Number VARCHAR(15) UNIQUE,
    Capacity INT,
    Status ENUM('Available', 'In-Transit', 'Maintenance') NOT NULL
);

-- Insert Dummy Data into Vehicle Table
INSERT INTO Vehicle (Vehicle_Type, Registration_Number, Capacity, Status) VALUES
('Bus', 'DHK1234', 50, 'Available'),
('Bus', 'CTG5678', 40, 'In-Transit'),
('Bus', 'SYL9101', 35, 'Available'),
('Bus', 'RAJ1122', 45, 'Maintenance'),
('Bus', 'BAR3344', 40, 'Available');

-- 6. Create Route Table
CREATE TABLE Route (
    Route_ID INT AUTO_INCREMENT PRIMARY KEY,
    Source VARCHAR(100),
    Destination VARCHAR(100),
    Distance FLOAT,
    Estimated_Time TIME
);

-- Insert Dummy Data into Route Table
INSERT INTO Route (Source, Destination, Distance, Estimated_Time) VALUES
('Dhaka', 'Chittagong', 250.5, '05:30:00'),
('Sylhet', 'Dhaka', 240.0, '05:00:00'),
('Khulna', 'Rajshahi', 180.0, '03:30:00'),
('Barisal', 'Dhaka', 120.0, '02:45:00'),
('Rangpur', 'Dhaka', 300.0, '06:15:00');

-- 7. Create Trip Table
CREATE TABLE Trip (
    Trip_ID INT AUTO_INCREMENT PRIMARY KEY,
    Vehicle_ID INT,
    Route_ID INT,
    Driver_ID INT,
    Start_Time DATETIME,
    End_Time DATETIME,
    Trip_Status ENUM('Scheduled', 'Ongoing', 'Completed', 'Canceled') NOT NULL,
    FOREIGN KEY (Vehicle_ID) REFERENCES Vehicle(Vehicle_ID),
    FOREIGN KEY (Route_ID) REFERENCES Route(Route_ID),
    FOREIGN KEY (Driver_ID) REFERENCES Driver(Driver_ID)
);

-- Insert Dummy Data into Trip Table
INSERT INTO Trip (Vehicle_ID, Route_ID, Driver_ID, Start_Time, End_Time, Trip_Status) VALUES
(1, 1, 7, '2024-12-12 08:00:00', '2024-12-12 13:30:00', 'Scheduled'),
(2, 2, 6, '2024-12-12 09:00:00', '2024-12-12 14:00:00', 'Ongoing');
select * from trip;

-- 8. Create Booking Table
CREATE TABLE Booking (
    Booking_ID INT AUTO_INCREMENT PRIMARY KEY,
    Trip_ID INT,
    Passenger_ID INT,
    Booking_Date DATETIME,
    Seats_Booked INT,
    Total_Fare FLOAT,
    Payment_Status ENUM('Paid', 'Pending', 'Canceled') NOT NULL,
    FOREIGN KEY (Trip_ID) REFERENCES Trip(Trip_ID),
    FOREIGN KEY (Passenger_ID) REFERENCES Passenger(Passenger_ID)
);

-- Insert Dummy Data into Booking Table
INSERT INTO Booking (Trip_ID, Passenger_ID, Booking_Date, Seats_Booked, Total_Fare, Payment_Status) VALUES
(11, 7, '2024-12-10 10:00:00', 2, 500.0, 'Paid');


-- 9. Create Payment Table
CREATE TABLE Payment (
    Payment_ID INT AUTO_INCREMENT PRIMARY KEY,
    Booking_ID INT,
    Payment_Date DATETIME,
    Amount FLOAT,
    Payment_Method ENUM('Cash', 'Credit Card', 'Online') NOT NULL,
    FOREIGN KEY (Booking_ID) REFERENCES Booking(Booking_ID)
);

-- Insert Dummy Data into Payment Table
INSERT INTO Payment (Booking_ID, Payment_Date, Amount, Payment_Method) VALUES
(1, '2024-12-10 11:00:00', 500.0, 'Online'),
(2, '2024-12-11 16:00:00', 300.0, 'Credit Card'),
(3, '2024-12-09 09:00:00', 750.0, 'Cash'),
(5, '2024-12-13 10:00:00', 1000.0, 'Credit Card'),
(4, '2024-12-12 13:00:00', 400.0, 'Online');

-- 10. Create Feedback Table
CREATE TABLE Feedback (
    Feedback_ID INT AUTO_INCREMENT PRIMARY KEY,
    User_ID INT,
    Trip_ID INT,
    Feedback_Date DATETIME,
    Rating FLOAT,
    Comments TEXT,
    FOREIGN KEY (User_ID) REFERENCES User(User_ID),
    FOREIGN KEY (Trip_ID) REFERENCES Trip(Trip_ID)
);

-- Insert Dummy Data into Feedback Table
INSERT INTO Feedback (User_ID, Trip_ID, Feedback_Date, Rating, Comments) VALUES
(2, 1, '2024-12-12 14:00:00', 4.5, 'Very smooth trip. Highly recommended!');

