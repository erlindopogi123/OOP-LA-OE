class party:
    def __init__(self, theme, foods):
        self.theme = theme
        self.foods = foods
    def __bday(self):
        print(f"Party Theme: {self.theme} with {self.foods}")
    def pub(self):
        self.__bday()
       
debut = party("Birth day", "Cake")
holloween = party("Holloween", "Pumpkin")
newyear = party("New Year", "Red Cake")
debut.pub()
holloween.pub()
newyear.pub()