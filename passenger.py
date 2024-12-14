from auth import Auth
from dbConnection import create_connection
from tabulate import tabulate  

connection = create_connection()

class Passenger:
    def __init__(self, user):
        self.user = user

    def menu(self):
        while True:
            print("\nPassenger Menu:")
            print("1. View Available Trips")
            print("2. Book a Trip")
            print("3. View My Booked Trips")
            print("4. Provide Feedback")
            print("5. Logout")

            choice = input("Enter your choice:z ")
            if choice == '1':
                self.view_trips()
            elif choice == '2':
                self.book_trip()
            elif choice == '3':
                self.view_booked_trips()
            elif choice == '4':
                self.provide_feedback()
            elif choice == '5':
                Auth.logout()
                break
            else:
                print("Invalid choice. Try again.")

    def view_trips(self):
        cursor = connection.cursor()
        cursor.execute(f"""
            SELECT t.Trip_ID, rt.Source, rt.Destination, t.Start_Time, t.End_Time, v.Vehicle_Type, t.Trip_Status
            FROM Trip t
            JOIN Route rt ON t.Route_ID = rt.Route_ID
            JOIN Vehicle v ON t.Vehicle_ID = v.Vehicle_ID
            WHERE t.Trip_Status = 'Scheduled'
        """)
        trips = cursor.fetchall()
        if trips:
            headers = ["Trip ID", "Source", "Destination", "Start Time", "End Time", "Vehicle Type", "Status"]
            print(tabulate(trips, headers=headers, tablefmt="pretty"))
        else:
            print("No scheduled trips available.")
        cursor.close()

    def book_trip(self):
        trip_id = self.validate_int("Enter Trip ID to book: ")
        seats = self.validate_int("Enter number of seats: ")

        cursor = connection.cursor()
        cursor.execute(f"SELECT v.Capacity FROM Vehicle v JOIN Trip t ON v.Vehicle_ID = t.Vehicle_ID WHERE t.Trip_ID = {trip_id}")
        vehicle_capacity = cursor.fetchone()
        total_fare = seats * 100  

        query = f"""
            INSERT INTO Booking (Trip_ID, Passenger_ID, Booking_Date, Seats_Booked, Total_Fare, Payment_Status)
            VALUES ({trip_id}, {self.user['User_ID']}, NOW(), {seats}, {total_fare}, 'Pending')
        """
        cursor.execute(query)
        connection.commit()
        cursor.close()
        print(f"Trip {trip_id} booked successfully with {seats} seats!")

    def view_booked_trips(self):
        cursor = connection.cursor()
        cursor.execute(f"""
            SELECT b.Booking_ID, t.Trip_ID, rt.Source, rt.Destination, b.Seats_Booked, b.Booking_Date, b.Payment_Status
            FROM Booking b
            JOIN Trip t ON b.Trip_ID = t.Trip_ID
            JOIN Route rt ON t.Route_ID = rt.Route_ID
            WHERE b.Passenger_ID = {self.user['User_ID']}
        """)
        booked_trips = cursor.fetchall()
        if booked_trips:
            headers = ["Booking ID", "Trip ID", "Source", "Destination", "Seats Booked", "Booking Date", "Payment Status"]
            print(tabulate(booked_trips, headers=headers, tablefmt="pretty"))
        else:
            print("No booked trips found.")
        cursor.close()

    def provide_feedback(self):
        trip_id = self.validate_int("Enter Trip ID for feedback: ")
        rating = self.validate_int("Rate the trip (1-5): ")
        comments = input("Enter your comments: ")

        query = f"""
            INSERT INTO Feedback (User_ID, Trip_ID, Feedback_Date, Rating, Comments)
            VALUES ({self.user['User_ID']}, {trip_id}, NOW(), {rating}, '{comments}')
        """
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        print(f"Feedback for Trip {trip_id} submitted successfully!")

    def validate_int(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
