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
    salary = int(input("Enter Doctor ID:")) 
    cur.execute("SELECT * from doctor where salary < %s",(salary,))
    return cur.fetchall()

doctor_data = doctor()
for row in doctor_data:
    print(row)

cur.close()
conn.close()

