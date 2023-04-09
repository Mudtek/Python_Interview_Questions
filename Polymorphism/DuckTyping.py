"""Duck Typing Example"""

class Cat:
    def speak(self) -> None:
        print("The cat says meow.")

class Dog:
    def speak(self) -> None:
        print("The dog says woof.")

class Pig:
    def speak(self) -> None:
        print("The pig says oink.")

class Duck:
    def fly(self) -> None:
        print("The duck is flying.")

def make_speak(animal: object) -> None:
    if hasattr(animal, 'speak') and callable(animal.speak):
        animal.speak()
    else:
        print("This animal cannot do that")

cat = Cat()
dog = Dog()
duck = Duck()
pig = Pig()

make_speak(cat)
make_speak(dog)
make_speak(pig)
make_speak(duck)
