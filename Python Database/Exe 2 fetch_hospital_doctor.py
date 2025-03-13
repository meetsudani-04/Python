# Question 2: Fetch Hospital and Doctor Information using hospital Id and doctor Id

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

# Execute a query
def hospital():
    hospital_id = int(input("Enter Hospital ID: "))
    cur.execute("SELECT * from hospital where hospital_id = %s",(hospital_id,))
    return cur.fetchone()

def doctor():
    doctor_id = int(input("Enter Doctor ID:")) 
    cur.execute("SELECT * from doctor where doctor_id = %s",(doctor_id,))
    return cur.fetchone()

hospital_data = hospital()
print(hospital_data)

doctor_data = doctor()
print(doctor_data)

cur.close()
conn.close()