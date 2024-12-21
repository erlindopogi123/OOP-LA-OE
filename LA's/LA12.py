class toy ():
    def __init__(self, name, price):
        self.name = name
        self.price = price
       
    def describetoy(self):
        print(f"the name of this toy {self.name} and the price of this is {self.price}")
       
class car(toy):
    def __init__(self, name, price):
        super().__init__(name, price)
 
toy1 = toy("ball", 150)
toy1.describetoy()