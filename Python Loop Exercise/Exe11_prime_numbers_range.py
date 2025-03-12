# Exercise 11: Print all prime numbers within a range
for num in range(25, 50):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)