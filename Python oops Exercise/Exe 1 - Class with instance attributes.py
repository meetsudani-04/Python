# OOP Exercise 1: Create a Class with instance attributes
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 =Person("Meet",18)
print(p1.name)
print(p1.age)
