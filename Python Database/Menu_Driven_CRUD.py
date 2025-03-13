import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="new_demo_db",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

# Create a cursor
cur = conn.cursor()

# create table
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT
        )
    """)
    conn.commit()

# insert record
def insert_record():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    cur.execute("insert into students(name,age)values(%s, %s)RETURNING id;",(name,age))
    student_id = cur.fetchone()[0] 
    conn.commit()
    print(f"Insert Student with Id {student_id}")

# view record
def read_students():
    cur.execute("SELECT * FROM students;")
    rows = cur.fetchall()
    if not rows:
        print("No students found.")
    else:
        print("\nStudents Data:")
        for row in rows:
            print(row)

# update record
def update_students():
    student_id = input("Enter student ID : ")
    new_name = input("Enter New Name: ")
    new_age = input("Enter New Age: ")
    cur.execute("UPDATE students SET name = %s,age = %s WHERE id = %s;",(new_name,new_age,student_id))
    conn.commit()
    print(f"Update Student with Id {student_id}")

# delete record
def delete_students():
    student_id = input("Enter student ID to delete: ")
    cur.execute("Delete from students where id = %s",(student_id))
    conn.commit()
    print(f"Delete Student with Id {student_id}")


def main():
    while True:
        print("\nMenu:")
        print("1. Create Table")
        print("2. Insert Student")
        print("3. View Students")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice in ['1','2','3','4','5','6']:
            if choice == '1':
                create_table()
            elif choice == '2':
                insert_record()
            elif choice == '3':
                read_students()
            elif choice == '4':
                update_students()
            elif choice == '5':
                delete_students()
            elif choice == '6':
                print("Exiting program.")
                break
            else:
                print("Invild Coice")

main()
cur.close()
conn.close()
print("Database connection closed.")
