# Exercise 6: Display numbers divisible by 5
x = [10, 20, 33, 46, 55]
divisible = int(input("Value:"))
for i in x:
    if i % divisible == 0:
        print(i)