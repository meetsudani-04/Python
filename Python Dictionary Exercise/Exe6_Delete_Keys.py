sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]

for key in keys:
    sample_dict.pop(key)
print(sample_dict)