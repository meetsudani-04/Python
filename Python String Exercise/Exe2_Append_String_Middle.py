# Exercise 2: Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"
c = int(len(s1)/2)
x = s1[:c:]
x += s2
print(x+s1[c:])
