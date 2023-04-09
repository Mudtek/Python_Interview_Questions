"""Lambda Example"""

str_list = ['hello', 'world', 'python', 'is', 'great']

# Use map() and a lambda function to capitalize each string
str_list = list(map(lambda x: x.capitalize(), str_list))

print("Lambda Example Output: " + str(str_list))

# =========================================================================

def lambda_equivalent(x: str) -> str:
    """Returns a capitalized string"""
    return x.capitalize()

# If lambda's seem confusing - here is an example to of a standalone function instead
non_lambda_str_list = list(map(lambda_equivalent, str_list))

print("Non-Lambda Map Example Output: " + str(non_lambda_str_list))
