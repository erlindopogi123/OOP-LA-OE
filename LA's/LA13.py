class fish:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class animal(fish):
    def __init__(self, name, type, can_swim):
        super().__init__(name, type)
        self.can_swim = True
       
       
bangus = animal("bangus", "salt water", True)
tilapia = animal("tilapia", "river water", True)

print(bangus.can_swim)