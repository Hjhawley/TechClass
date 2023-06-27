"Indentation"
# Note the number of spaces for each level of indentation
def function_example(argument1, argument2):
    if argument1 > argument2:  # 4 spaces
        result = argument1  # 8 spaces
    else:
        result = argument2
    return result


"Maximum Line Length (79-character limit)"
# Don't:
def my_function(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z):
    return a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s + t + u + v + w + x + y + z

# Do:
def my_function(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z):
    return (
        a + b + c + d + e + f + g + h + i + j + k + l + m + n
        + o + p + q + r + s + t + u + v + w + x + y + z
    )


"Naming Conventions"
# Function name
def calculate_area(width, height):
    return width * height

# Class name
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


"Imports"
# Standard library imports
import os
import sys

# Third-party imports
import numpy as np

# Local application imports
from my_package import my_module


"Whitespace"
# Two blank lines between top-level functions and class definitions 
# and one blank line between method definitions within a class.
def function_one():
    pass


def function_two():
    pass


class MyClass:
    def method_one(self):
        pass

    def method_two(self):
        pass


"Inline Comments"
x = 1
y = 2
x = x + y  # This is an inline comment explaining the purpose of this operation


"Trailing Commas"
my_list = [
    'item1',
    'item2',
    'item3',  # Trailing comma
]


"String Quotes"
my_string = 'string'
my_string = "string" # Both of these are fine, just stay consistent


"Spaces Around Operators"
# Don't:
z=10

# Do:
z = 10

result = x * (y + z) - x  # Spaces around operators, but not inside parentheses
my_list = [1, 2, 3, 4]  # Spaces after commas, but not inside brackets


"Identity vs. Equality (Comparison to None and Boolean Values)"
# Incorrect way to compare to None
if x == None:
    pass

# Correct way to compare to None
if x is None:
    pass

# Incorrect way to check for a Boolean value
if x == True:
    pass

# Correct way to check for a Boolean value
if x:
    pass