class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
   
ferrari= Car("Ferrari","Red")
ferrari.brand = "Ferrari"
print(f" Car1\n {ferrari.brand},{ferrari.color} ")
ferrari.color = "White"
print(f" {ferrari.brand}, {ferrari.color}")
ferrari.brand = "Rambo"
ferrari.color = "Black"
print(f" Car2\n {ferrari.brand},{ferrari.color} ")