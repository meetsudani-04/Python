# Exercise 5: Generate random String of length 5
import random
import string

letters = string.ascii_letters
for i in range(6):
    print(''.join(random.choice(letters)),end=" ")
