num1 = int(input("Enter Number:"))
num2 = int(input("Enter Number:"))
print(f"Multiplication of {num1} and {num2} is {num1 * num2}")
print(f"Sum of {num1} and {num2} is {num1 + num2}")

# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
str1 = input("Enter String 1:")
str2 = input("Enter String 2:")
str3 = input("Enter String 3:")

print(str1,str2,str3,sep="**")

# # Exercise 3: Convert Decimal number to octal using print() output formatting
num = int(input("Enter Number:"))
print('%o' % num)

# # Exercise 4: Display float number with 2 decimal places using print()
num = 458.541315
print(round(num,2))

# # Exercise 5: Accept a list of 5 float numbers as an input from the user
number = []
for i in range(5):
    num = float(input("Enter Number:"))
    number.append(num)
print(number)

# Exercise 7: Accept any three string from one input() call
name = input("ENTER VALUE: ")
print(name.split())