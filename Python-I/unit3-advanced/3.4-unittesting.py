# Unit Testing

# Unit testing is a method of software testing that checks individual units of 
# source code are working correctly. A unit represents the smallest testable 
# part of any software. It usually has one or a few inputs and a single output.

# Python's built-in 'assert' statement can be used for simple unit tests. It
# checks a condition and triggers an error if the condition is False. 

# Let's say we have a function in a separate file called "utils.py":
'''
def add_numbers(a, b):
    return a + b
'''

# We can write tests directly within the same file or a separate file:

import utils  # Make sure the utils.py file is in the same directory

# Test positive numbers
result = utils.add_numbers(1, 2)
assert result == 3, f"Error: {result}"

# Test negative numbers
result = utils.add_numbers(-1, -1)
assert result == -2, f"Error: {result}"

# Test zero
result = utils.add_numbers(0, 0)
assert result == 0, f"Error: {result}"

print("All tests passed.")

# Run this file with Python to execute the tests.
# If all the tests pass, then our function is working as expected.
