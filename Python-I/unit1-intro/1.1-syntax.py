# Basic Python Syntax

# In Python, each line of code contains its own separate instructions.
# These instructions carry out from top to bottom.

# In languages like Java and C++, indentation does not affect the
# program and is purely for the sake of user readability. However,
# indentation does matter in Python and later on we'll see some examples.

# <--- Hash symbols are used to write comments.
# Comments are ignored by the Python interpreter. They are meant for humans.
# Usually they clarify the purpose of a particular block of code.
# They can also be used to temporarily disable lines of code for testing purposes.

'''
Triple quotes like this can also be used to write multi-line comments
like this.
'''

# Throughout this course I'll be using comments to explain concepts.

print("Hello, world!")
# The above line of code should look just like the very first program you wrote.
# The print() function is a built-in Python function that allows you to
# output text to the console (aka the terminal).

# Inside the parentheses is the value we want to print; in this case, a
# string of characters that spell "Hello, world!"

# This value is called the argument. An argument is any value that is
# passed to a function when it is called. Some functions require multiple
# arguments, and some don't require any at all.

print(2 + 2)
# This time, instead of a string of characters we are passing a math
# expression as the argument to the print() function. The expression
# "2 + 2" will be calculated by Python and the result, 4, will be
# printed to the console.

# As you can see, the print() function can accept many types of arguments,
# not just strings.

# print() is just one of many built-in Python functions. Programmers can
# also define their own functions. We'll get into this later.