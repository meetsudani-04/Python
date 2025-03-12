import datetime
from datetime import datetime, timedelta

# Exercise 6: Add a week (7 days) and 12 hours to a given date
given_date = datetime(2020, 3, 22, 10, 0, 0)
day = 7
d = given_date + timedelta(days=day, hours=12)
print(d)
