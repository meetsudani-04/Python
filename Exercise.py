# # Exercise 1: Calculate the multiplication and sum of two numbers
# def calulate(num1,num2):
#     return num1 * num2
# total = calulate(10,5)
# print(total)

# # Exercise 2: Print the Sum of a Current Number and a Previous number
# first_num = 0
# for i in range(1,11):
#     sum = first_num + i 
#     print(f"{first_num} + {i} = {sum}") 
#     first_num = i

# # Exercise 3: Print characters present at an even index number
# even = []
# obb = []
# for i in range(1,10):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         obb.append(i)
# print(even)
# print(obb)

# word = input("Enter String:")
# size = len(word)
# for i in range(size):
#     if i % 2 == 0:
#         print(f"even: {word[i]}")

# # Exercise 4: Remove first n characters from a string
# word = input("Enter String:")
# n = int(input("Enter n Number:"))
# print(n)
# for i in word:
#     a = word[n:]
# print(a)

# # Exercise 5: Check if the first and last numbers of a list are the same
# x = [10, 20, 30, 40, 10]
# def same(x):
#     first_index = x[0]
#     last_index = x[-1]

#     if first_index == last_index :
#         return True
#     else:
#         return False 
    
# x = [10, 20, 30, 40, 40]
# print(same(x))

# # Exercise 6: Display numbers divisible by 5
# x = [10, 20, 33, 46, 55]
# divisible = int(input("Value:"))
# for i in x:
#     if i % divisible == 0:
#         print(i)

# # Exercise 7: Find the number of occurrences of a substring in a string
# str_x = "Emma is good developer. Emma is a writer"
# word = input("Enter String:")
# print(str_x.count(word))

# # Exercise 8: Print the following pattern
# # 1 
# # 2 2 
# # 3 3 3 
# # 4 4 4 4 
# # 5 5 5 5 5
# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# # Exercise 9: Check Palindrome Number
# num = 121
# revers = int(str(num)[::-1])
# print(revers)
# if num == revers:
#     print("True")
# else:
#     print("False")

# # Exercise 10: Merge two lists using the following condition
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# marge = list1 + list2
# result = []
# for i in list1:
#     if i % 2 != 0:
#         result.append(i)
# for i in list2:
#     if i % 2 == 0:
#         result.append(i)
# print(result)

# # Exercise 11: Get each digit from a number in the reverse order.
# num = 7536
# print(f"{num} revers: {str(num)[::-1]}")

# # Exercise 12: Calculate income tax
# income = 45000
# tax = 0

# if income <= 10000:
#     tax = 0
# elif income <= 20000:
#     x = income - 10000
#     tax = x * 10 / 100
# else:
#     tax = 0
#     tax = 10000 * 10 / 100
#     tax += (income-20000) * 20 / 100 # 20% 5000
# print(tax)

# # Exercise 13: Print multiplication table from 1 to 10
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j , end=" ")
#     print()

# # Exercise 14: Print a downward half-pyramid pattern of stars
# # * * * * *  
# # * * * *  
# # * * *  
# # * *  
# # *

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# # Exercise 15: Get an int value of base raises to the power of exponent
# num = 2
# power_num = 5
# total = num ** power_num
# print(total)

# # Exercise 1: Reverse a list in Python
# list1 = [100, 200, 300, 400, 500]
# list1.sort(reverse=True)
# print(list1)

# # Exercise 2: Concatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3 = []
# for i,j in zip(list1,list2):
#     list3.append(i+j)
# print(list3)

# # Exercise 3: Turn every item of a list into its square
# numbers = [1, 2, 3, 4, 5, 6, 7]
# output = []
# for i in numbers:
#     output.append(i**2)
#     # i **= 2
# print(output)

# Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# output = []
# for i in list1:
#     for j in list2:
#         output.append(i+j)
# print(output)

# # Exercise 5: Iterate both lists simultaneously
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for i,j in zip(list1,list2[::-1]):
#     print(i,j)

# # Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# output = []
# x = list(filter(None,list1))
# print(x)

# # Exercise 7: Add new item to list after a specified item
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(70)
# print(list1)

# Exercise 8: Extend nested list by adding the sublist
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print(list1)

# # Exercise 9: Replace list’s item with new value if found
# list1 = [5, 10, 15, 20, 25, 50, 20]
# x= list1.index(20)
# list1[x] = 200
# print(list1)

# # Exercise 10: Remove all occurrences of a specific item from a list.
list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
    list1.remove(20)
print(list1)

