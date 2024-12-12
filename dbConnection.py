import mysql.connector
import sys
from mysql.connector import Error

# Database Connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',  
            user='root',        
            password='quvqcro',  
            database='transport_ms'
        )
        if connection.is_connected():
            print("Connected to MySQL Database")
        return connection
    except Error as e:
        print(f"Error: {e}")
        sys.exit()

  
  

# def close_connection():
#     if connection.is_connected():
#         connection.close()
#         print("Database connection")