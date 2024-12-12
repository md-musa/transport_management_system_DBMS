from auth import Auth
from dbConnection import create_connection
from tabulate import tabulate  

connection = create_connection()

class Driver:
    def __init__(self, user):
        self.user = user

    def menu(self):
        while True:
            print("\nDriver Menu:")
            print("1. View Assigned Trips")
            print("2. Update Trip Status")
            print("3. Logout")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.view_trips()
            elif choice == '2':
                self.update_trip_status()
            elif choice == '3':
                Auth.logout()
                break
            else:
                print("Invalid choice. Try again.")


    def view_trips(self):
        cursor = connection.cursor()
        cursor.execute("SELECT t.Trip_ID, rt.Source, rt.Destination, t.Start_Time, t.End_Time, t.Trip_Status, v.Vehicle_Type "
                       "FROM Trip t "
                       "JOIN Route rt ON t.Route_ID = rt.Route_ID "
                       "JOIN Vehicle v ON t.Vehicle_ID = v.Vehicle_ID "
                       "WHERE t.Driver_ID = %s", (self.user['User_ID'],)) 
        trips = cursor.fetchall()
        if trips:
            headers = ["Trip ID", "Source", "Destination", "Start Time", "End Time", "Status", "Vehicle Type"]
            print(tabulate(trips, headers=headers, tablefmt="pretty"))
        else:
            print("No trips assigned.")
        cursor.close()


    def update_trip_status(self):
        trip_id = self.validate_int("Enter Trip ID to update: ")
        new_status = input("Enter new status (Scheduled/Ongoing/Completed/Canceled): ")

        query = """UPDATE Trip SET Trip_Status = %s WHERE Trip_ID = %s"""
        cursor = connection.cursor()
        cursor.execute(query, (new_status, trip_id))  
        connection.commit()
        cursor.close()
        print("Trip status updated successfully!")


    def validate_int(self, message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
