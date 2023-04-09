"""Questions could range wildly depending on the role you're looking at, and also the specialization - maybe the role is geared
around DB integration, in which case there are going to be Python questions specifically related to DB packages, but here I'm
attempting to give the best rounded questions that I might ask an engineer or I have been asked myself"""

import copy
from typing import List

"""Moderate Questions"""

# ====================================================================================================================
# Question 1. In terms of algorithms, what is a Binary Search?
#
#   Answer: Its an optimized method of finding an index of a sorted array by grabbing the middle index of a collection
#       and based on the result, halfing the search parameters recursively left/right of the middle index. This finds
#       the answer faster typically, rather than iterating over ever single index to find an item.

# ====================================================================================================================
# Question 2. What is the difference between 'is' and '=='? (I have received this question in two interviews)
#
#   Answer: 'is' keyword such as (a is b) means that the identity of variables are the same
#       whereas '==' (a == b) means that the value of the two variables are the same

# ====================================================================================================================
# Question 3. What is the difference between a list, tuple, and set in Python? When would you use each?
#
#   Answer: Lists are dynamic arrays that can store any combination of data types. They are mutable, ordered, but use
#   an overallocation method that make them most useful when the size of collection will be unknown. Tuples are the same
#   thing as Lists except that they are immutable. Sets are the same thing as Dictionaries, except that they have null
#   values and are just the keys. Use Lists when you will be making lots of changes that require ordering. Tuples when
#   the data is always going to be a specific size in a certain order (like CLI inputs, Vector3s, Coordinates), and Sets
#   when you don't care about the order, but want a faster lookup than Lists for optimization.

# ====================================================================================================================
# Question 4. How do you create a virtual environment in Python, and why is it important?
#
#   Answer: There is a built in module called 'venv' that can be activated by going to a directory and
#       running the following command `python3 -m venv --python=/usr/bin/python3.9 <name>`. Virtual environments
#       enable you to switch between python versions more easily. There also is the `pyenv` which will install any
#       number of python versions and works by switching the $PATH to point to whichever version of python you now
#       want to use - this is useful when you don't want directories to be associated with python versions (although
#       pyenv does have the capability to automatically switch versions based on directories if you so choose)

# ====================================================================================================================
# Question 5. Explain list comprehensions and provide an example of their usage.
#
#   Answer: It can be a faster way to create lists of data based on other lists or mappings. It also is a way
#       to make a deep copy of a list so that the new list does not use any references to the old values

list_comprehension: List[str] = ["this", "is", "a", "mudtek", "list"]

# Note: If we changed anything in this new list, it will not affect the original 'list_comprehension' list
new_list_comprehension: List[str] = [word for word in list_comprehension]

print("Question 5 Comprehension List Example Output: " + str(new_list_comprehension))

# ====================================================================================================================
# Question 6. What are decorators in Python, and how do you use them? Provide an example.
#
#   Answer: Decorators are notated by adding '@' + function_name above a function, this will make that function
#       become an input to the decorator function. This is useful for when you want to modify your existing functions
#       with some checks like logging, authentication, and validation

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Question 6 Decorator Example Output: " + f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print("Question 6 Decorator Example Output: " + "Returned {result}")
        return result
    return wrapper

# Notice the @ + function_name
@log_decorator
def greet(name):
    return f"Hello, {name}!"

greet("Alice")

# ====================================================================================================================
# Question 7. What is the Global Interpreter Lock (GIL), and how does it affect multithreading in Python?
#
#   Answer: GIL puts a mutex lock on resources. For cPython (the default interpeter) this means that only one
#       thread can be processed by the CPU at a time. It is therefore better in some cases to use multiprocessing.

# ====================================================================================================================
# Question 8. Explain the differences between Python 2 and Python 3. What are some key features introduced in Python 3?
#
#   Answer: There are a number of improvements, but common ones are:
#       the Print() requires the parenthesis now, 
#       unicode support - unicode is used for strings by default instead of ASCII
#       '/' is now true divison, while '//' is equal to python2's '/' (integer division)

# ====================================================================================================================
# Question 9. Describe how to handle exceptions in Python. What are the differences between the try, except, finally, and else clauses?
#
#   Answer: exceptions are events that occur when an error is encountered during the execution of a program. To handle exceptions, 
#       you can use a combination of try, except, finally, and else clauses.

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Question 9 ZeroDivision: " + "Error: Division by zero is not allowed.")
    except TypeError:
        print("Question 9 TypeError: " + "Error: Invalid input. Only numbers are allowed.")
    else:
        print("Question 9 Else: " + f"Result: {result}")
    finally:
        print("Question 9 Finally: " + "Finished executing the divide function.")

# Example usage:
divide(4, 2)
divide(4, 0)
divide("4", 2)

# ====================================================================================================================
# Question 10. What are some different programming styles and what are there use-cases?
#
#   Answer: This question is very subjective, and there are many programming styles, but there are 3 main ones commonly
#       touted: Object-oriented, procedural, and functional. A good analog for procedural is building a house in an exact
#       order from start to finish, where as object-oriented is like breaking down the walls, doors, flooring, etc into
#       individual components with multiple instances. So if you had 10 walls, and 4 doors - you might build a house
#       design that matches those specs better. Functional is like breaking down the materials into different components
#       and maticulously building floor boards, shingles, door knobs, from those materials. Its the most granular.
#
#       These approaches have different use cases. For an operations script where you're checking to see if a network
#       link is up/down. You could have an exact runthrough that happens every time. But if you were diagnosing a network
#       device, maybe you have an object for each port - with every port having its own speed, name, number, tx, rx, etc.
#       If you wanted a library of files that don't focus on changing state, but rather giving exact calculations based on
#       a given input - a functional approach is best.
#
#       Procedural is great for fixed data that needs to acheive a certain result (operational scripts, debugging scripts)
#       Object-oriented is great for when you have many instances of the same thing, but with their own unique values (like video games)
#       Functional is great for Data Analysis and Front-End Web Development
#
#       Note: There are plenty of other types like Aspect-oriented and Event-driven styles, but the 3 above are a great start

# ====================================================================================================================
# Question 11. Explain the concept of shallow and deep copy in Python. When would you use each?
#
#   Answer: A shallow copy creates a new object, but instead of copying the nested objects, it copies only the references to those 
#       nested objects. This means that the new copy and the original object will still share the same nested objects. If you modify 
#       a mutable nested object in one of the copies, the change will be reflected in the other copy as well.

# Shallow Copy
original_list: List[List[int]] = [[1, 2], [3, 4]]
shallow_copy = copy.copy(original_list)

shallow_copy[1][0] = 99
print("Question 11 Shallow-Copy Output: " + str(original_list))  # Output: [[1, 2], [99, 4]]

# Deep Copy
original_list: List[List[int]] = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(original_list)

deep_copy[1][0] = 99
print("Question 11 Deep-Copy Output: " + str(original_list))  # Output: [[1, 2], [3, 4]]

# If you didn't want to import the copy module then use list comprehension!
deep_copy_list_comprehension: List[List[int]] = [[item for item in inner_list] for inner_list in original_list]
print("Question 11 Deep-Copy List Comprehension Output: " + str(deep_copy_list_comprehension))

# ====================================================================================================================
# Question 12. Describe the differences between *args and **kwargs in Python function arguments.
#
#   Answer: *args takes any number of input arguments as an input signature, while **kwargs does the same thing
#       except for keys - so input Sets or Dictionaries would correlate with **kwargs argument. They stand for arguments
#       and key word arguments.

def args_function(*args):
    for arg in args:
        print("Question 12 *args Example Output: " + str(arg))

args_function(1, 2, 3)

def kwargs_function(**kwargs):
    for key, value in kwargs.items():
        print("Question 12 *kwargs Example Output: " + f"{key}: {value}")

info = {"name": "Bob", "age": 40, "city": "Chicago"}
kwargs_function(**info)

def both_argskwargs(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print("Question 12 *args|*kwargs Example Output: " + str(arg))
    
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print("Question 12 *args|*kwargs Example Output: " + f"{key}: {value}")

both_argskwargs(1, 2, 3, name="Alice", age=30, city="New York")

# ====================================================================================================================
# Question 13. How do you handle memory management in Python? Explain garbage collection and reference counting.
#
#   Answer: Reference counting is where Python automatically counts references to data, so like an object might be referenced
#       4 times in code, but every time a reference is removed, the counter goes backwards. Once the counter reaches 0
#       Python automatically frees up memory. There are situations where this does not catch everything - like when two
#       or more objects refer to each other (cyclical reference). Garbage collection is automatically done by Python
#       periodically checking unused resources and potentially freeing them up. There are situations, however, where
#       your code could be super optimized on a low-resource device, in which case you could actually disable garbage
#       collection in Python to work better - garbage collection is a process that adds overhead itself.

# ====================================================================================================================
# Question 14. What is the purpose of the __init__.py file in Python packages?
#
#      Answer: It's a special python file that signifies that the directory is a package.

# ====================================================================================================================
# Question 15. Describe the differences between class-based inheritance and multiple inheritance in Python. Provide an example.
#
#   Answer: class-based inheritance is where you have a class that accepts another class as an input into its signature:
#       class Dog(Animal). That child class can override methods in the parents class, or in the absence of its own methods
#       it will use the parent classes methods. Multiple inheritance is exactly as it sounds - where you inherit more than 1
#       parent class.

class FileSaver:
    def save(self):
        print("Question 15 Example Output: " + "Saving file...")

class DataProcessor:
    def process(self):
        print("Question 15 Example Output: " + "Processing data...")

# This becomes `multiple inheritance` simply by having more than one parent class in the input signature
class ExcelExporter(FileSaver, DataProcessor):
    def export(self):
        self.process()
        self.save()

exporter = ExcelExporter()
exporter.export()

# ====================================================================================================================
# Question 16. What is duck typing in Python, and how does it affect the way you write code?
#
#   Answer: duck typing comes from the phrase "if it walks like a dog, quacks like a duck...". It means that youre code
#       isn't statically operating on a set data type, but rather operating based on what the input can do. An example
#       would be that if the input of a function has a length - then it means it can be iterated, therefore iterate it.

class Duck:
    def quack(self):
        print("Question 16 Duck Typing Example Output: " + "Quack!")

class Dog:
    def bark(self):
        print("Question 16 Duck Typing Example Output: " + "Woof!")

def make_noise(animal):
    animal.quack() if hasattr(animal, "quack") else animal.bark()

duck = Duck()
dog = Dog()

make_noise(duck)
make_noise(dog)

# ====================================================================================================================
# Question 17. Explain the concept of context managers and the with statement in Python. Provide an example.
#
#   Answer: The 'with' statement in Python is used to reference a resource, so that once the subsequence code block
#       exists, the resource will be released. This is commonly used with OS package, network connections, mutexes.
#       Context managers are just methods/classes that facilitate resource handling (which describes many OS methods)

with open("setup.py") as file:
    contents = file.read()
    print("Question 17 With Statement Example Output: " + contents)

#=====================================================================================================================
# Question 18. What are dunder methods? Give examples.
#
#   Answer: They are special reserved methods, ending and beginning with double underscores in Python, that define 
#       modules and classes. 

# If you run a python file directly the __name__ automatically becomes "__main__" - so we're saying here "only run
# the print method if this file is being run directly. Otherwise, __name__ will be the name of the current module (file)"
if __name__ == "__main__":
    print("Question 18 Dunder Example Output: __name__ = " + __name__)

class Vector:

    # Special initialization method used extensively for classes
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # If you add this object with something else using the + operator - this is what will happen
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)

# add the two vector objects together using the "+" operator
v3 = v1 + v2

print("Question 18 Dunder Example Output: " + str(v3.x) + "|" + str(v3.y))
