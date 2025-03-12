# Exercise 4: Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"
lower = []
upper = []
for i in str1:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
print(lower)
print(upper)
sort_str = "".join(lower+upper)
print(sort_str)
