employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
output = dict.fromkeys(employees, defaults)
print(output)