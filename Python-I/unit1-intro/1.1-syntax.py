# Basic Python Syntax

# In Python, each line of code contains its own instruction.
# These instructions are executed from top to bottom.

# In some programming languages like Java and C++, indentation (spaces or tabs
# at the beginning of a line) is mainly for readability and doesn't affect the 
# program. However, in Python, spacing and indentation do matter.

# <--- Hash symbols are used to write comments, like this.
# Comments are ignored by Python when the code runs. They are meant for humans.
# Comments can help explain what the code does or temporarily disable parts of
# code for testing purposes.

'''
Triple quotes can also be used to write multi-line comments
like this one.
'''

# Throughout this course, I'll use comments to explain programming concepts.

print("Hello, world!")
# The above line of code should look just like the very first program you wrote.
# When run, it prints the text "Hello, world!" to the terminal below.
# The terminal is also sometimes called the 'console'.

# Inside the parentheses is the value we want to print; in this case, a string
# of characters that spell "Hello, world!"
# A string is a sequence of characters enclosed in quotes.

# The value inside the parentheses is called an argument.
# An argument is any value passed to a function when it is called.
# Some functions require multiple arguments, and some don't require any at all.

print(2 + 2)
# This time, instead of a string, we are passing a math expression to the
# print() function. The expression "2 + 2" will be calculated by Python and the
# result, 4, will be printed to the terminal.

# As you can see, the print() function can accept many types of input, not just
# strings. Many other programming languages require you to convert the input to
# a string before printing it, but Python handles this automatically.

# Here are a few more examples of using the print() function:
print("Python is fun!")
print(10 * 3)
print("The sum of 5 and 7 is", 5 + 7)

# The print() function is just one of many built-in Python functions.
# Programmers can also define their own functions. We'll learn how to do that
# very soon, and that's where programming gets really fun!
