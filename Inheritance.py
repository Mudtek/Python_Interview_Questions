"""Example of Inheritance in Python"""

class Character:
    def __init__(self, name, hp, level) -> None:
        self.name = name
        self.hp = hp
        self.level = level

    def attack(self, target) -> None:
        damage = self.level * 10
        target.hp -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage.")


class Warrior(Character):
    def __init__(self, name, hp, level) -> None:
        super().__init__(name, hp, level)
        self.strength = 10

    def attack(self, target) -> None:
        damage = self.level * self.strength
        target.hp -= damage
        print(f"{self.name} swings their sword at {target.name} for {damage} damage.")


class Mage(Character):
    def __init__(self, name, hp, level) -> None:
        super().__init__(name, hp, level)
        self.intelligence = 10

    def attack(self, target) -> None:
        damage = self.level * self.intelligence
        target.hp -= damage
        print(f"{self.name} casts a spell on {target.name} for {damage} damage.")


warrior = Warrior("Gobbo", 5, 50)
mage = Mage("Merlin", 10, 100)

mage.attack(warrior)
mage.attack(warrior)
mage.attack(warrior)
