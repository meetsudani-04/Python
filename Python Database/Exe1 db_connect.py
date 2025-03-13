# Exercise 1: Connect to your database server and print its version

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
cur.execute("SELECT version();")

# Fetch and print the result
print(cur.fetchone())

cur.close()
conn.close()