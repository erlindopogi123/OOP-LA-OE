class Champion:
    def __init__(self, name, hp, atk_power):
        self.name = name
        self.hp = hp
        self.atk_power = atk_power
       
    def basic_attack(self, target):
        target.hp = target.hp - self.atk_power
        print(f"{self.name} attacks {target.name} for {self.atk_power} damage.")

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name} heals for {amount} hp.")


Yasuo = Champion("Yasuo", 1000, 200)
Kayn = Champion("Kayn", 2000, 90)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Yasuo.basic_attack(Kayn)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Kayn.heal(100)

Kayn.basic_attack(Yasuo)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Yasuo.basic_attack(Kayn)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Kayn.heal(100)

Kayn.basic_attack(Yasuo)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Kayn.basic_attack(Yasuo)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Yasuo.basic_attack(Kayn)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Kayn.basic_attack(Yasuo)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Yasuo.basic_attack(Kayn)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Kayn.basic_attack(Yasuo)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Yasuo.basic_attack(Kayn)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")
Kayn.basic_attack(Yasuo)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Yasuo.basic_attack(Kayn)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Kayn.basic_attack(Yasuo)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Yasuo.basic_attack(Kayn)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Kayn.basic_attack(Yasuo)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Yasuo.basic_attack(Kayn)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Kayn.basic_attack(Yasuo)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Yasuo.basic_attack(Kayn)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Kayn.basic_attack(Yasuo)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Yasuo.basic_attack(Kayn)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Kayn.basic_attack(Yasuo)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")

Yasuo.basic_attack(Kayn)
print(Yasuo.name, Yasuo.hp, "hp", Yasuo.atk_power, "dmg")
print(Kayn.name, Kayn.hp, "hp", Kayn.atk_power, "dmg")
