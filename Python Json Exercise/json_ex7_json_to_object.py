import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

def VehicleDecoder(obj):
    return Vehicle(obj['name'],obj['engine'],obj['price'])

x = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }',object_hook=VehicleDecoder)
print(type(x))
print(x)
