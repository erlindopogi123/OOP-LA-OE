class Appliances():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def operate(self):
        print("Operating")
   
    def info(self):
        print(f"Brand: {self.brand} Model: {self.model}")
       
class WashingMachine(Appliances):
    def operate(self):
        print("WashingMachine!")

class Refrigerator(Appliances):
    def operate(self):
        print("Kepping food cold!")
       
class Microwave(Appliances):
    def operate(self):
        print("Heating food!")
       
washing = WashingMachine("Samsung", "1")
ref = Refrigerator("Lg", "2")
micro = Microwave("Panasonic", "3")
for x in [washing, ref, micro]:
    x.operate()
    x.info()