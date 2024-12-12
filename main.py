from admin import Admin
from driver import Driver
from passenger import Passenger
from auth import Auth

if __name__ == "__main__":
    try:
        while True:
            print("\n----Welcome to the Transport Management System-------")
            print("1. Login")
            print("2. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                try:
                    user = Auth.login()  
                    if user:
                        if user['Role'] == 'Admin':
                            admin = Admin(user)
                            admin.menu()
                        elif user['Role'] == 'Driver':
                            driver = Driver(user)
                            driver.menu()
                        elif user['Role'] == 'Passenger':
                            passenger = Passenger(user)
                            passenger.menu()
                        else:
                            print("Invalid user role. Please try again.")
                except Exception as e:
                    print(f"An error occurred during login or while handling the user session: {e}")

            elif choice == '2':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
