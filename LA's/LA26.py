from abc import ABC, abstractmethod


class NinjaTurle(ABC):
    @property
    @abstractmethod
    def alias(self):
        pass

# Leonardo class
class Leonardo(NinjaTurle):
    def __init__(self, real_name):
        self.real_name = real_name
        self.__alias = "Leo"  
    @property
    def alias(self):
        return self.__alias

# Michelangelo class
class Michelangelo(NinjaTurle):
    def __init__(self, real_name):
        self.real_name = real_name
        self.__alias = "Mikey"  
    
    @property
    def alias(self):
        return self.__alias

# Donatello class
class Donatello(NinjaTurle):
    def __init__(self, real_name):
        self.real_name = real_name
        self.__alias = "Don"  
    
    @property
    def alias(self):
        return self.__alias

# Raphael class
class Raphael(NinjaTurle):
    def __init__(self, real_name):
        self.real_name = real_name
        self.__alias = "Raph"  
    
    @property
    def alias(self):
        return self.__alias



from turtle import Leonardo, Michelangelo, Donatello, Raphael

def main():
    
    leo = Leonardo("Leonardo")
    mikey = Michelangelo("Michelangelo")
    don = Donatello("Donatello")
    raph = Raphael("Raphael")

   
    print(f"{leo.real_name}'s alias is {leo.alias}")
    print(f"{mikey.real_name}'s alias is {mikey.alias}")
    print(f"{don.real_name}'s alias is {don.alias}")
    print(f"{raph.real_name}'s alias is {raph.alias}")

if __name__ == "__main__":
    main()
