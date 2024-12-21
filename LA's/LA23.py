class AnimeCharacter:
    def __init__(self, name, ability):
        self.__name = name
        self.ability = ability

    def buksan(self, new_func):
        def opening(*args, **kwargs):
            print("--- Introducing... ---")
            new_func(*args, **kwargs)
            print("--- This character is amazing!... ---")
            print("")

        return opening


anime_ability = AnimeCharacter("Naruto", "Shadow Clone Jutsu")


@anime_ability.buksan
def anime(sign, receiver, delivery_fee):
    print(f"{sign} I am {receiver} and i can use {delivery_fee} ")


anime(">>", "Naruto", "Shadow Clone Jutsu")