import datetime
from datetime import datetime

# Exercise 2: Convert string into a datetime object
date_string = "Feb 25 2020 4:20PM"
d = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(d)
