import getpass
from dbConnection import create_connection

connection = create_connection()

class Auth:
    @staticmethod
    def login():
        email = input("Enter Email: ")
        password = getpass.getpass("Enter Password: ")

        try:
            cursor = connection.cursor(dictionary=True)
            query = f"SELECT * FROM User WHERE Email = '{email}' AND Password = '{password}'"  
            cursor.execute(query)
            user = cursor.fetchone()

            if user:
                print(f"Welcome, {user['Name']}! Your role is {user['Role']}.")
                return user
            else:
                print("Invalid credentials. Please try again.")
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    @staticmethod
    def logout():
        print("You have been logged out.")

    @staticmethod
    def register_passenger():
        print("\nPassenger Registration")
        name = input("Enter Full Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        phone_number = input("Enter Phone Number: ")
        address = input("Enter Address: ")

        try:
            cursor = connection.cursor()
            query = f"""
                INSERT INTO User (Name, Email, Password, Phone_Number, Address, Role)
                VALUES ('{name}', '{email}', '{password}', '{phone_number}', '{address}', 'Passenger')
            """  
            cursor.execute(query)
            connection.commit()
            print("Passenger registered successfully!")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()  
