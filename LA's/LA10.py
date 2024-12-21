class vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    def __str__(self):
        return f"the brand of this car is {self.brand} the model of this brand is {self.model} and the fuel type of this is {self.fuel_type}"
       
class car1(vehicle):
    pass

brand1 = car1("honda", "civic", "diesel")
print(brand1)

class motorcycle(vehicle):
    pass

brand2 = motorcycle("mio", "nmax", "primeum")
print(brand2)
