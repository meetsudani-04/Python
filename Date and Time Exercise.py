import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta


# # Exercise 1: Print current date and time in Python
print(datetime.now())

# Exercise 2: Convert string into a datetime object
date_string = "Feb 25 2020 4:20PM"
d = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(d)

# Exercise 3: Subtract a week (7 days)  from a given date in Python
from datetime import datetime,timedelta
given_date = datetime(2020, 2, 25)
day = 7
d = given_date - timedelta(days=day)

# Exercise 4: Print a date in a the following format
# Day_name  Day_number  Month_name  Year
given_date = datetime(2020, 2, 25)
d = given_date.strftime('%A %w %B %Y')
print(d)

# Exercise 5: Find the day of the week of a given date
given_date = datetime(2020, 7, 26)
print(given_date.strftime('%A'))

# Exercise 6: Add a week (7 days) and 12 hours to a given date
given_date = datetime(2020, 3, 22, 10, 0, 0)
day = 7
d = given_date + timedelta(days=day,hours=12)
print(d)

# Exercise 8: Convert the following datetime into a string
given_date = datetime(2020, 2, 25)
d = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(d)

# Exercise 9: Calculate the date 4 months from the current date
given_date = datetime(2020, 2, 25).date()
month = 4
d = given_date + relativedelta(months =+ month)
print(d)

# Exercise 10: Calculate number of days between two given dates
# 2020-02-25
date_1 = datetime(2020, 2, 25)
# 2020-09-17
date_2 = datetime(2020, 9, 17)
d = date_2-date_1
print(d)