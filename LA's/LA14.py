class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describeSpiderman(self):
        print(f"Name: {self.name} Age: {self.age}")

class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle


tobey_spdrMan = Tobey("Tobey Maguire", 49, "Spider-Man (2002)")
andrew_spdrMan = Andrew("Andrew Garfield", 41, "The Amazing Spider-Man 1 (2012)")
tom_spdrMan = Tom("Tom Holland", 28, "Spider-Man: No Way Home (2021)")


print(tobey_spdrMan.name.upper(), tobey_spdrMan.movieTitle)
print(andrew_spdrMan.name.upper(), andrew_spdrMan.movieTitle)
print(tom_spdrMan.name.upper(), tom_spdrMan.movieTitle)


tobey_spdrMan.describeSpiderman()
andrew_spdrMan.describeSpiderman()
tom_spdrMan.describeSpiderman()
