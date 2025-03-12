# OOP Exercise 5: Define a property that must have the same value for every class instance (object)
class Vehicle:
    color = "white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass
        

class Car(Vehicle):
    pass

s1 = Bus("School Volov",180,12)
c1 = Car("Audu A3",200,9)

print(s1.name,s1.max_speed,s1.mileage,s1.color)
print(c1.name,c1.max_speed,c1.mileage,c1.color)