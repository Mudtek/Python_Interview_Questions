"""Built-In Decorator Examples"""


class Player:
    def __init__(self):
        self._health = 42

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        self._health = value

    @staticmethod
    def my_static_method(x, y):
        return x + y

# Notice we don't have to instantiate Player here
print(Player.my_static_method(3, 4))

new_player = Player()
print(new_player.health)

new_player.health = 100
print(new_player.health)

# =================================================================================

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str

person1 = Person("Alice", 30, "New York")
person2 = Person("Bob", 40, "San Francisco")

print(person1 == person2) 