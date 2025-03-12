# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
str1 = "Welcome to USA. usa awesome, isn't it?"
value = "USA"
count = str1.lower().count(value.lower())
print(count)
