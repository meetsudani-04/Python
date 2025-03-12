# Exercise 5: Create an inner function to calculate the addition in the following way
def demo(a, b):
    def add(a, b):
        return a + b

    total = add(a, b)
    return total + 5

print(demo(5, 10))
