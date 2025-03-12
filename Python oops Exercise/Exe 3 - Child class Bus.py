# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Model(Vehicle):
    print("Model")

m1 = Model("Audi",200,15)
print(m1.name,m1.max_speed,m1.mileage)
