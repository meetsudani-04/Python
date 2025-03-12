# Exercise 7: String characters balance Test
s1 = "Ya"
s2 = "PYnative"
flag = True

for i in s1:
    if i in s2:
        continue
    else:
        flag = False
print(flag)
