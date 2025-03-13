# Exercise 3: Get the list Of doctors as per the given specialty and salary

import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="new_demo_db",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def doctor():
    doctor_id = int(input("Enter Doctor ID:")) 
    experience = int(input("Enter Doctor experience:")) 

    cur.execute("select * from doctor where doctor_id = %s;",(doctor_id,))
    updated_record = cur.fetchone()
    print(f"Old experience: {updated_record}")

    cur.execute("update doctor set experience = %s where doctor_id = %s;",(experience,doctor_id))
    conn.commit()

    cur.execute("select * from doctor where doctor_id = %s;",(doctor_id,))
    updated_record = cur.fetchone()
    print(f"Update experience{updated_record}")

doctor_data = doctor()

cur.close()
conn.close()

