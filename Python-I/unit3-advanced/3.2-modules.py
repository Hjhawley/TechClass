# Modules and Libraries

# A Python modules is a single .py files that defines functions, classes, 
# and variables that you can reference in other Python .py files. Libraries
# are a collection of multiple modules. 

# Built-in Libraries
# Python has a number of libraries built into it. We call these the
# "standard library", and they provide a wide range of functionality.

# Here's an example of importing and using the 'math' module from the
# standard library:
import math

print(math.sqrt(16))  # prints "4.0"

# 'sqrt' is a function of the 'math' module, so if we want to use Python's
# built-in square root function, we have to import the math module.

# You can import a specific function or variable from a module like this:
from math import sqrt

print(sqrt(16))  # prints "4.0"

# The difference here is that we're only importing a single function from
# the math module, not the entire module. This means that we can use 'sqrt'
# directly without having to prefix it with 'math.', but other functions
# and variables from the 'math' module won't be available unless they're
# also explicitly imported.

# Python has a built-in module named 'random' that allows us to generate
# random numbers. The 'randint' function from the 'random' module is used
# to generate a random integer number within a specified range.
import random

# This will print a random integer number between 1 and 10.
print(random.randint(1, 10))  


# Third-party Libraries
# In addition to the standard library, there are thousands of third-party
# libraries that have been created by the Python community. These are
# libraries that do not come with Python by default, but can be installed
# using tools like pip.

# Here's an example of using a third-party library called 'requests',
# which is used for making HTTP requests.

# Before you can use it, you need to install it. Type this in your terminal
# or command prompt (without quotes):

"pip install requests"

# Once installed, you can use it in your scripts like this:

import requests
response = requests.get('https://www.example.com')
print(response.status_code)  # prints the HTTP status code

# We usually import all modules at the very top of the file. This is a 
# convention that makes it easy to see at a glance what modules a program
# depends on.