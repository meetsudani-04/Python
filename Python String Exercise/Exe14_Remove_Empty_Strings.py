# Exercise 14: Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_list = []
for i in str_list:
    if i:
        new_list.append(i)
print(new_list)
