# Exercise 6: Generate a random Password which meets the following conditions
# Password length must be 10 characters long.
# It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

import random
import string

upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
digits = string.digits
symblos = string.punctuation

password = random.sample(upper_case,2)
password += random.sample(lower_case,6)
password += random.sample(digits,1)
password += random.sample(symblos,1)

random_pass = random.shuffle(password)
a = "".join(password)
print(a)

    