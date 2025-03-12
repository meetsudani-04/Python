# Exercise 12: Calculate income tax
income = 45000
tax = 0

if income <= 10000:
    tax = 0
elif income <= 20000:
    x = income - 10000
    tax = x * 10 / 100
else:
    tax = 0
    tax = 10000 * 10 / 100
    tax += (income-20000) * 20 / 100 # 20% 5000
print(tax)