# Exercise 6: Create a recursive function
def demo(num):
    if num:
        return num + demo(num - 1)
    else:
        return 0

r = demo(10)
print(r)
