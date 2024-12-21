class phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
       
    def describephone1(self):
        return f"the brand of this phone is {self.brand} and the model is {self.model}"
       

class android(phone):
    def __init__(self, brand, model):
       phone.__init__(self, brand, model)
       
cellphone = android("realme", "10")  
print(cellphone.describephone1())