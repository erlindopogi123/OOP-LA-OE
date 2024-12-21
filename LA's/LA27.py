from abc import ABC, abstractmethod

class NinjaTurtles(ABC):
    def __init__(self, real_name, __alias):
        self.real_name = real_name

    @property
    @abstractmethod
    def __init__(self, real_name):
        pass

class Leonardo (NinjaTurtles):
     def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias
     @property
     def alias(self):
        return self.__alias

class MichaelAngelo (NinjaTurtles):
     def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias

     @property
     def alias(self):
        return self.__alias     

class Donatello (NinjaTurtles):
     def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias

     @property
     def alias(self):
        return self.__alias

class Raphael (NinjaTurtles):
     def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias

     @property
     def alias(self):
        return self.__alias

if __name__ == "__main__":
    pogi = Leonardo("Leonardo", "Mau")
    pogi1 = MichaelAngelo ("MichaelAngelo", "Jr")
    pogi2 = Donatello ("Donatello", "Erlindo")
    pogi3 = Raphael ("Raphael", "Erl")
    print(pogi.alias)
    print(pogi1.alias)
    print(pogi2.alias)
    print(pogi3.alias)


