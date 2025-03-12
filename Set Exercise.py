# Exercise 1: Add a list of elements to a set
ample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

ample_set.update(sample_list)
print(ample_set)

# Exercise 2: Return a new set of identical items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

x = set1.intersection(set2)
print(x)

# Exercise 3: Get Only unique items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

x = set1.union(set2)
print(x)

# Exercise 4: Update the first set with items that don’t exist in the second set
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)

# Exercise 5: Remove items from the set at once
set1 = {10, 20, 30, 40, 50}
set1.difference_update([10,20,30])
print(set1)

# Exercise 6: Return a set of elements present in Set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
x = set1.symmetric_difference(set2)
print(x)

# Exercise 7: Check if two sets have any elements in common. If yes, display the common elements
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(f"Hello\n{set1.intersection(set2)}")

# Exercise 8: Update set1 by adding items from set2, except common items
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.symmetric_difference_update(set2)
print(set1)

# Exercise 9: Remove items from set1 that are not common to both set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)