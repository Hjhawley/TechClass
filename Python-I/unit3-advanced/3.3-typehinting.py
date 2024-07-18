# Type Hinting

# Python is a dynamically typed language, which means that the type of a variable is 
# checked only during runtime. However, as your programs get larger and more complex,
# it would be helpful to have some way to check types earlier.

# Python 3.5 introduced "type hinting", which lets you annotate your functions to
# suggest the data types of the arguments and the return value. These hints don't 
# affect the actual runtime of the program -- they're just  hints, and the Python
# interpreter doesn't enforce them. However, they can be very helpful for reading and
# understanding code.

# Here's a function without type hints:
def describe_age(age):
    return f"You are {age} years old."

# And here's the same function with type hints:
def describe_age(age: int) -> str:
    return f"You are {age} years old."

# The ': int' after 'age' is a hint that 'age' should be an integer. The '-> str' before
# the colon is a hint that the function should return a string.

# You can use built-in types like 'int', 'list', 'dict', etc. for type hints.
# For more complex types like lists and dictionaries, you can use the typing module to
# provide more specific type hints:

from typing import List, Dict

def total_sales(sales: Dict[str, int]) -> int:
    return sum(sales.values())

def find_largest(numbers: List[int]) -> int:
    return max(numbers)
