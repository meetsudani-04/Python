# Exercise 12: Display Fibonacci series up to 10 terms
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b