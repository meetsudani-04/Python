# Exercise 9: Calculate the sum and average of the digits present in a string
str1 = "PYnative29@#8496"
digits = []

for i in str1:
    if i.isdigit():
        digits.append(int(i))

print(f"Sum:{sum(digits)} Avg:{sum(digits)/len(digits)}")
