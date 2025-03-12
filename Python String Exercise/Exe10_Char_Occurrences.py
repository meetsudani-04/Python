# Exercise 10: Write a program to count occurrences of all characters within a string
str1 = "Apple"
di = dict()
for i in str1:
    count = str1.count(i)   
    di[i] = count
print(di)
