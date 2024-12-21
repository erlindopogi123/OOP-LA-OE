
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Bark!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Meow!"

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Chirp!"

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "..."


def animal_sounds(animal):
    print(f"{animal.name} speaks: {animal.speak()}")


dog = Dog("Sheddy")
cat = Cat("Puss")
bird = Bird("Birdy")
fish = Fish("Fishda")


animals = [dog, cat, bird, fish]


for animal in animals:
    animal_sounds(animal)
