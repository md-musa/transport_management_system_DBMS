from auth import Auth
from dbConnection import create_connection
from tabulate import tabulate  # Importing tabulate for formatted output

connection = create_connection()

class Admin:
    def __init__(self, user):
        self.user = user

    def menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. View All Users")
            print("2. Add Vehicle")
            print("3. View Feedback")
            print("4. View Transactions")
            print("5. View Vehicle List")
            print("6. View Trips")
            print("7. View Routes")
            print("8. Logout")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.view_users()
            elif choice == '2':
                self.add_vehicle()
            elif choice == '3':
                self.view_feedback()
            elif choice == '4':
                self.view_transactions()
            elif choice == '5':
                self.view_vehicles()
            elif choice == '6':
                self.view_trips()
            elif choice == '7':
                self.view_routes()
            elif choice == '8':
                Auth.logout()
                break
            else:
                print("Invalid choice. Try again.")

    def view_users(self):
        cursor = connection.cursor()
        cursor.execute("SELECT User_ID, Name, Email, Phone_Number, Role FROM User")  # Safer query
        users = cursor.fetchall()
        if users:
            headers = ["User ID", "Name", "Email", "Phone Number", "Role"]
            print(tabulate(users, headers=headers, tablefmt="pretty"))
        else:
            print("No users found.")
        cursor.close()

    def add_vehicle(self):
        vehicle_type = input("Enter Vehicle Type (Bus/Taxi/Truck): ")
        registration_number = input("Enter Registration Number: ")
        capacity = self.validate_int("Enter Capacity: ")
        status = 'Available'

        query = """INSERT INTO Vehicle (Vehicle_Type, Registration_Number, Capacity, Status) 
                   VALUES (%s, %s, %s, %s)"""
        cursor = connection.cursor()
        cursor.execute(query, (vehicle_type, registration_number, capacity, status))
        connection.commit()
        cursor.close()
        print("Vehicle added successfully!")

    def view_feedback(self):
        cursor = connection.cursor()
        cursor.execute("SELECT f.Feedback_ID, u.Name, t.Trip_ID, f.Rating, f.Comments, f.Feedback_Date "
                       "FROM Feedback f "
                       "JOIN User u ON f.User_ID = u.User_ID "
                       "JOIN Trip t ON f.Trip_ID = t.Trip_ID")
        feedbacks = cursor.fetchall()
        if feedbacks:
            headers = ["Feedback ID", "User Name", "Trip ID", "Rating", "Comments", "Date"]
            print(tabulate(feedbacks, headers=headers, tablefmt="pretty"))
        else:
            print("No feedback found.")
        cursor.close()

    def view_transactions(self):
        cursor = connection.cursor()
        cursor.execute("SELECT p.Payment_ID, b.Booking_ID, p.Amount, p.Payment_Method, p.Payment_Date, b.Payment_Status "
                       "FROM Payment p "
                       "JOIN Booking b ON p.Booking_ID = b.Booking_ID")
        transactions = cursor.fetchall()
        if transactions:
            headers = ["Payment ID", "Booking ID", "Amount", "Payment Method", "Payment Date", "Payment Status"]
            print(tabulate(transactions, headers=headers, tablefmt="pretty"))
        else:
            print("No transactions found.")
        cursor.close()

    def view_vehicles(self):
        cursor = connection.cursor()
        cursor.execute("SELECT Vehicle_ID, Vehicle_Type, Registration_Number, Capacity, Status FROM Vehicle")
        vehicles = cursor.fetchall()
        if vehicles:
            headers = ["Vehicle ID", "Vehicle Type", "Registration Number", "Capacity", "Status"]
            print(tabulate(vehicles, headers=headers, tablefmt="pretty"))
        else:
            print("No vehicles found.")
        cursor.close()

    def view_trips(self):
        cursor = connection.cursor()
        cursor.execute("""SELECT t.Trip_ID, rt.Source, rt.Destination, t.Start_Time, t.End_Time, v.Vehicle_Type, t.Trip_Status 
                          FROM Trip t 
                          JOIN Route rt ON t.Route_ID = rt.Route_ID 
                          JOIN Vehicle v ON t.Vehicle_ID = v.Vehicle_ID""")
        trips = cursor.fetchall()
        if trips:
            headers = ["Trip ID", "Source", "Destination", "Start Time", "End Time", "Vehicle Type", "Status"]
            print(tabulate(trips, headers=headers, tablefmt="pretty"))
        else:
            print("No trips found.")
        cursor.close()

    def view_routes(self):
        cursor = connection.cursor()
        cursor.execute("SELECT Route_ID, Source, Destination, Distance, Estimated_Time FROM Route")
        routes = cursor.fetchall()
        if routes:
            headers = ["Route ID", "Source", "Destination", "Distance", "Estimated Time"]
            print(tabulate(routes, headers=headers, tablefmt="pretty"))
        else:
            print("No routes found.")
        cursor.close()

    def validate_int(self, message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
