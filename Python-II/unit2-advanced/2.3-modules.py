# Modular Programming Revisited

# Modular programming is a software design technique that emphasizes separating the functionality
# of a program into independent, interchangeable modules. Each module contains everything necessary
# to execute only one aspect of the desired functionality.

# You learned about importing modules way back in Python I Unit 3. Now you'll learn how to write
# your own modular programs.

# Benefits of Modular Programming:
# 1. Code Reusability: Modules can be reused across different programs.
# 2. Maintainability: Easier to maintain and update individual modules.
# 3. Collaboration: Facilitates teamwork by allowing different team members to work on separate modules.
# 4. Readability: Improves the readability and organization of the code.

# Writing and Using Custom Modules

# In Python, a module is simply a file containing Python definitions and statements.
# The file name is the module name with the suffix .py added.

# Example: Creating a module named my_module.py
# Save the following code in a file named my_module.py

# my_module.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# Importing Custom Modules

# You can import the module using the import statement and access the functions using dot notation.
# Save the following code in a file named main.py

# main.py
import my_module

# Using functions from my_module
print(my_module.greet("Alice"))  # Output: Hello, Alice!
print(my_module.add(5, 3))       # Output: 8

# Importing Specific Functions

# You can also import specific functions from a module using the from ... import statement.
# Save the following code in a file named main.py

# main.py
from my_module import greet, add

# Using imported functions directly
print(greet("Bob"))  # Output: Hello, Bob!
print(add(10, 7))    # Output: 17

# Organizing Code into Multiple Modules

# Let's create a few more modules to demonstrate how to organize code into multiple modules.

# Create a module named arithmetic.py
# arithmetic.py
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# Create another module named greetings.py
# greetings.py
def hello(name):
    return f"Hello, {name}!"

def goodbye(name):
    return f"Goodbye, {name}!"

# Importing Multiple Custom Modules

# Save the following code in a file named main.py

# main.py
from arithmetic import multiply, divide
from greetings import hello, goodbye

# Using functions from arithmetic.py
print(multiply(3, 4))  # Output: 12
print(divide(10, 2))   # Output: 5.0

# Using functions from greetings.py
print(hello("Charlie"))   # Output: Hello, Charlie!
print(goodbye("Charlie")) # Output: Goodbye, Charlie!

# Organizing code into modules helps in building scalable and maintainable applications.
# Practice modular programming by dividing your code into logical modules and reusing them across different projects.
