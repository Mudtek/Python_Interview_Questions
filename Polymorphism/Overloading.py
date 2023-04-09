"""Overloading Example"""

from typing import Union

class Player:
    def __init__(self, name: str, health: int, attack: int, armor: int=0):
        self.name = name
        self.health = health
        self.attack = attack
        self.strength = armor

    # Method Overloading
    def __add__(self, item: Union['Item', 'Armor']) -> 'Player':
        if isinstance(item, Item):
            print("this was an item being added")
            return Player(self.name, self.health + item.health_bonus, self.attack + item.attack_bonus)
        if isinstance(item, Armor):
            print("this was a piece of armor being added")
            return Player(self.name, self.health, self.attack, self.strength + item.strength)
        else:
            raise TypeError("Unsupported operand type")

    def use(self, item: Union['Item', int]) -> 'Player':
        if isinstance(item, Item):
            return Player(self.name, self.health + item.health_bonus, self.attack + item.attack_bonus)
        elif isinstance(item, int):
            return Player(self.name, self.health + item, self.attack)
        else:
            raise TypeError("Unsupported argument type")

    def __str__(self) -> str:
        return f"{self.name}: Health={self.health}, Attack={self.attack}"

class Item:
    def __init__(self, name: str, health_bonus: int, attack_bonus: int):
        self.name = name
        self.health_bonus = health_bonus
        self.attack_bonus = attack_bonus

    def __str__(self) -> str:
        return f"{self.name}: Health Bonus={self.health_bonus}, Attack Bonus={self.attack_bonus}"
    

class Armor:
    def __init__(self, strength: int) -> None:
        self.strength = strength


player = Player("Hero", 100, 20)
potion = Item("Health Potion", 50, 0)
sword = Item("Iron Sword", 0, 10)
armor = Armor(2)

# Operator overloading example
player = player + potion
player = player + armor
print(player)

# Method overloading example
player = player.use(sword)
print(player)

player = player.use(10)
print(player)
