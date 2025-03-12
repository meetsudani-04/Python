import datetime
from datetime import datetime, timedelta

# Exercise 3: Subtract a week (7 days) from a given date in Python
given_date = datetime(2020, 2, 25)
day = 7
d = given_date - timedelta(days=day)
print(d)
