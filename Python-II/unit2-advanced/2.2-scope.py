# Scope

# Scope refers to the region of the code where a variable is accessible.
# There are four types of scope:
# 1. Local Scope
# 2. Enclosing Scope
# 3. Global Scope
# 4. Built-in Scope


# Local Scope
# Variables declared inside a function are in the local scope and can only be
# accessed within that function.

def my_function():
    local_var = "This is a local variable"
    print(local_var)    # Output: This is a local variable

my_function()
#print(local_var)       # This raises an error because local_var is not accessible outside the function


# Enclosing Scope
# This is also known as non-local scope. Variables in enclosing functions
# can be accessed in nested functions.

def outer_function():
    outer_var = "This is an outer variable"

    def inner_function():
        inner_var = "This is an inner variable"
        print(outer_var)    # Output: This is an outer variable
        print(inner_var)    # Output: This is an inner variable
    
    # Notice how outer_var is accessible within the inner_function
    # Pay attention to indentation, it's how you can tell scope

    inner_function()
    #print(inner_var)       # This raises an error because inner_var is not accessible outside inner_function

outer_function()    # Output: This is an outer variable; This is an inner variable


# Global Scope
# Variables declared outside of all functions are in the global scope and can
# be accessed from any function within the same module.

global_var = "This is a global variable"

def another_function():
    print(global_var)  # Output: This is a global variable

another_function()

# Modifying a global variable within a function
# To modify a global variable within a function, you need to use the `global` keyword.

counter = 0

def increment_counter():
    global counter
    counter += 1

increment_counter()
increment_counter()
print(counter)  # Output: 2


# Built-in Scope
# Built-in scope includes built-in functions and exceptions provided by Python.
# For example, functions like `len()`, `print()`, and `input()` are always available.

print(len("Hello, World!"))  # Output: 13

# Scope Resolution - LEGB Rule
# Python follows the LEGB rule to resolve the scope of a variable.
# LEGB stands for:
# L: Local — Variables defined within a function
# E: Enclosing — Variables in the local scope of enclosing functions
# G: Global — Variables defined at the module level
# B: Built-in — Built-in functions and exceptions

def scope_demo():
    local_var = "Local"
    def inner_demo():
        enclosing_var = "Enclosing"
        print(local_var)  # Output: Local variable
        print(enclosing_var)  # Output: Enclosing variable
    inner_demo()

scope_demo()

# Practicing scope is essential for writing clear and maintainable code.
# Remember to carefully consider the scope of your variables to avoid unexpected
# behaviors and bugs in your programs.
