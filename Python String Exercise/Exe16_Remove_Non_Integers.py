# Exercise 16: Removal all characters from a string except integers
str1 = 'I am 25 years and 10 months old'
l = []
for i in str1:
    if i.isdigit():
        l.append(i)
print("".join(l))
