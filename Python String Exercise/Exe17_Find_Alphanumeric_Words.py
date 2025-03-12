# Exercise 17: Find words with both alphabets and numbers
str1 = "Emma25 is Data scientist50 and AI Expert"
temp = str1.split()
l = []
for i in temp:
    if not i.isalpha():
        l.append(i)
print(l)
