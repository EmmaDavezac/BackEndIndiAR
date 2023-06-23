#Import the required modules:
import mysql.connector
from mysql.connector import Error
#Connect to the MySQL database:
try:
    connection = mysql.connector.connect(
        host='your_host',
        database='your_database',
        user='your_username',
        password='your_password'
    )
    if connection.is_connected():
        print('Connected to MySQL database')
except Error as e:
    print(f'Error connecting to MySQL database: {e}')
#Create a new record (Create operation):
def create_record(connection):
    try:
        cursor = connection.cursor()
        sql_query = "INSERT INTO your_table (column1, column2, ...) VALUES (%s, %s, ...)"
        values = ('value1', 'value2', ...)
        cursor.execute(sql_query, values)
        connection.commit()
        print('Record created successfully')
    except Error as e:
        print(f'Error creating record: {e}')
#Retrieve records (Read operation):
def retrieve_records(connection):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT * FROM your_table"
        cursor.execute(sql_query)
        records = cursor.fetchall()
        for record in records:
            print(record)  # Do something with the retrieved data
    except Error as e:
        print(f'Error retrieving records: {e}')
#Update a record (Update operation):
def update_record(connection):
    try:
        cursor = connection.cursor()
        sql_query = "UPDATE your_table SET column1 = %s WHERE column2 = %s"
        values = ('new_value', 'condition_value')
        cursor.execute(sql_query, values)
        connection.commit()
        print('Record updated successfully')
    except Error as e:
        print(f'Error updating record: {e}')
#Delete a record (Delete operation):
def delete_record(connection):
    try:
        cursor = connection.cursor()
        sql_query = "DELETE FROM your_table WHERE column = %s"
        value = 'value_to_delete'
        cursor.execute(sql_query, (value,))
        connection.commit()
        print('Record deleted successfully')
    except Error as e:
        print(f'Error deleting record: {e}')
