"""Examples of Class Decorators"""

def add_methods(cls):
    def fly(self):
        return "You are flying."
    cls.fly = fly
    return cls

@add_methods
class MyClass:
    def __init__(self, x):
        self.x = x

    def my_method(self):
        return f"The value of x is {self.x}."

obj = MyClass(1)
print(obj.my_method())
print(obj.fly()) 