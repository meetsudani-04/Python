# Exercise 8: Generate a Python list of all the even numbers between 4 to 30
even = []
for i in range(4,30):
    if i % 2 == 0:
        even.append(i)
print(even)
