5,6
# # Exercise 1: Create a function in Python
# def demo(num1,num2):
#     return num1 + num2

# d = demo(10,10)
# print(d)

# # Exercise 2: Create a function with variable length of arguments
# def demo(*args):
#     for i in args:
#         print(i)
# demo(10,20,30)

# # Exercise 3: Return multiple values from a function
# def demo(num1,numb2):
#     print(num1*numb2)
# demo(5,2)

# # Exercise 4: Create a function with a default argument
# def demo(name,salary):
#     print(f"My Name in {name} and salary is {salary}")
# demo("Meet",1000)
 
# # Exercise 5: Create an inner function to calculate the addition in the following way
# def demo(a,b):
#     def add(a,b):
#         return a+b
    
#     total = add(a,b)
#     return total + 5

# demo(5,10)

# # Exercise 6: Create a recursive function
# def demo(num):
#     if num:
#         return num + demo(num-1)
#     else:
#         return 0 
# r = demo(10)
# print(r)

# # Exercise 7: Assign a different name to function and call it through the new name
def demo(name):
    print(name)

new_demo = demo
new_demo("Meet Sudani")

# # Exercise 8: Generate a Python list of all the even numbers between 4 to 30
even = []
for i in range(4,30):
    if i % 2 == 0:
        even.append(i)
print(even)

# # Exercise 9: Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]
print(max(x))