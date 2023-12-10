import mysql.connector

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host = '34.82.166.112',
            port = '3306',
            user = 'root',
            password = '/IJ})"Hm#v.2N9xP',
            database = 'fall2023_cpsc408'
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySql: {e}")
        return None

# Create a record in the Students table

def create_student_record(conn,name, age):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO Students (name, age) VALUES (%s, %s)"
        cursor.execute(query, (name, age))
        conn.commit()
        print("Student record created successfully.")
    except mysql.connector.Error as e:
        print(f"Error creating a record: {e}")

# select and display record from the Students table

def select_and_display_students(conn):
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM Students"
        cursor.execute(query)
        for (student_id, name, age) in cursor:
            print(f"ID: {student_id}, Name: {name}, Age: {age}")
    except mysql.connector.Error as e:
        print(f"Error fetching records: {e}")

def main():
    conn = connect_to_database()
    if conn:
        create_student_record(conn, 'John Doe', 20)
        select_and_display_students(conn)
        conn.close()

if __name__ == '__main__':
    main()