# Exercise 4: Print multiplication table of a given number
num = int(input("Enter Number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num*i}")