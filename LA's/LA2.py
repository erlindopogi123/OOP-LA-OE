class ml_hero() :
 def __init__(self, name, basic_attk, role ) :

     self.name = name
     self.basic_attk = basic_attk
     self.role = role
     

M1 = ml_hero("Fighter:", "Yu Zhong", 250)
M2 = ml_hero("Marksman:", "Claude", 200)

print(f"{M1.name}\n{M1.basic_attk}\n{M1.role}\n{M2.name}\n{M2.basic_attk}\n{M2.role}")