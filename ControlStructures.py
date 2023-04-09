### Example Control Structures ###

# If statements: Used to execute code based on whether a particular condition is true or false.

# For loops: Used to iterate over a sequence of values (such as a list or tuple) and execute a block 
#    of code for each item in the sequence.

# While loops: Used to repeatedly execute a block of code as long as a particular condition is true.

# Try-except statements: Used to handle errors and exceptions that may occur during program execution.

# Break and continue statements: Used to alter the flow of execution in a loop. Break is used to exit a loop, 
#   while continue is used to skip the current iteration and move on to the next.

# List comprehensions: A concise way of creating a new list by iterating over an existing list 
#   or sequence and applying some operation to each item.

from typing import Dict, List

# Example of If Statements
x = 10
if x > 5:
    print("If Statement Example Output: " + "x is greater than 5")
else:
    print("If Statement Example Output: " + "x is not greater than 5")


# Example of For loop
fruits: List[str] = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("For loop Example Output: " + str(fruit))


# Example of While loop
i = 1
while i <= 5:
    print("While Loop Example Output: " + str(i))
    i += 1


# Example of Try-Except
x = 5
y = "2"
try:
    z = x + y
except TypeError:
    print("Try-Except Example Output" + "Cannot add a string and an integer")


# Example of Break-Continue
fruits: List[str] = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print("Break-Continue Example Output: " + str(fruit))

fruits: List[str] = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print("Break-Continue Example Output: " + str(fruit))


# Example of List Comprehension
characters: List[Dict[str, str]] = [
    {"name": "Bob", "race": "human"},
    {"name": "Alice", "race": "elf"},
    {"name": "Charlie", "race": "minotaur"},
    {"name": "David", "race": "dwarf"},
    {"name": "Jordan", "race": "minotaur"}
]

minotaur_names: List[str] = [x["name"] for x in characters if x["race"] == "minotaur"]

print("List Comprehension Example Output: " + str(minotaur_names))