# Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
output = []
for i in list1:
    for j in list2:
        output.append(i+j)
print(output)