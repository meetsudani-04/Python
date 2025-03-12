# Exercise 5: Count all letters, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
letters = []
digits = []
symbols = []
for i in str1:
    if i.isalpha():
        letters.append(i)
    elif i.isdigit():
        digits.append(i)
    else:
        symbols.append(i)
print(len(letters))
print(len(digits))
print(len(symbols))
