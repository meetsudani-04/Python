# Exercise 3: Print characters present at an even index number
even = []
obb = []
for i in range(1,10):
    if i % 2 == 0:
        even.append(i)
    else:
        obb.append(i)
print(even)
print(obb)

word = input("Enter String:")
size = len(word)
for i in range(size):
    if i % 2 == 0:
        print(f"even: {word[i]}")