import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Exercise 9: Calculate the date 4 months from the current date
given_date = datetime(2020, 2, 25).date()
month = 4
d = given_date + relativedelta(months=+month)
print(d)
