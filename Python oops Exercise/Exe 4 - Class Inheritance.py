# OOP Exercise 4: Class Inheritance
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
class Model(Vehicle):
    def seating_capacity(self):
        return super().seating_capacity(capacity=4)

m1 = Model("Polo",180,21)
print(m1.seating_capacity())
    