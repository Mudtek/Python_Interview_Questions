"""Example of weak references - where you can keep track of an object, 
without preventing it from being garbage collected"""

import weakref

class PlayerLevel:
    def __init__(self, value: any) -> None:
        self.value = value

my_object = PlayerLevel(42)
my_ref = weakref.ref(my_object)

print(my_ref() is my_object)
del my_object
print(my_ref() is None)