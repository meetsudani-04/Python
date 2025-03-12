# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
s1 = "America"
s2 = "Japan"

first = s1[0]+s2[0]
middle = s1[int(len(s1)/2)] + s2[int(len(s2)/2)]
last = s1[-1]+s2[-1]
print(first+middle+last)
