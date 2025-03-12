# Exercise 9: Check Palindrome Number
num = 121
revers = int(str(num)[::-1])
print(revers)
if num == revers:
    print("True")
else:
    print("False")