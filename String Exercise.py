6,7
# Exercise 1A: Create a string made of the first, middle and last character
# str1 = "James"
# print(str1[0]) # first
# lenth = int(len(str1))
# a = int(lenth/2)
# print(str1[2]) # middle
# print(str1[-1]) # last

# Exercise 1B: Create a string made of the middle three characters
# str1 = "JhonDipPeta"
# mi = int(len(str1) / 2)
# print(mi)
# output = str1[5]
# print(output)

# # Exercise 2: Append new string in the middle of a given string
# s1 = "Ault"
# s2 = "Kelly"
# c = int(len(s1)/2)
# x = s1[:c:]
# x += s2
# print(x+s1[c:])

# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
# s1 = "America"
# s2 = "Japan"

# first = s1[0]+s2[0]
# middle = s1[int(len(s1)/2)] + s2[int(len(s2)/2)]
# last = s1[-1]+s2[-1]
# print(first+middle+last)

# Exercise 4: Arrange string characters such that lowercase letters should come first
# str1 = "PyNaTive"
# lower = []
# upper = []
# for i in str1:
#     if i.islower():
#         lower.append(i)
#     else:
#         upper.append(i)
# print(lower)
# print(upper)
# sort_str = "".join(lower+upper)
# print(sort_str)

# Exercise 5: Count all letters, digits, and special symbols from a given string
# str1 = "P@#yn26at^&i5ve"
# letters = []
# digits = []
# symbols = []
# for i in str1:
#     if i.isalpha():
#         letters.append(i)
#     elif i.isdigit():
#         digits.append(i)
#     else:
#         symbols.append(i)
# print(len(letters))
# print(len(digits))
# print(len(symbols))

# Exercise 6: Create a mixed String using the following rules
# s1 = "Abc"
# s2 = "Xyz"


# Exercise 7: String characters balance Test
# s1 = "Ya"
# s2 = "PYnative"
# flag = True

# for i in s1:
#     if i in s2:
#         continue
#     else:
#         flag = False
# print(flag)

# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# str1 = "Welcome to USA. usa awesome, isn't it?"
# value = "USA"
# count = str1.lower().count(value.lower())
# print(count)

# Exercise 9: Calculate the sum and average of the digits present in a string
# str1 = "PYnative29@#8496"
# digits = []

# for i in str1:
#     if i.isdigit():
#         digits.append(int(i))


# print(f"Sum:{sum(digits)} Avg:{sum(digits)/len(digits)}")

# # Exercise 10: Write a program to count occurrences of all characters within a string
# str1 = "Apple"
# di = dict()
# for i in str1:
#     count = str1.count(i)   
#     di[i] = count
# print(di)

# # Exercise 11: Reverse a given string
# str1 = "PYnative"
# print(str1[::-1])

# # Exercise 12: Find the last position of a given substring
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# print(str1.rfind("Emma"))

# # Exercise 13: Split a string on hyphens
# str1 = "Emma-is-a-data-scientist"
# output = str1.split("-")
# for i in output:
#     print(i)

# Exercise 14: Remove empty strings from a list of strings
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# new_list = []
# for i in str_list:
#     if i:
#         new_list.append(i)
# print(new_list)

# Exercise 15: Remove special symbols / punctuation from a string
str1 = "/*Jon is @developer & musician"
l = []
for i in str1:
    if i.isalpha():
        l.append(i)
print("".join(l))

# Exercise 16: Removal all characters from a string except integers
str1 = 'I am 25 years and 10 months old'
l = []
for i in str1:
    if i.isdigit():
        l.append(i)
print("".join(l))

# Exercise 17: Find words with both alphabets and numbers
str1 = "Emma25 is Data scientist50 and AI Expert"
temp = str1.split()
l = []
for i in temp:
    if not i.isalpha():
        l.append(i)
print(l)
    
# Exercise 18: Replace each special symbol with # in the following string
str1 = '/*Jon is @developer & musician!!'
new_str = str1.replace('/',"#")
print(new_str)
