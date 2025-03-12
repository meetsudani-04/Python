# Exercise 15: Remove special symbols / punctuation from a string
str1 = "/*Jon is @developer & musician"
l = []
for i in str1:
    if i.isalpha():
        l.append(i)
print("".join(l))
