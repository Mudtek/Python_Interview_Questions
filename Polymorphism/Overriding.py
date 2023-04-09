"""Method Overriding"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal speaks.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("The dog barks.")

animal = Animal("generic animal")
dog = Dog("Rufus")

animal.speak()
dog.speak()