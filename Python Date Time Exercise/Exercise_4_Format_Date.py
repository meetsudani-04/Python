import datetime
from datetime import datetime

# Exercise 4: Print a date in the following format: Day_name  Day_number  Month_name  Year
given_date = datetime(2020, 2, 25)
d = given_date.strftime('%A %w %B %Y')
print(d)
