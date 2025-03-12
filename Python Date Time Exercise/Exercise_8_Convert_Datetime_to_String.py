import datetime
from datetime import datetime

# Exercise 8: Convert the following datetime into a string
given_date = datetime(2020, 2, 25)
d = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(d)
