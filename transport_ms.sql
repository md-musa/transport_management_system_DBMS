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


-- 2. Create Passenger Table
CREATE TABLE Passenger (
    Passenger_ID INT PRIMARY KEY,
    Membership_Status ENUM('Regular', 'VIP') NOT NULL,
    Preferred_Payment_Method VARCHAR(50),
    FOREIGN KEY (Passenger_ID) REFERENCES User(User_ID)
);


-- 3. Create Driver Table
CREATE TABLE Driver (
    Driver_ID INT PRIMARY KEY,
    License_Number VARCHAR(20),
    Rating FLOAT,
    Experience INT,
    Assigned_Vehicle INT,
    FOREIGN KEY (Driver_ID) REFERENCES User(User_ID)
);

-- 4. Create Admin Table
CREATE TABLE Admin (
    Admin_ID INT PRIMARY KEY,
    Access_Level ENUM('Super', 'Regional') NOT NULL,
    FOREIGN KEY (Admin_ID) REFERENCES User(User_ID)
);


-- 5. Create Vehicle Table
CREATE TABLE Vehicle (
    Vehicle_ID INT AUTO_INCREMENT PRIMARY KEY,
    Vehicle_Type ENUM('Bus', 'Taxi', 'Truck') NOT NULL,
    Registration_Number VARCHAR(15) UNIQUE,
    Capacity INT,
    Status ENUM('Available', 'In-Transit', 'Maintenance') NOT NULL
);

-- 6. Create Route Table
CREATE TABLE Route (
    Route_ID INT AUTO_INCREMENT PRIMARY KEY,
    Source VARCHAR(100),
    Destination VARCHAR(100),
    Distance FLOAT,
    Estimated_Time TIME
);

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
ALTER TABLE Trip ADD COLUMN Fare DECIMAL(10, 2) NOT NULL DEFAULT 0.00;



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

-- 9. Create Payment Table
CREATE TABLE Payment (
    Payment_ID INT AUTO_INCREMENT PRIMARY KEY,
    Booking_ID INT,
    Payment_Date DATETIME,
    Amount FLOAT,
    Payment_Method ENUM('Cash', 'Credit Card', 'Online') NOT NULL,
    FOREIGN KEY (Booking_ID) REFERENCES Booking(Booking_ID)
);

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
