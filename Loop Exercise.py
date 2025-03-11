# 3,6 ,11, 14,15,16,17
# # Exercise 1: Print first 10 natural numbers using while loop
# for  i in range(1,11):
#     print(i)

# # Exercise 2: Print the following pattern
# # 1 
# # 1 2 
# # 1 2 3 
# # 1 2 3 4 
# # 1 2 3 4 5
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# # Exercise 3: Calculate sum of all numbers from 1 to a given number
# sum = 0
# num = int(input("Enter Number:"))
# for i in range(1,num+1):
#     sum = sum + i
# print(sum)

# # Exercise 4: Print multiplication table of a given number
# num = int(input("Enter Number:"))
# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")

# # Exercise 5: Display numbers from a list using a loop
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i == 180:
#         break
#     print(i)

# # Exercise 6: Count the total number of digits in a number
# n = 75869
# print(len(str(n)))

# # Exercise 7: Print the following pattern
# # 5 4 3 2 1 
# # 4 3 2 1 
# # 3 2 1 
# # 2 1 
# # 1
# for i in range(5,0,-1):
#     for j in range(i):
#         print(i, end=" ")
#     print()

# # Exercise 8: Print list in reverse order using a loop
# list = [10, 20, 30, 40, 50]
# reverse = []    
# for i in list[::-1]:
#     reverse.append(i)
# print(reverse)

# # Exercise 9: Display numbers from -10 to -1 using for loop
# for i in range(-10,0,1):
#     print(i)

# # Exercise 10: Display a message “Done” after the successful execution of the for loop
# for i in range(5):
#     print(i)
# else:
#     print("Done!")

# # Exercise 11: Print all prime numbers within a range
# for i in range(25,50):
#     if i % 2 != 0:
#         print(i)

# # Exercise 12: Display Fibonacci series up to 10 terms
# a = 0
# b = 1
# for i in range(11):
#     i+=1
#     print(a,end = " ")
#     a,b = b,i

# # Exercise 13: Find the factorial of a given number
# num = 5
# fa = 1
# for i in range(1,num+1):
#     fa *= i
# print(fa)

# # Exercise 14: Reverse a integer number
# num = "76542"
# str = str(num)
# print(str[::-1])

# # Exercise 15: Print elements from a given list present at odd index positions
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# even = []
# odd = []
# for i in range(my_list):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(even)
# print(odd)

# # Exercise 16: Calculate the cube of all numbers from 1 to a given number
# num = 6
# for i in range(6):
#     i**=i
#     print(i)

# # Exercise 17: Find the sum of the series up to n terms
# n = 5

# for i in range(n):
#     i+=i
#     print(i) 

# # Exercise 18: Print the following pattern
# # * 
# # * * 
# # * * * 
# # * * * * 
# # * * * * * 
# # * * * * 
# # * * * 
# # * * 
# # *
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()