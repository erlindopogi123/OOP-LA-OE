class ml_hero() :
 def __init__(self, name, role ) :
     self.name = name
     self.role = role
     
 def describe(self):
     return f"{self.name} is a {self.role}"
     
 def __str__(self):
     return f"This {self.name} object is created using ml_hero class"
     
m1 = ml_hero("Chou", "Fighter")
print(m1)