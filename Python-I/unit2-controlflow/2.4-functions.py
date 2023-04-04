# Functions

# A function (sometimes called a subroutine) is a block of reusable
# code that performs a specific task. It allows you to break down
# complex programs into smaller, more manageable pieces of code,
# making your code easier to read, understand, and maintain.
# A function may or may not take one or more inputs, and may or may
# not return an output value.

# We define a function using the 'def' keyword. This line is called the header.
# We name the function and follow it with a pair of parentheses and a colon.
# If there are any parameters, they go inside the parentheses, separated by commas.
# The body of the function goes below the header and is indented.
def square(x):
    print(x ** 2) # This function takes a number and prints the square of it.
# We call a function by using its name followed by parentheses and
# any necessary arguments. If the function returns a value, we can assign that
# value to a variable.
square(3) # This will print 9


# Here's an example of a function without a return statement.
# Sometimes these are called "void functions".
def greet(name):
    print(f"Hello, {name}!")
greet("Roo") # Prints "Hello, Roo!"
# This function doesn't return a value. It just prints a string.


# Functions can be defined with multiple parameters:
def print_name_age(name, age):
    print(f"{name} is {age} years old.")
print_name_age("Alice", 30) # Prints "Alice is 30 years old."


# Functions can be set up to have default parameter values.
# If the function call doesn't specify, the default value is used.
def repeat(word, times = 3):
    print(word * times)
repeat("hello") # Prints "hellohellohello"
repeat("bye", 2) # Prints "byebye"


# The 'return' keyword is used to output a value when the function is called.
def add_numbers(x, y):
    sum = x + y
    return sum
result = add_numbers(5, 7)  # Takes two arguments and assigns a value to 'result'
print(result)               # This will print 12


# Functions can take an arbitrary number of arguments:
def multiply(*args):
    product = 1
    for arg in args:
        product *= arg # Multiplies every argument
    return product
result = multiply(2, 3, 4)
print(result) # Prints 24


# Functions can be passed as arguments to other functions:
def do_twice(func, x):
    return func(func(x)) 
result = do_twice(square, 2) # This calls the 'square' function we defined earlier
print(result) # Prints 16


# Functions can be nested:
def outer():
    print("Outer function")
    def inner():
        print("Inner function")
    inner()
outer() # Prints "Outer function" and then "Inner function"