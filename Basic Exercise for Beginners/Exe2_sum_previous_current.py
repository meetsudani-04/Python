# Exercise 2: Print the Sum of a Current Number and a Previous number
first_num = 0
for i in range(1,11):
    sum = first_num + i 
    print(f"{first_num} + {i} = {sum}") 
    first_num = i