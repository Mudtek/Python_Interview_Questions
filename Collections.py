# Make sure you know the differences!

from typing import List

# List
#   Mutable
#   Ordered
#   Duplicate Values Allowed
races_list: List[str] = ["human", "elf", "minotaur", "tiger", "bear", "leopard", "minotaur"]

# Tuple
#   Immutable
#   Ordered
#   Duplicate Values Allowed
races_tuple: List[str] = ("human", "elf", "minotaur")

# Set
#   Mutable
#   Unordered
#   Unique Values
races_set: List[str] = {"human", "elf", "minotaur"}

temp_list = list(set(races_list))
print(temp_list)

# Dict
#   Mutable
#   Mapping key/value pairs
#   Unordered
#   Unique Values
races_dict: List[str] = {"level": 2, "XP": 100, "race": "Minotaur"}

# ^ In Common:
#       All are iterable
#       All can contain any data types within them






