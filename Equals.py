# is versus ==

from typing import List

a: List[int] = [1, 2, 3]
b: List[int] = [1, 2, 3]
c = a

print(a == b)  # True
print(a is b)  # False
print(a is c)  # True