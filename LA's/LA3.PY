class ml_hero() :
 def __init__(self, name, role ) :
     self.name = name
     self.role = role
     
 def describe(self):
     return f"{self.name} is a {self.role} hero"
     
 def __str__(self):
     return f"{self.name} is a {self.role}"
     
m1 = ml_hero("Beatrix", "Marksman")
print(m1.describe())