"""Lambda Example"""

from typing import List

str_list: List[str] = ['hello', 'world', 'python', 'is', 'great']

# =========================================================================

# Use map() and a lambda function to capitalize each string
str_list: List[str] = list(map(lambda x: x.capitalize() if x == "hello" or x == "world" \
                               else x, str_list))

print("Lambda Example Map Output: " + str(str_list))

# =========================================================================

def lambda_equivalent(x: str) -> str:
    """Returns a capitalized string"""
    return x.capitalize()

# If lambda's seem confusing - here is an example to of a standalone function instead
non_lambda_str_list: List[str] = list(map(lambda_equivalent, str_list))

print("Non-Lambda Map Example Output: " + str(non_lambda_str_list))

# =========================================================================

numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter()
even_numbers: List[int] = list(filter(lambda x: x % 2 == 0, numbers))
print("Lambda Filter Example: " + str(even_numbers))

numbers: List[int] = [2, 4, 6, 8, 10]

def are_any_true(numbers: List[int]) -> bool:
    for number in numbers:
        if number % 2 == 0:
            return True
    return False

# Any() - Check if any number in the list is even
has_even_number: bool = are_any_true(numbers)
has_even_number: bool = any(map(lambda x: x % 2 == 0, numbers))
print("Lambda Any Example: " + str(has_even_number))

# All() - Check if all numbers in the list are even
are_all_numbers_even: bool = all(map(lambda x: x % 2 == 0, numbers))
print("Lambda All Example: " + str(are_all_numbers_even))

# ========================================================================

# Sorted() - Did you know sorted has an option for Lambdas?
numbers: List[int] = [4, 2, 7, 1, 8, 3, 5, 6]
sorted_numbers: List[int] = sorted(numbers, key=lambda x: -x)
print("Lambda Sorted Exampled: " + str(sorted_numbers))
